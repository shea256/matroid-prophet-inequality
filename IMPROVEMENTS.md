# Improvement record

## Recorded checkpoints — October 10, 2026

Current coefficient: **greater than `2^-34`**, with exact certificate
`C_1=14995972860899/244123247301151948800000` and `37n+24` fair bits.
The new step combines shared-variable residual encoding with a density cutoff.
Independent review and formalization are pending.

The result was developed through earlier internal
checkpoints on the same date:

| Bound | Main change | Proof and certificate | Status |
|---|---|---|---|
| `2^-63` | Source-parameter refinement, affine branch mixture, finite rounding offsets | [Proof](archive/2026-10-10/proofs/parameter_refinement.md), [paper](archive/2026-10-10/manuscript/note.pdf), [certificate](archive/2026-10-10/verification/certify_constants.py) | Superseded; written proof and same-agent verification |
| `2^-43` | Logarithmic hazard potential and tighter residual accounting | [Proof](archive/2026-10-10/proofs/hazard_potential.md), [addendum](archive/2026-10-10/manuscript/hazard_addendum.pdf), [certificate](archive/2026-10-10/verification/certify_hazard_constants.py) | Superseded; written proof and same-agent verification |
| `2^-36` | Quadratic potential, integrated residual bound, revised masks and finer phases | [Published version](https://github.com/shea256/matroid-prophet-inequality/tree/669e97c863aa7863c93258a5a1e2c6d9165b2d2b), [certificate](verification/certify_quadratic_constants.py) | Published; superseded on this branch |
| `2^-34` | Shared-variable residual encoding and density cutoff | [Current proof](manuscript.md), [paper](manuscript.pdf), [certificate](verification/certify_joint_residual.py) | Proposed refinement; written proof and same-agent verification |

This table records the project's derivation history, not independent priority
claims or separate discoveries of the original theorem. No earlier
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
