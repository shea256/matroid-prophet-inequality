# Second-pass audit of the `2^-63` derivation

Date: October 10, 2026. **Same-agent mathematical audit, not independent review
or formal verification.** No gap was identified in this pass. The record remains
`Candidate result`; scalar and finite verification cannot settle the universal
conditioning arguments. The [research note](../manuscript/note.tex) contains
the expanded derivation and full definitions.

## Dependency interfaces checked against the pinned source

Source: OpenAI/math commit `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`;
see the immutable links and hashes in [BASELINE.md](../BASELINE.md) and
[source_manifest.json](../verification/source_manifest.json).

| Interface | Source TeX label | Hypotheses needed for this use | Audit conclusion |
|---|---|---|---|
| Candidate mass | `algorithm.tex`, `lem:filter` | Deterministic rounded vector, fair independent `H`, fixed priority ties | Independent of `B,kappa,t`; applies separately at every phase |
| Largest density maximizer and residual density | `algorithm.tex`, `lem:density` | Finite matroid and `kappa>0` | Supermodularity, monotonicity, and objective comparison use no large constant |
| Path nesting and excluded births | `algorithm.tex`, `lem:paths` | Enabled maps at `a_h=-3h`, same recursion | Valid for the retuned maps; no birth at `a_h+1` |
| Generators for the entire path | `algorithm.tex`, `lem:generators` | Monotone incoming path; positive rank charge | Telescoping objective increments give `|J_h|<=|D_h|/kappa` without slack |
| Exit-hazard estimate | `safety.tex`, `lem:transactions`, `eq:dyadic-exit` | Finite predictable queries, disjoint queried coordinates, product guard law | The cutoff can be left symbolic; replacing 12 by 4 yields the stated `13/20` bound |
| Hybrid safety | `safety.tex`, `eq:hybrid-bits`, `eq:hybrid-containment` | Same guard/test rate; no test bits in the ordinary transcript; enabled focal map | These hypotheses persist. The product law is conditional on the **complete** ordinary transcript; independence is endpointwise only |
| Residual encoding | `transfer.tex`, `lem:pivot-patterns`, `lem:pattern-family`, `eq:raw-pattern-count` | Fixed `H`, parity, exterior bits; `n>=kappa`; `z<=n/kappa` | Generator and witness subsets have size `q=floor(n/kappa)`. No focal bits or listing event condition the family |
| Residual entropy | `transfer.tex`, proof after `eq:raw-pattern-count` | `kappa>=4` for the two binomial bounds | The unrelaxed expression `(6 log kappa+6+4 log 2)n/kappa` is already in the source proof |
| Every-order rank comparison | `accounting.tex`, `lem:all-orders` | All coins fixed; greedy layer selection | Deterministic for every order; minimization remains before expectation |
| Later-path cost | `accounting.tex`, `lem:rank-cost`, `eq:rank-telescope-step` | One common generator set and nested parity endpoints | The common set is charged once; rank inequalities do not require it to be independent of masks |
| Test thinning | `accounting.tex`, `lem:thinning` | Condition on `H,D,C`, parity, all exterior `T` bits | Focal `T` stays independent. The arrival order is excluded from this conditioning |
| Expected density cost | `accounting.tex`, paragraph after `eq:expected-cost` | Bound by counts on all true groups before averaging | The source explicitly identifies the exact contribution `1/(4kappa)` used here |
| Gluing | `setup.tex`, `lem:simulation` | All sample/value coordinates independent with paired laws; seed-independent coordinates | Seed-selected mask is allowed, including phase and rare branch. Unused coordinates may still influence the adversary |

## Conditioning ledger

1. Fix the hidden vector before any randomness. Condition on the common phase
   to apply the rounded-vector argument; no other coin is affected.
2. Candidate groups and `Y` are fixed by `H`. The listing mask is not exposed
   when averaging true-group costs.
3. For reverse safety fix `H,D`. Only adaptively queried `C` bits enter the
   reverse transcript. Parity and `T` do not. Never recompute past states after
   deleting earlier positives in the certificate comparison.
4. For the residual union bound fix `H`, parity, and exterior `D,C,T`. The
   focal group's possible listed index and lower-group paths are already fixed.
   Its own bits and its listing event are not fixed. A deterministic family is
   union-bounded before the actual residual is selected.
5. For focal thinning fix `H,D,C`, parity, and exterior `T`. All bases and
   witness ranks are measurable under that conditioning. Do not fix a chosen
   order, which could reveal the focal test mask.
6. Minimize over permutations at each complete seed. Then average the branch
   and phase. This order of operations allows their values to be public.
7. In the prophet reduction condition on the **whole** seed to establish the
   glued product law. Only afterwards integrate the fixed-vector inequality.

## Explicit definitions added to the research note

The original short proof referred to source statistics without restating all
of them. The note now defines `K_(h,b)`, valid parity endpoints, nominal birth
sets `P_(h,b)`, unsacrificed sets `S_(h,b)`, safe counts `sigma_h`, nominal rank
`z_h`, basis witnesses `Z_b`, residuals, final tested ranks `lambda_h`, and the
single later-path cost `c_h`. It also specifies empty thresholds, the no-listed-
group branch, priority ties, and the exact allowed information in preparation.
These additions make the candidate reviewable without guessing notation.

## Boundary checks in the derivation

- `n=kappa`: the residual union bound is already at most `2^-18`; it does not
  rely on an asymptotically large group or rounding away the floor in `q`.
- Unlisted groups: all focal statistics are zero; the sample count is also
  zero, so averaging safe counts never conditions on a selected group.
- Large nominal rank: if `z>n/kappa`, `sigma<=n<kappa z`; no residual-family
  assertion is needed there.
- Baseline birth: subtract `|D_h|/kappa` **before** parity, leaving the stronger
  `|D_h|/(2kappa)` loss afterwards and `n/(8kappa)` after the `D` average.
- Negative main affine bound: adding the maximum branch still cancels its
  largest-coordinate term. No case split or positivity per vector is needed.
- Phase boundaries: all sixteen rounded exponents appear exactly once,
  including for negative exponents and exact powers of two.
- Loops and integrability: loops cannot enter `U` or the accepted set. Only
  the optimum, not every coordinate separately, needs a finite expectation.
- Resource model: the finite seed is counted in bits. The matroid-table
  implementation and exact-real observations are not treated as efficient
  finite-precision computation.

## New executable evidence

[check_online_rule.py](../verification/check_online_rule.py) constructs paths
using only revealed weights and supplies unsacrificed weights only on arrival.
It covers all labeled matroids on up to three elements with the weight cases
defined in the script, plus targeted four-element uniform, partition, and
triangle-with-loop examples. It enumerates relevant `D,C,T` masks conditional
on every `H`; irrelevant bits are marginalized exactly. It takes the minimum
over every arrival permutation separately for each seed before averaging.

The guard and test rate is `1/4` to exercise the parameter-uniform statements.
Density thresholds are `2` and, for six small cases, the proposed `2^18`.
The smaller threshold is necessary to exercise nontrivial density on these
small ground sets. This is not a test of the universal `2^-63` guarantee and
does not use large instances with the proposed `t=2^-29`.

The executed output records 221 instances, 19,200 prepared rules, 287,976 seed
states, 5,347,942 complete order runs, and 7,736,592 order-uniform inequalities.
It exercises 3,160 nontrivial density states and 12,491 nontrivial guard states;
3,232 conditional safety inequalities pass with exact rational averaging.
Prefix independence, generator budgets, and the telescoping rank-cost inequality
also pass. See [online_output.json](../verification/online_output.json).

## Remaining decisive work

Independent review should concentrate on the hybrid coupling and the residual
encoding, then verify that the dependency chain proves the exact theorem
quantifiers. Formalizing only the final arithmetic would not resolve these
points. The stronger external `2^-47` proof is needed for the novelty comparison.
No external review, formalization, public release, or author contact was done
by this agent.
