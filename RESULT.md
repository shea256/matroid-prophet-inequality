# Current result

**Claimed theorem with a written proof: a guarantee greater than `2^-36`**
for one-sample matroid prophet selection in the original full-seed almighty
model. The compact exact lower bound is
`9652683394380719 / 637507023635152349901619200`, approximately
`1.0405020 * 2^-36`. The construction uses `38n+23` initial fair bits.

The key lemma establishes `E P >= (1+p_start^2)/2 >= 1/2` by a quadratic
query potential. A repeated-OR construction approaches `1/2`, proving the
abstract lemma's sharpness. This is not a hard instance for the full matroid
theorem. The final calculation additionally integrates the residual tail,
recalibrates mask probabilities, and uses a finer finite rational phase mesh.

| Evidence category | Status |
|---|---|
| Universal mathematical claim | Written proof with explicit source dependencies |
| Exact coefficient | Standard-library rational certificate passes |
| Reverse process | 4,916 local quadratic checks and 3,153 global checks pass on the declared finite cases |
| Other ingredients | Adaptive Boolean events, biased filtering, residual expectations, and phase boundaries checked |
| Same-agent audit | Completed; no remaining gap identified |
| Independent peer review | Pending |
| Lean formalization of this refinement | Not performed |
| Strongest-current-result / novelty comparison | Unresolved while the announced proof is unavailable |
| Polynomial-time or practical-performance improvement | Not claimed |

Finite tests support the argument; the universal claim rests on the written
proof. Review status is not a claim that finite enumeration proves all matroids.
The private repository contains the manuscript with reproducible evidence.

See [the paper](manuscript.md), [verification scope](verification/README.md),
[baseline](BASELINE.md), and [review questions](HANDOFF.md).
