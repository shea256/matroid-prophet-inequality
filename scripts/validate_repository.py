#!/usr/bin/env python3
"""Validate generated paper inputs, exact metadata, archives, and local links."""
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

from result_registry import ROOT, archive_hashes
from build_manuscript import verify_generated, verify_build


def validate(root=ROOT):
    verify_generated(root)
    build = verify_build(root)
    archived = archive_hashes(root)
    links = 0
    for source in root.rglob('*.md'):
        relative = source.relative_to(root)
        if any(part in ('.git', '.context') for part in relative.parts):
            continue
        # Unchanged publication links refer to the original repository context.
        # Their bytes are checked against manifests; their current indexes below
        # are still link-checked normally.
        if source.resolve() in archived:
            continue
        for target in re.findall(r'!?\[[^\]]*\]\(([^)\n]+)\)', source.read_text()):
            target = target.strip('<>')
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            destination = (source.parent/unquote(parsed.path)).resolve()
            if root.resolve() not in destination.parents and destination != root.resolve():
                raise ValueError('Link leaves repository: '+str(relative)+' -> '+target)
            if not destination.exists():
                raise ValueError('Missing local link: '+str(relative)+' -> '+target)
            links += 1
    current = json.loads((root/'results/current.json').read_text())
    return dict(local_links_checked=links, immutable_artifacts_checked=len(archived),
                current_result=current['result_id'], generated_text_verified=True,
                paper_input_hashes_verified=True, paper_hash_verified=True,
                source_hash_verified=True, result='PASS (package validation, not a proof check)')


if __name__ == '__main__':
    print(json.dumps(validate(), indent=2))
