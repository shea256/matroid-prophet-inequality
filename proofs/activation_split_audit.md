# Same-agent audit: activation splitting and joint membership

October 10, 2026. This is a second pass by the same agent, not independent
mathematical review or formalization. No remaining gap was identified in
the [written derivation](../results/activation-split.md) in this pass.

| Obligation | Assessment |
|---|---|
| Strongest accessible comparison | Reproduced C3 from its scalar verifier. PR #5 is merged; the new result is compared with the exact C3, not merely its rounded power-of-two headline. The source refresh remains a scoped search, not a priority claim. |
| Deterministic excluded births | With H,D and weights fixed, Q(L) is fixed before guards/tests. Nonbaseline labels have no possible birth at a or a+1. The half-exit result is applied to those fixed labels individually, before summing or parity averaging. |
| Safety improvement | Independent parity gives one quarter times the nonbaseline sampled comparison count. The discarded independent count is at most rank Q(L), exactly j0 in the canonical initial extension. It is not assumed that baseline births themselves become safe. |
| Activation location | All initial generators are inserted at a; X(a)=X(a+1) forbids a generator at a+1. Their second-stream endpoint is fixed at a or a+1 according to parity, with empty competitors/witnesses and incoming loop flat. |
| Fixed scores | Initial generators become fixed old occurrences in both affine streams. Their label choices remain charged. Active generators retain variable insertion times; their variables are not removed. |
| Forced retention | All initial generators are retained in both streams. All active generators are retained in the first; all witnesses in the second. Active second generators may be omitted, so their 2^j1 factor remains. |
| Two active types | Active times are at least a+2. Same-parity times are valid, leaving only (1,1) and (-1,2^T). Initial-time negative same-parity scores are fixed constants, not a third active type. |
| Dimension and degeneracies | The first test uses j1 variables, the second j1+z, and together they use j1+z. Fixed activation scores can enter affine constants. Zero sizes and dimensions above 2y obey the same binomial arrangement bound. |
| Role disjointness | J0 and J1 are disjoint subsets of D. Projected Z is a subset of Y outside D union C, so it is disjoint from both. Each enumerated role assignment is fixed before focal mask bits. |
| Overlap probability | R may overlap J. The exact law is rho^j (1-p)^z p^|R\J|, not rho^j (1-p)^z p^|R|. The upper bound includes p^(-|J intersect Y|). A singleton negative control rejects naive multiplication. |
| Per-label generating product | Outside Y there are three exclusive roles; inside Y there are four, adding the witness role. The generator roles inside Y have the 1/p correction. Their exact sum yields (1+u)^(n-y)(1+u/p+w)^y, with the separate (1+v)^(2y) arrangement factor. |
| Adaptive selection | The union bound is over fixed sets, roles, and affine families. No independence is claimed for the actual selected generators, witnesses, or residual. Unlisted outcomes have zero excess, so they cannot enter a positive-excess tail event. |
| Quarter-charge cancellation | The tail penalty of an activation generator is mu-1/4. Adding j0/4 to the pointwise rank comparison cancels the negative E j0/4 in safety before replacing total generators by |D|/kappa. Dropping this term prematurely would be invalid. |
| Projected/full rank | The previous projected residual comparison and z_projected <= z_full are unchanged. Focal test bits are absent from both statistics, so the source thinning calculation applies to full nominal rank. |
| Final costs | The proof keeps Kt, K*rho/kappa, the additive 1/d, small groups, geometric sums, and maximum-branch cancellation. No gain is claimed from merely removing the integrated tail's additive constant. |
| Exact tilts | The bound p^(-1/4)<4/3 is certified by a fourth-power inequality. Both tilt conditions have outward-log and separate integer-power checks. A direct positive atanh sum cross-checks the decay. |
| Quantifiers | Every rank comparison remains order-uniform with the seed fixed. Minimum over permutations stays inside seed expectations, including phase/branch. The original lossless sample/value simulation is retained. |
| Resources | 40N+26 initial fair bits, down from 42N+27. No additional sample or access to the optimum is used. Exact observations, unbounded level-index precision, and possibly exponential preprocessing/storage remain explicit. |

Finite tests cover all filter masks on 170 inherited small matroid/weight
instances at stress threshold 2 and guard/test rate 1/4. They check the
fixed-activation affine representation, conditional safety, and positive
charged residuals. Separate arbitrary-family tests use the stress and final
mask rates, allow generator/residual overlaps, and let the selector see the
whole mask. Positive-excess tests are required to avoid vacuous tail checks.
These enumerations do not prove the universal assertions.

The decisive external review should begin with the conditioning in the
activation safety estimate, then the fixed-time affine count and overlap
correction in the joint mask law. The quarter-charge cancellation and full
payoff substitution should be checked after those. Review of the inherited
quadratic hazard and joint encoding is still required; this pass does not
establish those independently.
