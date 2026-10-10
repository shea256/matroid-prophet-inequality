# Review and next work

The selected paper certifies
`8003458533570087953/16807475946150704657203200000 > (51/50)*2^-31`,
approximately `4.76184440734e-10`. This is **14.97% larger** than the preceding
retained-basis certificate. The same one-sample and full-seed adversary model
is retained; the seed drops from `42n+27` to `40n+26` fair bits. Independent
mathematical review and formalization remain pending.

The [versioned workflow](results/README.md) combines the
[shared framework](paper/framework.md) with the
[selected argument](results/activation-split.md). The preceding
[retained-basis publication](archive/retained-bases/README.md) is an unchanged
snapshot of merged commit `6d94154`. Stable paper links, the README progress
table, and result metadata are generated. Workflow checks establish
publication consistency, not the theorem.

Review in this order:

1. Fix filter/density masks before classifying membership in the activation
   flat. Check that outside labels have only valid births before parity and
   that the conditional safety loss is at most `j0/4`.
2. Check activation-generator positions and forced retention in both streams.
   Their labels remain enumerated. Active generators retain time variables,
   have two types, and may be omitted in the second stream. Verify the count
   `4^j1*S_(j1+z)(2y)` and zero-size cases.
3. Check the exact joint membership law, especially generator/residual
   overlap. Verify the `p^(-|J intersect Y|)` correction and the disjoint-role
   product before taking a union bound over adaptively selected sets.
4. Cancel `E j0/4` before applying the total generator budget. Check the new
   rank interface and projected/full rank relation, including absence of
   focal test bits from the witnesses.
5. Retain both later costs `Kt` and `K*rho/kappa`, the additive `1/d` tail
   error, small groups, and the maximum-branch cancellation condition.
   Recalculate the coefficient, exact tilts, and seed count.
6. Review the inherited reconstruction and projection arguments, quadratic
   potential, reverse containment, hybrid comparison, and lossless full-seed
   sample/value simulation.

The [audit](proofs/activation_split_audit.md) records a same-agent second pass.
Finite cases and exact scalar checks do not prove assertions for arbitrary
matroids. No independent review is claimed.

Further progress might sharpen the overlap charge using actual support
constraints or strengthen the safety/cost relation beyond the abstract
half-exit estimate. Neither is established here. The parameter search does
not prove an optimum or a ceiling. The abstract hazard bound `1/2` remains
sharp without additional structure. Verify newer primary sources before
asserting novelty; comparison limits are in [BASELINE.md](BASELINE.md).
