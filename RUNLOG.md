# Reproduction log

Preparation date: October 10, 2026. This standalone repository is private at
the maintainer's request. Announcement wording is a draft; no social-media
announcement has been posted by this agent.

The manuscript consolidates the current `2^-36` derivation, algorithm
definitions, statistics, and source interfaces into one paper. Earlier
project notes are not required to read it. The structural results inherited
from the pinned OpenAI manuscript remain explicit dependencies.

The portable package uses Python 3.9+ and the standard library. pdfLaTeX is
required only to rebuild the paper. Commands for this package are:

```sh
python3 -B scripts/build_manuscript.py > verification/paper_build.json
python3 -B scripts/run_checks.py --full --receipt verification/run_receipt.json
python3 -B experiments/search_quadratic_parameters.py
python3 -B verification/fetch_sources.py
python3 -B scripts/validate_repository.py
```

The build and verification receipts record actual executions. The parameter
search is a declared finite family, not a global optimum. Upstream artifacts
are retrieved into an ignored cache and checked against the pinned manifest.

The original exact checks passed before extraction. This package reruns them
after making import and path handling independent of the research workspace.
Finite verification, exact scalar certification, and manuscript compilation
are separate from independent mathematical review, which remains pending.

## Executed standalone checks

All five programs in the full suite exited zero on Python 3.9.25/Linux.
Fresh JSON matched the stored references exactly. The recorded suite took
35.752 seconds in this environment; this is reproduction timing, not
algorithmic performance evidence. It includes the current scalar and
quadratic checks plus the retained structural checks over 92 small matroids
and 5,347,942 complete arrival-order runs. Detailed script hashes and timings
are in [run_receipt.json](verification/run_receipt.json).

The standalone exact search reproduced the recorded 8,064-tuple output
byte for byte, with 3,234 feasible certificates. Fresh retrieval verified all
20 upstream artifacts against the pinned source manifest. The optional
source cache is ignored and is not part of the repository upload.

The consolidated seven-page PDF builds in three pdfLaTeX passes with zero
warnings. [paper_build.json](verification/paper_build.json) records the final
source and PDF hashes. After the full numerical suite, editorial changes
clarified the missing external proof, distinguished the loop flat from the
scalar loss, and made the Markdown math render on GitHub. The paper was
rebuilt and package links and source/PDF hashes were validated again.

Only the selected proof, documentation, verification code, references, and
small generated artifacts are included. Original repository history, unrelated
research, local caches, and credentials are excluded. The user explicitly
requested private visibility before repository creation.

## Apache 2.0 and upstream links — October 10, 2026

At the maintainer's request, replaced the root license with the Apache 2.0
text from the pinned OpenAI/math revision
`fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`. Its SHA-256 is
`c71d239df91726fc519c6eb72d318ec65820627232b2f796219e87dcf35d0ab4`.
The downloaded text matches the Apache Software Foundation's canonical
license apart from whitespace. The upstream root directory has no NOTICE
file. The original MIT copyright and permission notice was preserved byte
for byte in [LICENSES/MIT.txt](LICENSES/MIT.txt), with provenance recorded in
[NOTICE](NOTICE). README, attribution, and contributor instructions now
identify Apache 2.0 as the project license.

The README's opening reference now links directly to OpenAI's dedicated #111
page, with an adjacent link to the pinned original manuscript. The upstream
problem entry and the dedicated page were checked for the correct title and
model. No theorem, verifier, manuscript source, or PDF was modified.

Executed `python3 -B scripts/run_checks.py`,
`python3 -B scripts/validate_repository.py`, and `git diff --check`.
All three current verification programs and package checks passed. Byte
comparisons confirmed that LICENSE matches the pinned upstream license and
LICENSES/MIT.txt matches the previous commit's MIT license.
