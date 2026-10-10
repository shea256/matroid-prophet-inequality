# Improvement record

## Recorded checkpoints — October 10, 2026

Current coefficient: **greater than `2^-36`**, with compact exact lower
bound `C_0=9652683394380719/637507023635152349901619200` and `38n+23` fair bits.
The main contribution is the quadratic exit-hazard proof, combined with the
integrated residual estimate and recalibrated masks and rational phases.
Independent review and formalization are pending.

The result was developed through earlier internal
checkpoints on the same date:

| Bound | Main change | Proof and certificate | Status |
|---|---|---|---|
| `2^-63` | Source-parameter refinement, affine branch mixture, finite rounding offsets | [Proof](archive/2026-10-10/proofs/parameter_refinement.md), [paper](archive/2026-10-10/manuscript/note.pdf), [certificate](archive/2026-10-10/verification/certify_constants.py) | Superseded; written proof and same-agent verification |
| `2^-43` | Logarithmic hazard potential and tighter residual accounting | [Proof](archive/2026-10-10/proofs/hazard_potential.md), [addendum](archive/2026-10-10/manuscript/hazard_addendum.pdf), [certificate](archive/2026-10-10/verification/certify_hazard_constants.py) | Superseded; written proof and same-agent verification |
| `2^-36` | Quadratic potential, integrated residual bound, revised masks and finer phases | [Current proof](manuscript.md), [paper](manuscript.pdf), [certificate](verification/certify_quadratic_constants.py) | Current; written proof and same-agent verification |

This table records the project's derivation history, not independent priority
claims or three separate discoveries of the original theorem. No earlier
checkpoint is needed to read the current paper; it includes the rule and
all changed deductions. Source structural lemmas remain explicit dependencies.

The [archive index](archive/README.md) records dates, review status, provenance,
and reproduction commands. Original artifacts are preserved byte for byte,
including historical comparisons and labels; they are not current claims.
The `2^-63` checkpoint has an original commit. The `2^-43` files were retained
in the research workspace and are archived here without inventing a prior
commit or publication date. The `2^-43` addendum relies on the archived
`2^-63` note for the unchanged construction and accounting definitions.

Future public versions should retain stable `manuscript.md`, `manuscript.pdf`,
and `tex/manuscript.tex` entry points. Previous versions remain in Git history.
