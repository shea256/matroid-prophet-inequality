#!/usr/bin/env python3
"""Verify preserved checkpoint artifacts and reproduce their recorded checks."""
import argparse
import hashlib
import json
from pathlib import Path
import platform
import subprocess
import sys
import time

sys.dont_write_bytecode = True
from validate_repository import ROOT, validate
from result_registry import archive_hashes

ARCHIVE = ROOT / 'archive/2026-10-10'
CHECKS = (
    ('certify_constants.py', 'constants_output.json'),
    ('certify_hazard_constants.py', 'hazard_constants_output.json'),
    ('check_hazard_potential.py', 'hazard_potential_output.json'),
)
EXTENDED = (
    ('finite_checks.py', 'finite_output.json'),
    ('check_online_rule.py', 'online_output.json'),
)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--full', action='store_true',
                        help='also reproduce archived exhaustive structural checks')
    parser.add_argument('--receipt', type=Path,
                        default=ROOT / '.context/archive-checks.json')
    args = parser.parse_args()
    started = time.monotonic()
    manifest_bytes = (ARCHIVE / 'manifest.json').read_bytes()
    manifest = json.loads(manifest_bytes)
    snapshot_count = len(archive_hashes(ROOT))
    print('PASS all '+str(snapshot_count)+' archived artifact hashes', flush=True)

    records = []
    for script, reference in CHECKS + (EXTENDED if args.full else ()):
        print('Running archived ' + script, flush=True)
        before = time.monotonic()
        script_path = ARCHIVE / 'verification' / script
        reference_path = ARCHIVE / 'verification' / reference
        result = subprocess.run([sys.executable, '-B', str(script_path)],
                                cwd=ROOT, text=True, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        if result.returncode:
            raise SystemExit(result.stdout + result.stderr)
        if json.loads(result.stdout) != json.loads(reference_path.read_text()):
            raise SystemExit('Archived check differs from reference: ' + script)
        records.append({
            'script': script_path.relative_to(ROOT).as_posix(),
            'reference': reference_path.relative_to(ROOT).as_posix(),
            'script_sha256': hashlib.sha256(script_path.read_bytes()).hexdigest(),
            'seconds': round(time.monotonic() - before, 3),
            'result': 'PASS; fresh JSON equals preserved reference',
        })
        print('PASS archived ' + script, flush=True)

    receipt = args.receipt if args.receipt.is_absolute() else ROOT / args.receipt
    receipt.parent.mkdir(parents=True, exist_ok=True)
    report = {
        'python': platform.python_version(), 'platform': platform.system(),
        'archive_manifest_sha256': hashlib.sha256(manifest_bytes).hexdigest(),
        'archived_files_checked': len(manifest['files']),
        'all_snapshot_artifacts_checked': snapshot_count,
        'full_suite': args.full, 'checks': records,
        'seconds': round(time.monotonic() - started, 3),
        'scope': 'Historical scalar and finite checks; not independent review or universal formalization',
    }
    # Publish check results before validating links to this first recorded run.
    receipt.write_text(json.dumps(report, indent=2) + '\n')
    report['package'] = validate()
    report['result'] = 'PASS'
    receipt.write_text(json.dumps(report, indent=2) + '\n')
    print('PASS all requested archive checks and package validation', flush=True)


if __name__ == '__main__':
    main()
