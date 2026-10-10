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
for byte in `LICENSES/MIT.txt` at that checkpoint, with provenance recorded in
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

## Author and presentation — October 10, 2026

At the author's request, added Ryan Shea to the paper's title page and PDF
metadata, Markdown manuscript, README, attribution, and result metadata.
Removed the draft label from the paper and current project descriptions.
Independent-review status, AI-assistance disclosures, and source attribution
are retained. No mathematical claim, algorithm, or verification code changed.

Rebuilt the seven-page paper with `python3 -B scripts/build_manuscript.py`;
all three passes completed with zero warnings. The source and PDF hashes
were updated in [paper_build.json](verification/paper_build.json). `pdfinfo`
confirmed the author field, extracted PDF text confirmed the byline and
label removal, and the rendered first page was visually inspected.

`python3 -B scripts/run_checks.py`,
`python3 -B scripts/validate_repository.py`, and `git diff --check` passed.
All three current verification programs reproduced their reference outputs.

## Consolidate inherited notice — October 10, 2026

At the maintainer's request, removed the `LICENSES` directory. Its sole file
held the inherited MIT notice retained during the Apache 2.0 change; that
text is now included verbatim in the root [NOTICE](NOTICE). Updated README,
attribution, contributor instructions, and the earlier log link to reflect
the new location. The root Apache 2.0 license is unchanged.

A byte comparison confirmed that NOTICE retains the entire former file.
`python3 -B scripts/run_checks.py`,
`python3 -B scripts/validate_repository.py`, and `git diff --check` passed.
The manuscript and mathematical code were not changed.

## Baseline presentation and intermediate archive — October 10, 2026

At the author's request, removed the external announcement from the abstract,
README comparison table, announcement copy, and current scalar comparator
field. The main comparison now uses the `2^-293` coefficient derived in the
accessible OpenAI manuscript. A short related-work note acknowledges the
unverified announcement and states that its assumptions and proof were
unavailable for comparison at the audit date. The mathematical coefficient,
algorithm, and review status are unchanged.

Added a short development history to the current Markdown and PDF paper and
expanded [IMPROVEMENTS.md](IMPROVEMENTS.md). The [dated archive](archive/README.md)
preserves 23 original artifacts totaling 564,467 bytes: the `2^-63` note and
derivation, the `2^-43` addendum and derivation, their certificates and finite
checks, and supporting provenance. All copied files are unchanged and listed
with hashes in the archive manifest. The first checkpoint was recovered from
commit `c078169da3b6cb8cca4802fb4490ed09799bc736`; the later artifacts came
from the existing research workspace without assigning them a prior commit.
Historical labels and comparisons remain in the snapshots and are explicitly
identified as historical in the archive index.

Executed:

```sh
python3 -B scripts/build_manuscript.py > verification/paper_build.json
python3 -B scripts/check_archive.py --full --receipt verification/archive_run_receipt.json
python3 -B scripts/run_checks.py --receipt verification/current_run_receipt.json
python3 -B scripts/validate_repository.py
git diff --check
```

All 23 archived hashes matched. All five archived programs reproduced their
preserved JSON outputs, including 5,347,942 arrival-order runs, in 33.607
seconds on Python 3.9.25/Linux. The three current programs also matched their
updated references. Only the current scalar output's comparator reporting
field changed; all theorem parameters and coefficient fields matched the
previous version exactly. The first current-suite attempt reached package
validation before the archive receipt existed; after that receipt completed,
the current suite and package validation passed. Actual executions are
recorded in the two receipts above.

The current PDF remains seven pages and rebuilt in three passes with no
warnings. Its first and last pages were rendered and visually inspected;
the abstract uses the documented baseline, and the closing section contains
the qualified related-work note and development history. PDF and TeX hashes
were refreshed. These checks are not independent mathematical review.

## License provenance correction and accessible announcement — October 10, 2026

The author clarified that the MIT license had been introduced during our
preparation under a mistaken assumption; it was not an inherited license.
Removed the incorrect inheritance sentence from README, the corresponding
claims from attribution and contributor instructions, and the MIT text from
NOTICE. Apache 2.0 remains the project license, and NOTICE retains OpenAI
source attribution and names Ryan Shea. Earlier entries about preserving an
inherited MIT notice record that mistaken assumption, not the corrected
provenance.

Reworked the prepared announcement into a two-post thread using limited team
slots as an illustration of irreversible online selection. The follow-up
credits OpenAI's qualitative result and states the improved expected-reward
bound, Codex assistance, and invitation for independent review. Technical
context explains the analogy and assumptions. No announcement was posted.

The final package validator checked 102 local links and both paper hashes.
The archive hash check and three default archived programs passed again after
the archive index's attribution edit. Both prepared posts fit within 280
characters even counting the repository URL in full. README, attribution,
and NOTICE contain no MIT claim or text; `LICENSES` is absent. Whitespace
checks passed.
