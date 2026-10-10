# Improvement record

## Initial standalone draft — October 10, 2026

Current coefficient: **greater than `2^-36`**, with compact exact lower
bound `C_0=9652683394380719/637507023635152349901619200` and `38n+23` fair bits.
The main contribution is the quadratic exit-hazard proof, combined with the
integrated residual estimate and recalibrated masks and rational phases.
Independent review and formalization are pending.

The result was developed through earlier internal
checkpoints on the same date:

| Checkpoint | Main change | Relationship to current draft |
|---|---|---|
| `2^-63` | Source-parameter refinement, affine branch mixture, finite offsets | Superseded quantitative analysis |
| `2^-43` | Logarithmic hazard potential and sharper residual accounting | Superseded exit argument |
| `2^-36` | Quadratic potential, integrated tail, revised masks and finer phases | Current manuscript |

This table records the project's derivation history, not independent priority
claims or three separate discoveries of the original theorem. No earlier
checkpoint is needed to read the current paper; it includes the rule and
all changed deductions. Source structural lemmas remain explicit dependencies.

Future public versions should retain stable `manuscript.md`, `manuscript.pdf`,
and `tex/manuscript.tex` entry points. Previous versions remain in Git history.
