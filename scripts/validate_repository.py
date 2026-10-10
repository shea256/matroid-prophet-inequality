#!/usr/bin/env python3
"""Validate package links, current-result metadata, and paper artifact hashes."""
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


def validate():
    links = 0
    for source in ROOT.rglob('*.md'):
        relative = source.relative_to(ROOT)
        if any(part in ('.git', '.context') for part in relative.parts):
            continue
        for target in re.findall(r'!?\[[^\]]*\]\(([^)\n]+)\)', source.read_text()):
            target = target.strip('<>')
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            destination = (source.parent/unquote(parsed.path)).resolve()
            if ROOT not in destination.parents and destination != ROOT:
                raise ValueError('Link leaves repository: '+str(relative)+' -> '+target)
            if not destination.exists():
                raise ValueError('Missing local link: '+str(relative)+' -> '+target)
            links += 1
    current = json.loads((ROOT/'results/current.json').read_text())
    certificate_path = (ROOT/current['certificate']).resolve()
    if ROOT not in certificate_path.parents:
        raise ValueError('Certificate path leaves repository')
    certificate = json.loads(certificate_path.read_text())
    for key in ('simplified_guarantee', 'certified_coefficient_lower_bound', 'seed_bits', 'parameters', 'base'):
        if current[key] != certificate[key]:
            raise ValueError('Result/certificate mismatch: '+key)
    build = json.loads((ROOT/'verification/paper_build.json').read_text())
    pdf = ROOT/build['pdf']
    source = ROOT/build['source']
    if pdf.stat().st_size != build['bytes']:
        raise ValueError('PDF size differs from build receipt')
    for path, expected in ((pdf, build['sha256']), (source, build['source_sha256'])):
        if hashlib.sha256(path.read_bytes()).hexdigest() != expected:
            raise ValueError('Artifact hash mismatch: '+str(path.relative_to(ROOT)))
    if build['warnings']:
        raise ValueError('Paper build contains warnings')
    return {'local_links_checked': links, 'current_result': current['result_id'],
            'paper_hash_verified': True, 'source_hash_verified': True,
            'result': 'PASS (package validation, not a proof check)'}


if __name__ == '__main__':
    print(json.dumps(validate(), indent=2))
