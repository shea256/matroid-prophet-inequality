# Same-agent second pass: retained bases and projected residuals

October 10, 2026. This is a second pass by the same agent, not independent
mathematical review or formalization. No remaining gap was identified in
the [written derivation](../results/retained-bases.md) in this pass.

| Obligation | Assessment |
|---|---|
| Old basis reconstruction | Rejected old occurrences are spanned by preceding retained old occurrences and a subset of final retained movable occurrences. Accepted ones remain independent with the entire final movable set. These two facts give the contraction scan by induction, including repeated labels and loops. |
| Forced first generators | The source constructs each batch as an independent extension over the actual first-stream prefix. The proof specifies that canonical construction, rather than an arbitrary set satisfying only the generator-size bound. |
| Forced second witnesses | Each chosen witness batch is an independent extension of the preceding endpoint plus competition set; same-mark reorderings of later generators do not alter this base. |
| Second generators not forced | The new finite paths include 168 omitted second-stream generators. The proof retains the `2^j` choice factor and does not incorrectly replace it by one. |
| Joint affine representation | The retained bases are now fewer, but generator types, score shifts, old paths, and `j+z'` common variables are unchanged. All three types remain, including early invalid insertions of the chosen parity. |
| Projected witnesses | Choose a basis only of `(P_b intersect Y) minus O`; its union is inside fixed `Y`. Its total rank `z'` is at most the full nominal `z`. The online rule still uses the full candidate groups. |
| Projected residual comparison | All counted safe samples are in `Y`. A safe sample outside the new residual is charged by the same density inequality to projected witness rank. The projected residual, not the old full residual, is contained in `O` by the new spanning property. |
| No access to optimum | `I*`, `Y`, `Z'`, and the new residual are analysis objects. The rule does not acquire hindsight information or a second sample. |
| Conditioning | `H`, the rounded fixed vector, parity, and outside masks fix `U`, `Y`, incoming paths, and competition sets before focal bits. The safety expectation is averaged over parity; the tail bound holds separately at each parity. No listing event or chosen order is conditioned upon. |
| Size factors | Generator choices use `binom(n,j)`; projected witnesses use `binom(y,z')`; only `2y` affine forms are tested. The family bound includes zero sizes and arrangement dimension larger than `2y`. |
| Adaptive selection | The actual residual can depend on the entire mask. The union is over a fixed family; containment of each fixed member has probability `p^|R|`. There is no multiplication by a potentially overlapping generator event. |
| Weighted tail | Its entropy is `n u + y(w+2v)`. Integration contributes `1/lambda`; the new argument preserves and pays for that constant. |
| Both rank charges | Witness penalty changes the denominator to `K=kappa+nu`; generator penalty contributes `mu*rho/kappa`. Subsequent costs contain both `Kt` and `K*rho/kappa`. |
| Full rank and thinning | Source thinning lower-bounds the full `z`; substituting `z>=z'` is valid, and projected witnesses use no focal test bits. No new thinning lemma is presumed. |
| Maximum-branch cancellation | Geometric summation charges the additive constant to the maximum weight. The correct loss is `t*(bar_gamma*kappa+a0)/K`, and the new cancellation inequality includes `a0`. |
| Rounding and order quantifier | The same finite phases are used; minimum over permutations remains inside every seed expectation. Source glued-vector simulation still includes all sample/value/seed information available to the adversary. |
| Exact arithmetic | Interval logarithms and separate integer-power comparisons both verify the tilt inequalities. A separate direct positive atanh sum verifies the decay lower bound. `49/50` alone fails the first tilt comparison, so that shortcut is explicitly rejected. |
| Baseline comparison | Direct rational reconstruction gives the exact previous `C_2`; the new `C_3/C_2` is about 1.71459. The certificate explicitly checks `C_3<2^-31`. |
| Resources | Dyadic probabilities require `42N+27` fair bits, up from `36N+23`. Exact observation/index precision and potentially exponential preprocessing/storage remain unchanged. |

The finite checks enumerate all 92 labeled matroids through four elements
for the abstract interleaving lemma, with up to two movable occurrences
and forward/reverse old orders. Actual projected-stream checks cover
170 small matroid/weight instances and 45,824 paths at stress threshold 2
and empty filter mask,
with nonzero rank, generator, residual, and strict-projection cases.
They also check adaptive containment tails and geometric-weight boundaries.
They do not prove any assertion for arbitrary matroids.

No proof from the unavailable external `2^-47` announcement was used.
The OpenAI source commit is unchanged; recent searches found no accessed
replacement in the same model. Those searches are not exhaustive.

Independent review should begin with the forced-retention application and
the projected density comparison, then check the additive cancellation
in the weighted-entropy and parameter sections. The inherited quadratic hazard and affine encoding
arguments also remain review obligations.
