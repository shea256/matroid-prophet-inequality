#!/usr/bin/env python3
"""Build the current paper; keep TeX intermediate files out of the repo."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile


def main():
    folder = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', type=Path, default=folder/'tex/manuscript.tex')
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    source = args.source.resolve()
    if not source.is_file() or source.suffix != '.tex':
        parser.error('--source must name an existing .tex file')
    output = args.output or folder/'manuscript.pdf'
    if shutil.which('pdflatex') is None:
        parser.error('pdflatex is required; see README.md')
    env = dict(os.environ, SOURCE_DATE_EPOCH='1791590400', FORCE_SOURCE_DATE='1')
    with tempfile.TemporaryDirectory(prefix='matroid-111-tex-') as tmp:
        for _ in range(3):
            result = subprocess.run(
                ['pdflatex', '-interaction=nonstopmode', '-halt-on-error',
                 '-no-shell-escape', '-output-directory='+tmp, source.name],
                cwd=source.parent, env=env, text=True, stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT)
            if result.returncode:
                raise SystemExit(result.stdout)
        log = (Path(tmp)/(source.stem+'.log')).read_text()
        warnings = [line for line in log.splitlines()
                    if 'Warning' in line or 'Overfull' in line]
        output.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(Path(tmp)/(source.stem+'.pdf'), output)
    print(json.dumps({'pdf': output.name, 'bytes': output.stat().st_size,
                      'sha256': hashlib.sha256(output.read_bytes()).hexdigest(),
                      'source': source.relative_to(folder).as_posix(),
                      'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
                      'passes': 3, 'warnings': warnings}, indent=2))


if __name__ == '__main__':
    main()
