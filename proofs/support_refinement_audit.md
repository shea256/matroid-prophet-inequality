# Same-agent audit of three-state encoding

October 11, 2026. This is a second pass by the same agent, **not independent
mathematical review**. No remaining gap was identified in this pass.

## Basis and variable audit

- The first stream retains every active generator. Once its labels and the
  fixed activation occurrences are specified, retained-old reconstruction
  fixes its basis independently of generator times and marks.
- In the second stream, the retained set is exactly the activation old
  occurrences, all witnesses, and a chosen subset T of active generators,
  together with its reconstructed old complement. T is encoded by the three
  states, so charging another subset factor would double-count it.
- An omitted active generator has no occurrence in the second retained
  basis, and hence no term in any second support sum. Its first signed score
  can be a single unrestricted variable. No relation to its unused second
  score is needed. An actual stream supplies a legal assignment of these
  variables; allowing unrealizable assignments only enlarges the family.
- For retained active generators the two types remain distinguished. Their
  second score includes the required shift factor for the wrong parity.
  The other fixed coefficients are exactly those of the existing joint
  representation. All support sums are affine in j1+z variables.
- Restrictions of variable domains and fixed residual exclusions can only
  reduce the number of patterns. The general arrangement bound still covers
  d=0, y=0, coincident forms, and dimensions larger than 2y.

## Overlap and conditioning audit

- Activation and retained wrong-parity generators have negative first pivots.
  Retained valid-parity generators have positive pivots in both streams.
  Witnesses have negative second pivots. Only valid retained and omitted
  active states can overlap R.
- Omitting a generator does not force its label out of R. The explicit
  binary rank-two example in the proof realizes exactly this obstruction.
  The first inherited finite suite covered only negative omitted scores;
  the added example also exercises a positive omitted score and residual
  overlap. The correction for omitted generators remains in the certificate.
- The joint probability is evaluated for fixed role sets and fixed R before
  focal bits, retaining the factor for `R intersect J`. The actual adaptive
  choice is handled by a union bound over the fixed families.
- For labels outside Y there are three active choices of equal weight B.
  For labels inside Y one choice has weight B and two have weight B/p.
  Activation has weight A in both cases. Witnesses are available only in Y.
  This yields the generating product stated in the proof. The rational
  relaxation uses only A+3B<=u, B<=u/3, W<=w, and p>=rho.
- Neither listing nor a favorable event is conditioned on. Unlisted groups
  contribute zero. The tail is integrated with its additive 1/lambda term.

## Final-theorem audit

- The activation quarter charge cancels before using the generator budget.
  The projected witness rank is no larger than the full rank and uses no
  focal test bits. The existing thinning argument applies unchanged.
- The full rank coefficient K=kappa+nu appears in both later cost terms,
  Kt and K*rho/kappa, and in the final denominator.
- The maximum-branch condition pays the additive and small-group losses.
  Both beta factors and the finite rounding denominator remain present.
- All new probabilities are dyadic. They use 47N+27 initial fair bits; this
  is an increase from 40N+26, not a seed improvement. Exact observations and
  potentially exponential preprocessing/storage remain allowed.
- The seedwise order minimum and lossless one-sample simulation are inherited
  explicitly. No fixed-order or seed-oblivious theorem is substituted.

## Actual checks and limits

The exact verifier passes separate rational-power tilt inequalities,
outward logarithm intervals, a positive-series decay check, final accounting,
seed counting, and recalculation of C4. The finite verifier passes 70,297
path pairs, 504,552 compressed support signs, 4,760 mask probabilities,
30 generating bounds, 112 adaptive tails, and 32 adaptive expectations.
It includes 2,716 inherited conditional safety bounds and the added
omitted-but-residual negative control. The [receipt](../verification/current_run_receipt.json)
records actual commands, outputs, runtime, and environment.

These checks do not prove the universal theorem, validate source Lean
compilation, establish optimality, or replace independent review. The
optional forced-pivot numerical mode is excluded from the selected proof.

Next decisive review: inspect the signed-variable elimination in the three-state encoding section
and the per-state overlap weights in the joint mask law section of the
[proof](../results/support-refinement.md), then audit the inherited C4 dependencies.
