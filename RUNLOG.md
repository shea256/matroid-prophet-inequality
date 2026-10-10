# Reproduction log

Preparation date: October 10, 2026. This log includes historical private
preparation; the author subsequently made the repository public and reported
announcing the `2^-36` result. No social-media post was made by this agent.

The initial manuscript consolidated the `2^-36` derivation, algorithm
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

## Joint residual refinement — October 10, 2026

Prepared the requested pull request for the coefficient above `2^-34`,
retaining the published `2^-36` version at commit `669e97c`. The new proof
shares generator variables across the two residual pivot tests and charges
a density-size cutoff's exceptional event explicitly. Updated the stable
Markdown, TeX, and PDF, result metadata, attribution, and reproduction entry
points. Corrected obsolete private-repository wording to reflect the
maintainer's subsequent public release. No social-media post or merge was made.

Executed:

```sh
python3 -B scripts/build_manuscript.py > verification/paper_build.json
python3 -B scripts/run_checks.py --full --receipt verification/current_run_receipt.json
python3 -B experiments/search_joint_residual.py > .context/joint-search-rerun.json
cmp .context/joint-search-rerun.json experiments/joint_residual_search_output.json
python3 -B scripts/check_archive.py
python3 -B scripts/validate_repository.py
git diff --check
```

All seven full-suite programs passed and reproduced their stored JSON on
Python 3.9.25/Linux in 41.645 seconds. The new finite checker covered 45,824
actual residual encodings and 331,491 affine signs, plus its stated boundary
and negative-control cases. The numerical search reproduced byte for byte.
All 23 archived hashes and the three default archive checks passed.
The nine-page PDF rebuilt in three passes with zero warnings; pages 1, 5,
and 7 were rendered and visually inspected. Source/PDF hashes and 117 local
links passed package validation before this log entry. Same-agent verification
is not independent mathematical review; that remains pending.

## Versioned paper workflow and rank-charged result — October 10, 2026

After the maintainer merged PR #1 at `08300e2`, prepared a follow-up on
`shea256/versioned-paper-rank-charge`. The user requested the versioned
paper-update pattern used in the Fourier repository. Added shared proof
sources, immutable result records, an explicit current-result registry,
and a builder that regenerates the stable Markdown, TeX, PDF, current
metadata, README headline, and improvement history. Candidate records
cannot become current; independent review remains a separate status.

Integrated the previously derived rank-charged proof with exact coefficient
`773895463001/3203794364409053184000 > (33/32)*2^-32`. The shared accounting
now carries `K=kappa+nu` through all costs and the small-group loss. The
selected rule uses `36n+23` initial fair bits. This is about 3.93235 times
the preceding exact certificate, with the same one-sample/full-seed
adversary quantifier. No new novelty or independent-review claim is made.

Preserved the six committed publication files from `08300e2` in
`archive/joint-residual/`. Each was separately compared byte for byte with
`git show` at that commit. Together with the previous archive, 29 immutable
artifacts pass their recorded hashes. The new certificate and finite output
agree with the research-track evidence (apart from documented metadata-key
normalization); mathematical scripts retain the same calculation.

Executed:

```sh
python3 -B scripts/archive_paper.py --result-id joint-residual --commit 08300e2d9c4a8529db0198631716b7ef20dd8aa5
python3 -B scripts/build_manuscript.py
python3 -B scripts/run_checks.py --full --receipt verification/current_run_receipt.json
python3 -B scripts/check_archive.py --receipt verification/versioned_archive_run_receipt.json
python3 -B -m unittest discover -s scripts/tests
python3 -B experiments/search_rank_charged.py > .context/rank-search-rerun.json
cmp .context/rank-search-rerun.json experiments/rank_charged_search_output.json
python3 -B scripts/build_manuscript.py --check
python3 -B scripts/validate_repository.py
git diff --check
```

All 11 full-suite programs reproduced their stored JSON on Python
3.9.25/Linux in 43.451 seconds. The three default historical
programs passed in 0.762 seconds, and the numerical search reproduced
byte for byte. All 11 workflow tests passed, including deliberate stale
inputs, coefficient mismatches, candidate selection, archive/PDF mutation,
and a compiler failure that leaves published artifacts unchanged. These
workflow tests validate publication consistency, not mathematical claims.

The build used Pandoc 3.12.1 and pdfTeX 1.40.22. Pandoc was installed from
the official release after the system package manager had no matching
package; its tarball SHA-256 was
`d0c90410e90204c9ca83b8539fac5c7aed01fd537207e4585849f8abc5df20b8`.
An unavailable T1 font dependency and a code-font math warning were corrected
before the final build. The 11-page, 241053-byte PDF built in three passes
with zero warnings; pages 1, 8, 9, and 11 were rendered and visually inspected.
The build receipt binds all active paper inputs and generated artifacts.
Package validation checked 150 local links
and all 29 immutable artifacts before this log entry. Same-agent checks and
finite enumeration are not independent mathematical review.

## Retained-basis refinement — October 10, 2026

Packaged the previously derived retained-basis, additive-error, and projected-
witness argument as `results/retained-bases.md`. Its exact coefficient is
`548933908320757/1325382348737372749824000 > (7/4)*2^-32`, about 71.46%
above the preceding rank-charged coefficient, with the same model and
`42n+27` initial fair bits. Updated the shared accounting to carry the
projected safety coefficient and additive maximum-branch loss explicitly.
The registry now supports an exact rational multiplier on a power-of-two
threshold; the new result does not cross `2^-31`.

Prepared branch `shea256/retained-basis-refinement` from committed PR #2
head `ff4187f03456fe54e8dc0a68e691fdc15f6c707f`. Although the maintainer
reported #2 merged, repeated GitHub queries returned `OPEN`, `mergedAt: null`,
and fetched `master` remained `08300e2`. The new PR is therefore prepared
against #2's branch to isolate this refinement. This records the observed
remote state; no merge was performed by the agent.

Preserved 16 publication artifacts from `ff4187f` in `archive/rank-charged/`,
each separately compared byte for byte with `git show`. The earlier
29 artifacts remain unchanged. Copied research-track verifiers without
mathematical changes, adapting only the helper import and certificate
metadata (coefficient field name, equivalent simplified threshold text,
and explicit base description). The scalar and finite reference outputs
match the research-track evidence after those stated metadata changes.
The publication audit's obsolete equation-number references were replaced
with section descriptions, and its generator-type description was clarified.

Executed:

```sh
python3 -B scripts/archive_paper.py --result-id rank-charged --commit ff4187f03456fe54e8dc0a68e691fdc15f6c707f
python3 -B scripts/build_manuscript.py
python3 -B scripts/run_checks.py --full --receipt verification/current_run_receipt.json
python3 -B scripts/check_archive.py --receipt verification/retained_basis_archive_run_receipt.json
python3 -B -m unittest discover -s scripts/tests
python3 -B experiments/search_retained_basis.py > .context/retained-basis-search-rerun.json
cmp .context/retained-basis-search-rerun.json experiments/retained_basis_search_output.json
python3 -B scripts/build_manuscript.py --check
python3 -B scripts/validate_repository.py
git diff --check
```

All 13 full-suite programs reproduced their reference JSON on Python
3.9.25/Linux in 50.848 seconds. All 13 workflow tests passed, including
rejection of a mismatched multiplier and a coefficient above `2^-32` but
below the selected scaled threshold. The numerical search reproduced byte
for byte. All 45 archived hashes passed, and the three default historical
programs passed in 0.788 seconds. The new finite checks include 74,881
interleavings, 3,349 basis families, and 45,824 projected path charges.

The first paper build rejected a 3.45-point overfull line in the parameter
list; splitting that display fixed it. The final 12-page, 255060-byte PDF
built in three passes with zero warnings using Pandoc 3.12.1 and pdfTeX
1.40.22. Pages 1, 8, 9, 10, and 12 were rendered under `.context/` and
visually inspected. Package validation checked 172 local links, all 45
immutable artifacts, and current paper input/output hashes before this log
entry. These are same-agent arithmetic, finite, and publication checks;
independent mathematical review and formalization remain pending.

## README progress table — October 10, 2026

After PR #4 merged into `master` at `9bd129a`, added the requested four-row
progress table below the current result. It starts with the originally
announced quadratic-hazard certificate, highlights the selected result,
and links the earlier research checkpoints to the full development history.
The builder generates rows from the result registry and divides exact
coefficients before rounding display gains to two decimals: 1×, 4.06×,
15.95×, and 27.35×. The registry names the announcement baseline explicitly
so subsequent selected refinements update the table automatically.

Ran the full paper build to refresh its input hashes, then the default
11-program verification suite (18.67 seconds, fresh JSON equal to all
references), all 13 workflow tests, the read-only build check, package
validation, and `git diff --check`. Package validation covered 177 local
links and all 45 immutable artifacts. Independently recalculated displayed
ratios directly from the certificate files. The manuscript Markdown,
LaTeX, PDF, current result metadata, and full development history are
byte-identical to their versions on `master`; only README presentation,
its generation/configuration, workflow documentation, and build-input
hashes changed. This does not change any mathematical claim or review stage.

## Activation splitting above 2^-31 — October 10, 2026

Prepared on `shea256/activation-split-refinement` from merged master
`6d94154ae9961733b7604918a2d3b642d218d61e`, at the maintainer's request for
a new PR. Archived the preceding retained-basis publication before replacing
it: 17 unchanged artifacts, bringing the immutable total to 62. Each new
archived file also matched `git show` at the recorded source commit directly.

Integrated the activation-split proof and audit, normalized standalone imports
and the previous certificate's coefficient-field name, and copied the exact
reference outputs and deterministic numerical search. The shared framework
and old result records are unchanged. The selected record recalls the
reconstruction and projection lemmas so the current paper contains its
project-specific dependencies in one place. The conditional safety display
explicitly restricts sampled comparison labels to the focal group.

Actual commands:

```sh
python3 -B scripts/archive_paper.py --result-id retained-bases --commit 6d94154ae9961733b7604918a2d3b642d218d61e
python3 -B scripts/build_manuscript.py
python3 -B scripts/run_checks.py --full --receipt verification/current_run_receipt.json
python3 -B scripts/check_archive.py
python3 -B -m unittest discover -s scripts/tests
python3 -B experiments/search_activation_split.py > .context/activation_search_fresh.json
python3 -B scripts/build_manuscript.py --check
python3 -B scripts/validate_repository.py
git diff --check
```

All 15 full-suite programs passed on Python 3.9.25/Linux;
fresh JSON equaled every reference. The successful final suite took
85.344 seconds; this is reproduction timing, not algorithm
performance. Its hashes and individual timings are in the
[current receipt](verification/current_run_receipt.json). An earlier run
passed all programs but its final publication-consistency check caught a
manuscript made stale by a notation edit during the run. After rebuilding,
the entire suite and package validation passed with paper sources fixed.

All 13 workflow tests, all 62 archive hashes, and the archive's three default
verification programs passed. The numerical search reproduced its reference
JSON exactly. The 14-page PDF built in three passes with zero warnings,
265228 bytes, and SHA-256 `88210448ff7aa2351e95c1ce58827919a4953d36fdf9213ad917fe36f4e726a7`. Rendered pages 1, 9,
and 12 were inspected under `.context/`; generated Markdown/LaTeX/PDF hashes,
local links, and whitespace checks passed.

The coefficient is `4.76184440734e-10 > (51/50)*2^-31`, a 14.97% increase
over the preceding exact certificate, with `40n+26` initial fair bits. The
README table now includes the approximately 31.45-fold gain over the first
announced exact certificate. These remain written claims with same-agent
verification; independent review and formalization are pending.

## README progress graphic — October 10, 2026

The user supplied a step-chart reference and requested a matching README
image. PR #6 was already merged at `2cc1d21eace63b5dc6e56d70f3d3f94a98c7a43c`,
so this update uses a separate branch, `shea256/readme-progress-graphic`,
from merged master.

Generated `assets/guarantee-progress.png` (2560 by 1440, 256833 bytes) and
an SVG (98839 bytes) with Matplotlib 3.9.4 in an ignored local virtualenv.
The chart reads exact registry coefficients: a logarithmic comparison with
the derived OpenAI bound and a linear view of gains since the announcement.
Its horizontal axis is a refinement sequence; all displayed project dates
are October 10. Exact ratios and the greater-than-2^262 source comparison
were recalculated. The rendered graphic was inspected for labels and layout. Trailing
whitespace in the SVG export was normalized before final diff validation;
regeneration preserved the PNG bytes exactly.

The [data receipt](assets/guarantee-progress.json) binds the registry and
renderer inputs plus both image hashes. Added standard-library freshness
validation to the package checker, and documented optional chart regeneration.
The README embeds the PNG outside its generated result block. The manuscript,
PDF, LaTeX, and mathematical result registry match the merged publication.

Executed the renderer, `scripts/build_progress_graphic.py --check`,
`scripts/build_manuscript.py --check`, `scripts/validate_repository.py`,
`python3 -B -m unittest discover -s scripts/tests`, and `git diff --check`.
All passed, including 13 workflow tests and 62 archive hashes. The default
`scripts/run_checks.py --receipt .context/graphic-checks.json` run passed all
13 programs with fresh JSON equal to references and final package validation
in 42.367 seconds on Python 3.9.25/Linux.
This is a presentation update, not a new theorem or independent proof review.

## Graphic layout revision — October 10, 2026

At the user's request, removed the left source-comparison graph and expanded
the linear refinement chart to the full width. Retained the OpenAI baseline
as a source note, with the current guarantee and latest percentage increase
below the plot. Updated the README alt text, graphic documentation, renderer,
and PNG/SVG/data artifacts. Inspected the 2560x1360 rendering.

The graphic data/hash check, generated-paper check, package validation,
all 13 workflow tests, and `git diff --check` passed. Mathematical
coefficients and verification programs are unchanged; the previously passed
13-program suite was not repeated for this layout-only revision.
