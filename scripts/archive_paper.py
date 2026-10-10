#!/usr/bin/env python3
"""Preserve an existing committed publication without changing earlier snapshots."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
REPO = 'https://github.com/shea256/matroid-prophet-inequality'


def archive(result_id, revision):
    if not re.fullmatch(r'[a-z0-9][a-z0-9-]*', result_id):
        raise ValueError('Result ID must use lowercase letters, numbers, and hyphens')
    commit = subprocess.check_output(['git', 'rev-parse', '--verify', revision+'^{commit}'],
                                     cwd=ROOT, text=True).strip()
    dest = ROOT/'archive'/result_id
    if dest.exists():
        raise ValueError('Refusing to overwrite an existing snapshot: '+str(dest))
    paths = subprocess.check_output(['git', 'ls-tree', '-r', '--name-only', commit],
                                    cwd=ROOT, text=True).splitlines()
    selected = [p for p in paths if p in ('manuscript.md', 'manuscript.pdf', 'tex/manuscript.tex',
                 'tex/preamble.tex', 'verification/paper_build.json', 'verification/current_run_receipt.json')
                or p.startswith('paper/') or p.startswith('results/')]
    # Read everything before writing the snapshot.
    contents = [(p, subprocess.check_output(['git', 'show', commit+':'+p], cwd=ROOT)) for p in selected]
    for required in ('manuscript.md', 'manuscript.pdf', 'tex/manuscript.tex'):
        if required not in selected:
            raise ValueError('Revision has no '+required)
    files = []
    for path, data in contents:
        target = dest/path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
        files.append(dict(path=path, bytes=len(data), sha256=hashlib.sha256(data).hexdigest()))
    (dest/'manifest.json').write_text(json.dumps(dict(result_id=result_id, source_commit=commit,
                                                     files=files), indent=2)+'\n')
    (dest/'README.md').write_text(f'''# Preserved {result_id} publication

Unchanged artifacts from [commit {commit[:12]}]({REPO}/tree/{commit}).

- [PDF](manuscript.pdf)
- [Markdown snapshot](manuscript.md)
- [LaTeX snapshot](tex/manuscript.tex)
- [SHA-256 manifest](manifest.json)

Relative links inside the original documents describe their original repository
context. Use the pinned commit above to navigate that complete version.
Snapshots are immutable; corrections belong in current records and this index.
''')
    return dict(archive=dest.relative_to(ROOT).as_posix(), source_commit=commit, files=len(files))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--result-id', required=True)
    parser.add_argument('--commit', required=True)
    args = parser.parse_args()
    print(json.dumps(archive(args.result_id, args.commit), indent=2))
