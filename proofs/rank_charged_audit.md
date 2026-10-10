# Same-agent audit: rank-charged residual entropy

October 10, 2026. This is a second pass by the same agent, not independent
review or a formal proof. No remaining gap was identified in the pass below.

## Source and local dependencies

Re-read the source's marked-pivot and residual construction and the complete
rank-accounting section at OpenAI/math `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`.
The same-agent [joint-encoding audit](joint_residual_audit.md) and published
quadratic-potential proof remain dependencies. The new result does not
reclassify them as independently validated premises.

The [new derivation](../results/rank-charged.md) was recalculated as follows.

| Obligation | Assessment |
|---|---|
| Joint family for unequal counts | The earlier fixed-`J,Z` proof uses only the two sizes, not the later equal-cutoff restriction. Its factors are `3^j 4^(2j+z)` and arrangement dimension `j+z`, giving `48^j 4^z` after simplification. |
| Witness union size equals rank | Source bases `Z_b` are disjoint because their birth sets are disjoint. Their total size is the nominal rank statistic `z`. |
| Generator size | The source generator lemma provides one set for the whole nominal path with `kappa*j<=|D intersect U|`; it is not a separate set for every layer. A fixed choice rule suffices on the finite mask space. |
| Fixed before focal masks | Each size-class family is constructed from fixed old streams, all subsets of the specified sizes, and all permitted affine patterns. It precedes the focal masks and listing. |
| Full range of counts | Both counts can be summed from 0 through `n`; invalid choices only overcount. The binomial bound holds even when `j+z>=2n`, without division by a count or hidden floor. |
| Weighted union bound | For each fixed family member, its containment probability is exactly `p_O^|R|`. Counts attached to the actual selected residual may depend on the mask; the union is over fixed labelled families. No independence of that selection is used. |
| No generator probability shortcut | The proof does not multiply `Pr(R subset O)` by `Pr(J subset D)`. Overlap could invalidate that shortcut. Generator size is charged pointwise, then averaged linearly. |
| Excess residual | Clipping at zero gives `R<=mu*j+nu*z+e` on every outcome. The unlisted case has `sigma=z=e=0` and needs no containing residual family. |
| Integrated tail | The majorant is `min(1,exp(nD-lambda*x))`; its integral is `(nD+1)/lambda`. Absorbing the last term uses only `n>=kappa`. |
| Both deterministic charges | The witness penalty increases the rank coefficient to `K=kappa+nu`. The generator penalty contributes `mu*rho/kappa` to the expected error. Dropping either term is incorrect, as the negative controls demonstrate. |
| Later path cost | The source still contributes `t*n+(t+rho/kappa)*sum_later n`. Multiplying by `K` inside the group inequality changes both terms; the denominator substitution alone would be wrong. |
| Small groups and maximum branch | The cutoff for analyzed group size remains `kappa`, not `K`. Thus the affine loss is `t*gamma*kappa/K` times the maximum. The branch cancellation inequality holds with this factor. |
| Rounding and adversary | The same rational phases apply after an order-uniform fixed-phase guarantee. The minimum over all orders stays inside the seed expectation, including the branch and every unused bit. |
| Logarithm enclosures | The helper uses 24 atanh terms, a geometric upper tail, and dyadic range reduction. The two tilt inequalities use the unrounded interval for lambda. `9/10` alone does not certify the witness inequality and is used only in the final error bound. |
| Scalar recalculation | Direct substitution gives `K=583/2`, `D=133/40960`, error `7847/208896`, slack `1019519/174219264`, and `C_2=773895463001/3203794364409053184000`. The exact ratio over the PR coefficient is about 3.93235, not four. |
| Resources and model | The new penalties and tilts are analysis devices. The rule uses `36n+23` dyadic fair bits; exact observations and possibly exponential rank/closure storage remain part of the model. |

The new finite checks cover the weighted generating inequality, adaptive
selection of overlapping residuals after the entire mask is revealed, and
45,824 actual small-matroid path charges. The path check uses small stress
penalties and threshold 2 to obtain nonzero residual, generator, and witness
cases. Its abstract scalar negative controls are not hard matroid instances.
The exact final constants are checked separately, with rational arithmetic.

The first numerical comparison retained the density cutoff while charging
witness rank; it improved the bound but was superseded by charging generator
counts too. Neither coordinate search is globally optimal. Ordinary
exponential weighting and union bounds are not claimed as new mathematical
principles; their application and final-theorem implication are the proposed
refinement.

Independent review should start with the size-stratified family count and
the weighted containment bound, then the source-to-final accounting. The
joint affine lemma and quadratic hazard proof also need independent review.
