# Superseded research checkpoints

The current result is in the [root manuscript](../manuscript.md). This archive
preserves the earlier `2^-63` and `2^-43` derivations from **October 10, 2026**,
as stages of the same research effort. Both have written proofs and same-agent
checks; neither has completed independent review or formalization.

## Read the checkpoints

| Bound | Contribution | Manuscript | Derivation | Exact certificate and output |
|---|---|---|---|---|
| `2^-63` | Parameters, affine branch mixing, and finite rounding offsets | [PDF](2026-10-10/manuscript/note.pdf), [TeX](2026-10-10/manuscript/note.tex) | [Proof](2026-10-10/proofs/parameter_refinement.md), [same-agent audit](2026-10-10/proofs/audit.md) | [Script](2026-10-10/verification/certify_constants.py), [output](2026-10-10/verification/constants_output.json) |
| `2^-43` | Logarithmic hazard potential and tighter residual accounting | [PDF addendum](2026-10-10/manuscript/hazard_addendum.pdf), [TeX](2026-10-10/manuscript/hazard_addendum.tex) | [Proof](2026-10-10/proofs/hazard_potential.md) | [Script](2026-10-10/verification/certify_hazard_constants.py), [output](2026-10-10/verification/hazard_constants_output.json) |

Read the `2^-43` addendum with the `2^-63` note: it replaces the exit argument
and constants while relying on the earlier construction and accounting
definitions. The [old certificate limitation](2026-10-10/proofs/certificate_limit.md)
applies to that old proof template, not to the later hazard arguments.

## Provenance and interpretation

The first checkpoint is preserved from
[original commit c078169](https://github.com/shea256/open-math-problems/commit/c078169da3b6cb8cca4802fb4490ed09799bc736),
dated October 10, 2026. The second checkpoint's artifacts were present in the
research workspace and were not previously committed there. Their document
date is October 10, 2026; no earlier commit or public-release time is asserted.

The [manifest](2026-10-10/manifest.json) records every original path, byte
length, SHA-256 hash, and available source commit. All 23 listed artifacts
are unchanged copies. The PDFs and historical text retain their original
labels, authorship presentation, and references to an unverified external
announcement. This preserves the record; those passages do not establish
current comparisons or independent validation. The current comparison uses
the accessible OpenAI manuscript, as explained in [BASELINE.md](../BASELINE.md).

## Reproduce

From the repository root, with Python 3.9+ and its standard library:

```sh
python3 -B scripts/check_archive.py
```

This checks all archived hashes, reruns both exact scalar certificates and
the old finite hazard checks, compares fresh JSON with the preserved outputs,
and validates repository links and current paper hashes. To also rerun the
retained exhaustive small-matroid and arrival-order programs:

```sh
python3 -B scripts/check_archive.py --full
```

The [recorded archive run](../verification/archive_run_receipt.json) states
which programs were actually run. These are arithmetic and finite checks,
not independent mathematical review or a universal proof checker.

Optional PDF rebuilds require pdfLaTeX and the packages listed in the root
README, plus `booktabs` for the original note. Keep rebuilds outside the
preserved archive:

```sh
python3 -B scripts/build_manuscript.py --source archive/2026-10-10/manuscript/note.tex --output .context/archived-note.pdf
python3 -B scripts/build_manuscript.py --source archive/2026-10-10/manuscript/hazard_addendum.tex --output .context/archived-hazard-addendum.pdf
```

The original PDFs are checked against their recorded hashes; rebuilt PDF
bytes may vary with the TeX environment. This archive is distributed with
the project's [license](../LICENSE) and [source attribution](../NOTICE).

## Joint residual publication above `2^-34`

The [joint-residual snapshot](joint-residual/README.md) preserves the complete
publication from merged commit `08300e2d9c4a8529db0198631716b7ef20dd8aa5`:
Markdown, nine-page PDF, LaTeX, result metadata, and build/check receipts.
Its six files have a separate SHA-256 manifest. Original relative links retain
their original repository context; the pinned commit provides full navigation.
The package validator verifies these bytes alongside the 23 earlier artifacts.
