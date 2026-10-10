#!/usr/bin/env python3
"""Fetch the pinned primary artifacts into the gitignored workspace cache."""
import argparse
import hashlib
import json
from pathlib import Path
import urllib.request

COMMIT = 'fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb'
PAPER = ('preprints/One-Sample-Suffices-for-Matroid-Prophet-Inequalities-'
         'against-an-Almighty-Adversary-September-23-2026')
PATHS = {
    'CONTENTS.md': 'CONTENTS.md',
    'source-README.md': 'README.md',
    '111.md': 'lean/docs/111.md',
    'README.md': PAPER+'/README.md',
    'final.pdf': PAPER+'/final.pdf',
    'main.tex': PAPER+'/build/main.tex',
    'literature.bib': PAPER+'/build/references/literature.bib',
    **{name+'.tex': PAPER+'/build/sections/'+name+'.tex' for name in (
        'introduction', 'setup', 'algorithm', 'safety', 'transfer', 'accounting', 'secretary')},
    **{name+'.'+ext: 'lean/ComparatorChallenges/'+name+'.'+ext
       for name in ('MatroidProphet', 'MatroidSecretary') for ext in ('lean', 'json')},
    'source-Main.lean': 'lean/OAI/Probability/MatroidProphet/Main.lean',
    'source-Constants.lean': 'lean/OAI/Probability/MatroidProphet/Constants.lean',
}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path,
                        default=Path(__file__).resolve().parents[1]/'.context/upstream')
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    manifest = json.loads(Path(__file__).with_name('source_manifest.json').read_text())
    expected = {item['cache_name']: item for item in manifest['artifacts']}
    artifacts = []
    for name, path in PATHS.items():
        url = 'https://raw.githubusercontent.com/openai/math/'+COMMIT+'/'+path
        data = urllib.request.urlopen(url, timeout=30).read()
        digest = hashlib.sha256(data).hexdigest()
        if len(data) != expected[name]['bytes'] or digest != expected[name]['sha256']:
            raise SystemExit('Source hash mismatch: '+name)
        (args.output/name).write_bytes(data)
        artifacts.append(dict(path=path, cache_name=name, bytes=len(data),
                              sha256=hashlib.sha256(data).hexdigest(), url=url))
    print(json.dumps(dict(repository='https://github.com/openai/math',
                          commit=COMMIT, artifacts=artifacts), indent=2))


if __name__ == '__main__':
    main()
