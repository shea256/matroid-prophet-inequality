# Review and next work

The selected paper certifies
`548933908320757/1325382348737372749824000 > (7/4)*2^-32`, approximately
`4.14170227062e-10`. This is **71.46% larger** than PR #2's exact certificate
and remains below `2^-31`. The same one-sample and full-seed adversary model
is retained; the seed grows from `36n+23` to `42n+27` fair bits. Independent
mathematical review and formalization remain pending.

The [versioned workflow](results/README.md) combines the
[shared framework](paper/framework.md) with the
[selected argument](results/retained-bases.md). The previous
[rank-charged publication](archive/rank-charged/README.md) is an unchanged
snapshot of commit `ff4187f`. Stable paper links and metadata are generated;
workflow checks establish consistency, not the theorem.

Review in this order:

1. Prove that retained movable occurrences determine old retained occurrences
   by contraction, including repeated labels. Check forced retention of all
   first-stream generators and second-stream witnesses; second generators
   may be omitted. The resulting basis/type count is `6^j`.
2. Verify projected witnesses, `z' <= z`, the exact projected residual test,
   and `sigma <= kappa*z'+|R_Y|`. The comparison optimum is fixed before the
   focal bits, and no test-bit dependence or optimum access enters the rule.
3. Check fixed-family counting before focal masks, all three generator types,
   and the shared affine dimension. Adaptive selection is handled by a union
   bound; no extra generator-membership probability is assumed.
4. Track both changed costs `Kt` and `K*rho/kappa`, projected safety coefficient
   `gamma_bar`, and the additive loss. Check the geometric sum and cancellation
   `(1-t)*(gamma_bar*kappa+a0)/K <= 1/4` explicitly.
5. Check the unrounded log intervals and integer-power tilt comparisons. The
   coarse `49/50` decay is valid for errors but insufficient for the first tilt.
6. Review the inherited quadratic potential, reverse containment, safety
   comparison, and lossless full-seed sample/value simulation.

The [audit](proofs/retained_basis_audit.md) records a same-agent second pass.
Finite structural cases and exact scalar checks do not prove assertions for
arbitrary matroids. No independent review is claimed.

A further advance may exploit dependencies among generator types, witness
supports, and residual labels, or sharpen the safety/cost interface. The
parameter search does not establish an optimum or a ceiling. The abstract
hazard bound `1/2` remains sharp without additional structure. Verify newer
primary sources before asserting novelty; comparison limits are in
[BASELINE.md](BASELINE.md).
