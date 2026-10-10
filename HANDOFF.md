# Review and next work

The selected paper gives more than `2^-32`, with exact certificate
`773895463001/3203794364409053184000`, approximately 3.93235 times the
preceding `2^-34` certificate. It retains the full one-sample model and
seed-visible adversary and uses `36n+23` initial fair bits. Independent
mathematical review and formalization remain pending.

The paper now uses the [versioned update workflow](results/README.md).
Edit the [shared framework](paper/framework.md),
[selected argument](results/rank-charged.md), and [registry](results/registry.json).
The stable Markdown, LaTeX, PDF, headline, history, and metadata are generated.
The [previous publication](archive/joint-residual/README.md) is preserved
unchanged. Workflow validation is not mathematical proof verification.

Review in this order:

1. Verify the joint affine representation: one shared variable per density
   generator, all three parity/early-birth types, fixed old scores, and the
   arrangement dimension `j+z`. See the [joint audit](proofs/joint_residual_audit.md).
2. Check that each size-stratified residual family precedes the focal masks.
   The actual selected residual and its counts may depend on the mask; the
   product containment probability is used only for each fixed family member.
3. Check both charges: witness penalty increases `K`, generator penalty
   contributes `mu*rho/kappa`. Verify `Kt`, `K*rho/kappa`, and the small-group
   term `t*gamma*kappa/K` throughout the final accounting.
4. Check the rigorous logarithm intervals in both tilt inequalities; the
   coarse `9/10` decay is used only in the final error estimate.
5. Review the inherited quadratic transaction potential, reverse containment,
   safety comparison, and lossless full-seed sample/value simulation.

The [rank-charge audit](proofs/rank_charged_audit.md) records a same-agent
second pass. Exact arithmetic and adversarial finite checks support the
argument, without establishing its universal assertions by enumeration.

A further improvement might tighten the retained joint basis/type count or
exploit relationships between generators, witnesses, and residual support.
Smaller parameter gains may remain; the numerical search is not globally
optimal. The abstract hazard bound `1/2` is sharp without additional structure.
Source comparisons and unavailable external announcements remain qualified in
[BASELINE.md](BASELINE.md). Do not infer new independent review or novelty
from a passing package build.
