#!/usr/bin/env python3
"""Run actual verification programs and compare their outputs with references."""
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

CURRENT = (
    ('certify_joint_residual.py', 'joint_residual_constants_output.json'),
    ('check_joint_residual.py', 'joint_residual_checks_output.json'),
    ('certify_quadratic_constants.py', 'quadratic_constants_output.json'),
    ('check_quadratic_hazard.py', 'quadratic_hazard_output.json'),
    ('check_quadratic_ingredients.py', 'quadratic_ingredients_output.json'),
)
EXTENDED = (
    ('finite_checks.py', 'finite_output.json'),
    ('check_online_rule.py', 'online_output.json'),
)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--full', action='store_true', help='also run retained exhaustive structural checks')
    parser.add_argument('--receipt', type=Path, default=ROOT/'.context/checks.json')
    args = parser.parse_args()
    started = time.monotonic()
    records = []
    for script, reference in CURRENT+(EXTENDED if args.full else ()):
        print('Running '+script, flush=True)
        before = time.monotonic()
        completed = subprocess.run([sys.executable, '-B', str(ROOT/'verification'/script)],
                                   cwd=ROOT, text=True, stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
        if completed.returncode:
            raise SystemExit(completed.stdout+completed.stderr)
        actual = json.loads(completed.stdout)
        expected = json.loads((ROOT/'verification/reference'/reference).read_text())
        if actual != expected:
            raise SystemExit('Fresh output differs from recorded reference: '+script)
        records.append({'script': 'verification/'+script,
                        'reference': 'verification/reference/'+reference,
                        'seconds': round(time.monotonic()-before, 3),
                        'script_sha256': hashlib.sha256((ROOT/'verification'/script).read_bytes()).hexdigest(),
                        'result': 'PASS; fresh JSON equals reference'})
        print('PASS '+script, flush=True)
    package = validate()
    report = {'python': platform.python_version(), 'platform': platform.system(),
              'full_suite': args.full, 'checks': records, 'package': package,
              'seconds': round(time.monotonic()-started, 3),
              'scope': 'Exact scalar and finite checks; not independent review or universal formalization',
              'result': 'PASS'}
    receipt = args.receipt if args.receipt.is_absolute() else ROOT/args.receipt
    receipt.parent.mkdir(parents=True, exist_ok=True)
    receipt.write_text(json.dumps(report, indent=2)+'\n')
    print('PASS all requested checks and package validation', flush=True)


if __name__ == '__main__':
    main()
