# Executed approaches

The published `2^-36` derivation used these three linked attacks:

1. **Quadratic query potential.** Track the actual conditional failure
   probability `m` and the depleted failure probability `q`. The potential
   `q^2-2qm` has conditional increment `(q'-q)(q'+q-2m)>=0`. A completed
   failure has `m=q=1`. This gives `E[1_survive q^2]>=p(1-p)`, and the
   next-event containment and finite telescope imply expected exit hazard
   at least `1/2`. A repeated-OR family proves sharpness under the abstract
   hypotheses. Earlier logarithmic potentials were superseded.
2. **Integrated residual tail.** A family fixed before focal bits yields
   `Pr(e>x)<=min(1,N p_O^x)`. Integration gives
   `(log N+1)/log(1/p_O)`, uniformly down to the smallest analyzed group
   `n=kappa`. The selected residual is allowed to depend on the mask.
3. **Recalibrated masks and phases.** Recompute the filter expectation,
   safety probability, and density cost for changed mask rates. Use 64
   finite phases with rational mesh `69/64`, giving rounding factor
   `beta/5`. Combined with affine branch mixing, this yields the coefficient
   above `2^-36` with the same adversary and one-sample model.

The recorded exact parameter search examines 8,064 tuples with density
rate fixed at `5/8`; 3,234 have positive certificates. The chosen tuple
is best in that declared grid. This is not a global optimum. Floating-point
exploration guided discovery, but the published coefficient is certified
by exact fractions. [Search code](experiments/search_quadratic_parameters.py)
and [recorded output](experiments/quadratic_search_output.txt).

No independent agent review, external author consultation, or formal proof
build is claimed. The universal derivation and inherited structural lemmas
are in [the manuscript](manuscript.md).

## Joint-encoding follow-up

Executed three comparisons using the same analytic objective: parameter-only
retuning, a density-size cutoff with the old count, and the cutoff with joint
pivot encoding. The numerical search used 12 deterministic starts per mode
and a declared 275-tuple grid. It is not a global optimum or proof.
[Code](experiments/search_joint_residual.py),
[output](experiments/joint_residual_search_output.json).

The selected dyadic tuple has `kappa=640`, `rho=7/16`, `h=3/4`, `t=2^-15`,
256 phases, and analysis cutoff `33/64`. The exact certificate exceeds
`(21/20)*2^-34`. The written proof charges all basis choices, three generator
types, both affine tests, and the density exception without conditioning
away independence. [Detailed argument](proofs/joint_residual.md),
[same-agent audit](proofs/joint_residual_audit.md).

## Rank-charged entropy and the versioned paper

The [rank-charged record](results/rank-charged.md) executes two attacks: charge witness
entropy to nominal rank while retaining the density cutoff, then charge
generator entropy to expected density-sample size too. The latter removes
the cutoff and its exceptional-event term. The numerical search uses 16
starts per mode and a 15-tuple grid, without claiming a global optimum.
[Search](experiments/search_rank_charged.py), [output](experiments/rank_charged_search_output.json).

The exact dyadic construction uses `kappa=272`, `rho=13/32`, `h=3/4`, `t=2^-14`,
and 256 phases. Both analysis penalties are `39/2`, giving effective rank
coefficient `583/2`. Every changed later-cost factor and the small-group
term is carried through the final proof. The conservative certificate is
`1.0374747334 * 2^-32`; the proof is integrated into the shared framework and
selected record. [Same-agent audit](proofs/rank_charged_audit.md).

## Retained bases, additive accounting, and projection

Executed three cumulative attacks in the
[retained-basis argument](results/retained-bases.md):

1. Reconstruct old retained occurrences by greedy contraction. Canonical
   generators are forced in the first stream and witnesses in the second,
   reducing the basis/type factor from `48^j*4^z` to `6^j`.
2. Keep the integrated tail's `1/lambda` term additive per group. Sum its
   geometric weights and explicitly charge it to the maximum branch, instead
   of paying for it as a linear group-size error.
3. Project witnesses and residual tests onto `Y`, the fixed comparison
   optimum after filtering. This changes the family count to
   `binom(n,j)*binom(y,z)*6^j*S_(j+z)(2y)` and the entropy charge to
   `n*u+y*(w+2v)`. The optimum is only an analysis device.

The [search](experiments/search_retained_basis.py) used 16 deterministic
starts per cumulative mode. The recorded best multiples of `2^-32` were
about 1.05091 (prior formula), 1.30073 (retained bases), 1.71820 (additive
accounting), and 1.78594 (projection). These are numerical evidence, not
universal bounds or global optima. [Recorded output](experiments/retained_basis_search_output.json).

The exact dyadic tuple certifies approximately `1.77884758 * 2^-32`, using
`42n+27` initial fair bits. Both tilt inequalities have exact integer-power
cross-checks; the decay has a separate positive-series lower bound. A
coarse decay substituted into the first tilt fails, so the unrounded
log enclosure is essential there. The finite checks include reconstruction,
omitted second-stream generators, strict projection savings, adaptive mask
selection, and an additive-error negative control. The universal written
argument and [same-agent audit](proofs/retained_basis_audit.md) remain subject
to independent review.

## Activation splitting and joint membership

Executed three cumulative attacks in the
[selected argument](results/activation-split.md):

1. Condition safety on the deterministic activation flat after fixing the
   filter and density masks. Apply the half-exit lemma to labels outside it,
   obtaining `E sigma >= rho*y/4 - E j0/4`.
2. Treat activation generators as fixed old occurrences in both affine
   streams. Enumerate their label choices but remove their time variables.
   Active generators have only two types, and the fixed-role count becomes
   `4^j1*S_(j1+z)(2y)`. The activation penalty is `mu-1/4`, so adding `j0/4`
   to the residual comparison cancels the safety loss before applying the
   total generator budget.
3. Use the exact joint membership event for generators, witnesses, and
   residuals. Its probability is `rho^j*(1-p)^z*p^|R minus J|`. The overlap
   correction is essential. Enumerating disjoint roles per label gives
   `(1+u)^(n-y)*(1+u/p+w)^y*(1+v)^(2y)` as a tail prefactor.

The [numerical search](experiments/search_activation_split.py) uses seed
11133 and 24 starts per cumulative mode, with 256 phases. Recorded best
multiples of `2^-31` are about 0.892969 (preceding formula), 0.920310
(conditional safety), 1.000039 (activation splitting), and 1.027783 (joint
membership). [Output](experiments/activation_search_output.json). The tiny
floating-point crossing in the third mode is not a certified theorem.
No global optimum or ceiling is established by these searches.

The conservative exact certificate is `1.0225982999 * 2^-31`, with
`kappa=176`, `rho=3/8`, `h=3/4`, `t=11/2^17`, and 256 phases. All changed
costs, the additive tail term, and maximum-branch cancellation are retained.
The seed drops from `42n+27` to `40n+26` initial fair bits.

The initial adaptive-family test design did not exercise positive excess
adequately. It was revised before incorporation: 26 of 40 expectation
cases now have positive excess, and this coverage is asserted. The finite
checker also exercises all filter masks, omitted active generators,
generator/residual overlap, and unlisted outcomes. These are finite tests;
the universal proof and [same-agent audit](proofs/activation_split_audit.md)
remain subject to independent mathematical review.

## Three-state generator encoding and restricted overlap

The [selected proof](results/support-refinement.md) executes two linked
improvements and records one additional numerical candidate:

1. Exclude activation and wrong-parity generators from residual overlap.
   With the original four-state count, the best observed coefficient rises
   from `4.78598840606e-10` to `5.00591984396e-10`.
2. Absorb an omitted generator's parity into its signed first-stream score.
   It appears in no second-basis support, so three states suffice. Combining
   this compression with the valid overlap weights yields a best observed
   `5.11856741678e-10`; the conservative exact C5 is `5.10014502482e-10`,
   more than `(35/32)*2^-31` and 7.1044% above C4.
3. Numerically explore removal of forced pivot tests. Its best observed
   `5.11989869631e-10` is only about 0.026% above mode 2. This extension is
   excluded from the selected proof and certificate.

The [search](experiments/search_support_refinement.py) uses seed 11134,
24 starts per mode, and 256 phases. Its [output](experiments/support_search_output.json)
is numerical discovery evidence, not a global optimum or universal proof.

The finite checker covers both signs of omitted-generator variables. An
added rank-two binary example has an omitted valid-parity generator that
remains residual, rejecting a tempting stronger exclusion. Exact scalar,
mask-law, generating-product, and adaptive-tail checks accompany the
[same-agent audit](proofs/support_refinement_audit.md). Independent review
and formalization remain pending.
