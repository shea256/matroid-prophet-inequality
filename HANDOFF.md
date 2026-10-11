# Review and next work

The selected three-state refinement certifies
`4084754449786906742230661/8009094702029267287249256448000000 > (35/32)*2^-31`,
approximately `5.10014502482e-10`. This is **7.1044% larger** than the preceding
exact activation-split coefficient. It remains below `2^-30`. The one-sample
and full-seed adversary model is retained; seed usage grows from `40n+26`
to `47n+27` fair bits. Independent review and formalization are pending.

The [versioned workflow](results/README.md) combines the unchanged
[shared framework](paper/framework.md) with the
[selected argument](results/support-refinement.md). The previous announced
[activation-split publication](archive/activation-split/README.md) is an
unchanged snapshot of merged commit `4f650d6`. Stable paper links, the README
table, result metadata, and guarantee chart are generated. Workflow checks
establish publication consistency, not the theorem.

Review in this order:

1. Once a generator is omitted from the second retained basis, its signed
   first score is its only remaining variable. Verify that merging parity
   states leaves both affine tests fixed and gives `3^j1*S_(j1+z)(2y)`.
2. Check fixed residual exclusions: activation and retained wrong-parity
   generators cannot occur; retained valid-parity and omitted generators
   can occur. The explicit omitted-but-residual example prevents deleting
   the latter overlap charge.
3. Verify the joint mask law and disjoint-role generating weights, including
   the two `1/p` corrections and the rational coefficient `2/3`.
4. Audit inherited activation-conditioned safety, retained-basis reconstruction,
   projected witnesses, absence of focal test bits, and quarter-charge
   cancellation before the generator budget.
5. Recalculate all K-dependent later costs, the additive tail and small-group
   losses, maximum-branch cancellation, finite phases, exact tilts, and seed.
6. Review the quadratic potential, reverse containment, hybrid comparison,
   and lossless full-seed sample/value simulation.

The [audit](proofs/support_refinement_audit.md) records a same-agent second
pass. Finite examples and exact scalar checks do not prove the universal
assertions. No independent review is claimed.

The additional forced-pivot numerical mode is excluded from the selected
proof. Further progress may require stronger support constraints or an
improved safety/cost relation. The abstract half-exit estimate is sharp
without additional structure; parameter searches prove no ceiling. Refresh
primary sources before asserting novelty; see [BASELINE.md](BASELINE.md).
