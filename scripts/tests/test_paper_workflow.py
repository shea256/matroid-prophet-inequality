"""Workflow regressions; these test publication consistency, not mathematics."""
import copy
import json
from pathlib import Path
from fractions import Fraction
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import build_manuscript as paper
from result_registry import ROOT, archive_hashes, load, guarantee_text
from validate_repository import validate


class PaperWorkflow(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='matroid-workflow-test-')
        self.root = Path(self.tmp.name)/'repo'
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns('.git', '.context', '__pycache__'))

    def tearDown(self):
        self.tmp.cleanup()

    def registry(self):
        return json.loads((self.root/'results/registry.json').read_text())

    def selected(self, data):
        return next(r for r in data['results'] if r['id'] == data['current'])

    def save(self, data):
        (self.root/'results/registry.json').write_text(json.dumps(data))

    def test_current_package_is_consistent(self):
        report = validate(self.root)
        self.assertEqual(report['current_result'], self.registry()['current'])
        self.assertGreater(report['immutable_artifacts_checked'], 0)

    def test_coefficient_must_match_exact_certificate(self):
        data = self.registry()
        self.selected(data)['coefficient'] = '1/2'
        self.save(data)
        with self.assertRaisesRegex(ValueError, 'coefficient mismatch'):
            load(self.root)

    def test_duplicate_result_ids_are_rejected(self):
        data = self.registry()
        data['results'].append(copy.deepcopy(self.selected(data)))
        self.save(data)
        with self.assertRaisesRegex(ValueError, 'unique'):
            load(self.root)

    def test_unfinished_candidate_cannot_be_selected(self):
        data = self.registry()
        self.selected(data)['status'] = 'candidate'
        self.save(data)
        with self.assertRaisesRegex(ValueError, 'Current result must'):
            load(self.root)

    def test_bigger_candidate_does_not_select_itself(self):
        data = self.registry()
        candidate = copy.deepcopy(self.selected(data))
        candidate.update(id='unfinished', status='candidate', coefficient='1/2', exponent=2)
        data['results'].append(candidate)
        self.save(data)
        generated = json.loads(paper.generated(self.root)['results/current.json'])
        self.assertEqual(generated['result_id'], data['current'])
        self.assertEqual(generated['simplified_guarantee'], guarantee_text(self.selected(data)))

    def test_multiplier_must_match_certificate(self):
        data = self.registry()
        selected = self.selected(data)
        selected['multiplier'] = str(Fraction(selected.get('multiplier', 1)) + 1)
        self.save(data)
        with self.assertRaisesRegex(ValueError, 'guarantee mismatch'):
            load(self.root)

    def test_coefficient_must_exceed_scaled_guarantee(self):
        data = self.registry()
        selected = self.selected(data)
        # This is above 2^-32 but below (7/4)*2^-32. A validator that ignores
        # the multiplier would incorrectly accept the matching certificate.
        selected.update(coefficient='3/8589934592', exponent=32, multiplier='7/4')
        cert_path = self.root/selected['certificate']
        cert = json.loads(cert_path.read_text())
        cert[selected['coefficient_field']] = selected['coefficient']
        cert[selected['guarantee_field']] = guarantee_text(selected)
        cert_path.write_text(json.dumps(cert))
        self.save(data)
        with self.assertRaisesRegex(ValueError, 'does not exceed'):
            load(self.root)

    def test_paths_cannot_escape_repository(self):
        data = self.registry()
        self.selected(data)['certificate'] = '../outside.json'
        self.save(data)
        with self.assertRaisesRegex(ValueError, 'out-of-repository'):
            load(self.root)

    def test_generated_headline_edit_is_rejected(self):
        path = self.root/'README.md'
        path.write_text(path.read_text().replace('Current result:', 'Manually changed current result:'))
        with self.assertRaisesRegex(ValueError, 'Stale generated file: README.md'):
            paper.verify_generated(self.root)

    def test_framework_change_requires_pdf_rebuild(self):
        path = self.root/'paper/framework.md'
        path.write_text(path.read_text()+'\nA changed argument.\n')
        with self.assertRaisesRegex(ValueError, 'input hashes changed'):
            paper.verify_build(self.root)

    def test_pdf_change_is_rejected(self):
        path = self.root/'manuscript.pdf'
        path.write_bytes(path.read_bytes()+b'changed')
        with self.assertRaisesRegex(ValueError, 'artifact hash mismatch'):
            paper.verify_build(self.root)

    def test_historical_artifact_change_is_rejected(self):
        path = self.root/'archive/joint-residual/manuscript.md'
        path.write_text(path.read_text()+'\nchanged\n')
        with self.assertRaisesRegex(ValueError, 'Archived artifact changed'):
            archive_hashes(self.root)

    def test_compilation_failure_preserves_published_outputs(self):
        before = {p: (self.root/p).read_bytes() for p in
                  ('manuscript.md', 'manuscript.pdf', 'tex/manuscript.tex', 'results/current.json')}
        failure = subprocess.CompletedProcess([], 1, stdout='intentional compiler failure')
        with patch.object(paper.shutil, 'which', return_value='/fake/compiler'), \
             patch.object(paper, 'render_tex', return_value='invalid TeX'), \
             patch.object(paper.subprocess, 'run', return_value=failure):
            with self.assertRaisesRegex(ValueError, 'intentional compiler failure'):
                paper.build(self.root)
        self.assertEqual(before, {p: (self.root/p).read_bytes() for p in before})


if __name__ == '__main__':
    unittest.main()
