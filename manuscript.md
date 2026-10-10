# A quadratic hazard potential and a guarantee above `2^-36`

**Ryan Shea**

October 10, 2026.

**Written proof with same-agent verification; independent review and
formalization pending.**
The three changes are a quadratic exit argument, an integrated residual bound, and recalibrated
mask probabilities and finite rounding phases. The announced `2^-47` proof
remains unavailable, so the coefficient comparison is not a priority claim
or a comparison with that proof's strongest possible coefficient.

## 1. Statement, construction, and dependencies

For every known finite labeled matroid on `n` elements, the construction below
is a measurable, distribution-independent, one-sample rule using `38n+23`
initial independent fair bits. For mutually independent nonnegative sample
and value coordinates, with matching laws at each label and an independent
seed, assume only that the expected offline optimum is finite. For every
measurable arrival permutation depending on all samples, values, and the
entire seed, the accepted set is independent at every prefix and

```math
 \mathbb E[\mathrm{reward}]\ge C_0\mathbb E[\mathrm{OPT}],\qquad
 C_0=\frac{9652683394380719}{637507023635152349901619200}
 >2^{-36}.
```

The exact construction has a slightly larger coefficient; `C_0` uses a
simple rational lower bound on its geometric base. Approximately,
`C_0 = 1.0405020 * 2^-36 = 2130.9482 * 2^-47`.

Use the source's candidate filter, density maps, guarded paths, parity
layers, and online greedy rule, specified below. Choose the parameters

```math
 \kappa=2048,\quad t=2^{-16},\quad
 \Pr(H_e)=h=3/4,\quad \Pr(D_e)=\rho=5/8,\quad
 \Pr(C_e)=\Pr(T_e)=t.
```

The maximum branch retains its separate fair mask. Choose the main branch
with probability `p_main=1-t`. For rounding use

```math
 \theta=69/64,\quad L=64,\quad B=\theta^L,
 \quad J\sim\operatorname{Unif}\{0,\ldots,L-1\},
 \quad u_J(x)=\theta^J B^{\lfloor\log_B(x/\theta^J)\rfloor},
 \quad u_J(0)=0.
```

All these random choices are independent and occur in the initial seed.
`B` is rational; integer-valued `B` is unnecessary for the source's
geometric-sum arguments. For a fixed phase its scale `theta^J` factors out.

The primary dependency is OpenAI/math commit
`fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`, checked on October 10, 2026.
Immutable source links are in [BASELINE.md](BASELINE.md), with hashes in
[the source manifest](verification/source_manifest.json). We retain its
density/generator lemmas, path nesting and prefix feasibility, hybrid safety
comparison, marked-pivot theorem, residual encoding, rank accounting, and
lossless one-sample simulation. Their interfaces are made explicit below.
The sharper residual count is derived in Section 4. The new quadratic exit
proof replaces the source's hazard-band calculation. Attribution and the
scope of the claimed contribution are in [ATTRIBUTION.md](ATTRIBUTION.md).

### 1.1. The fixed-vector rule and analysis quantities

Fix a nonnegative vector `w` before drawing any seed bits. A hidden-vector
rule reveals and sacrifices a seed-chosen set of labels, then handles every
arrival permutation. Its target is the expected minimum reward over all
orders. Let `r(A | P)=r(A union P)-r(P)` and `F_empty=cl(empty)`; fix a total
label order for every tie. Rounded priority compares weight first, then
that label order. Let `W=OPT(u)` and let `I*` be rounded priority greedy on
all labels.

The phase, branch, masks, and parity have the probabilities in the theorem's
construction. In the maximum branch, reveal an independent fair mask and
accept the first unmasked positive nonloop with priority exceeding every
revealed positive nonloop. An empty revealed threshold is below every
positive nonloop. This branch has expected worst-order rounded reward at
least `m*/4`, where `m*` is the largest rounded nonloop weight: the largest
priority is unmasked and the second is masked with probability `1/4`.
With just one positive nonloop the success probability is `1/2`; with none
the claimed lower bound is zero.

In the main branch, reveal and sacrifice `H union D union C`. Define

```math
 U=\{e\notin H:u_e>0,\ e\notin\operatorname{cl}(H_{>e})\},
 \qquad Y=I^*\setminus H.
```

The candidate test uses only revealed `H` values and the arriving value.
For a fixed phase, divide weights by its common scale `theta^J`, so true
groups `U_i` have weight `B^i`. List those intersecting `D`, in increasing
weight order, as `G_1,...,G_m`. Set `D_j=D intersect G_j` and likewise for
`C_j,T_j`. The full groups are analysis objects; their revealed `D_j,C_j`
parts suffice to prepare the rule. If there are no listed groups, reject all.

For a flat `P`, let `Q_j(P)` be the largest flat `Z` containing `P` that
maximizes `|D_j intersect Z|-kappa r(Z)`. For nonflat arguments first take
closure. Put `a_j=-3j`; let `Q_(j,k)=Q_j` for `k>=a_j`, and the identity
earlier. With `F_0(k)=F_empty` for `k<0` and `F_0(k)=E` otherwise, define

```math
 X_j(k)=Q_{j,k}(F_{j-1}(k)),\qquad
 F_j(k)=\operatorname{cl}\bigl(X_j(k)\cup(C_j\cap X_j(k+1))\bigr).
```

Prepare these paths in increasing `j` on the finite relevant auxiliary
timeline, and put `Fhat=F_m`. For an arriving nonloop in listed group `j`,
its nominal birth is `b_j(e)=min{k:e in X_j(k)}`. It is eligible exactly
when it is unsacrificed, passes the candidate test, is in `T`, has birth
`b>=a_j+2` of the chosen parity, and lies outside `Fhat(b-2)`. At each
endpoint `b` maintain the set `A_b` of accepted elements in that layer;
accept an eligible `e` exactly when `r({e} | Fhat(b-2) union A_b)=1`.

The source's density and path lemmas give

```math
 F_{j-1}(k)\subseteq X_j(k)\subseteq F_j(k)\subseteq X_j(k+1),
 \qquad
 |D_j\cap(\operatorname{cl}(Q_j(P)\cup Z)\setminus Q_j(P))|
 \le\kappa r(Z\mid Q_j(P)).
```

Nonloops are born at `a_j` or in `[a_j+2,0]`; no birth at `a_j+1` is
possible. The entire nominal path uses a generator set `J_j` of size at
most `|D_j|/kappa`. These facts hold for the positive threshold used here.
Nested layer bases imply independence at every arrival prefix. Finite rank
operations, fixed tie rules, and countably many rounding levels imply
measurability. The original paper proves these structural facts; this
paper changes the probability and quantitative analysis.

For clarity, the statistics used below are as follows. For valid endpoints
`a_j+2<=b<=0` of the selected parity, set

```math
 \begin{aligned}
 K_{j,b}&=\bigcup_{\ell<j}T_\ell\cap(X_\ell(b)\setminus X_\ell(b-1)),\\
 P_{j,b}&=G_j\cap(X_j(b)\setminus X_j(b-1)),\quad
 O=D\cup C,\quad S_{j,b}=P_{j,b}\setminus O,\\
 z_j&=\sum_b r(S_{j,b}\mid X_j(b-2)\cup K_{j,b}),\\
 \lambda_j&=\sum_b r(T_j\cap S_{j,b}\mid\widehat F(b-2)\cup K_{j,b}).
 \end{aligned}
```

The safe count `sigma_j` counts `d in D_j intersect Y` with such a birth
and `d notin Q_j(F_(j-1)(b-2) union K_(j,b))`. Choose a fixed-order basis
extension `Z_b` of each nominal rank summand; then `sum_b |Z_b|=z_j`.
The residual is

```math
 \mathcal R_j=\bigcup_b\bigl(P_{j,b}\setminus
 \operatorname{cl}(X_j(b-2)\cup K_{j,b}\cup Z_b)\bigr)\subseteq O.
```

For true groups that are unlisted, extend `sigma_i,z_i,lambda_i` by zero.
The original density argument gives `sigma_j<=kappa z_j+|R_j|`. Its
order-uniform lemma says the number of accepted labels of weight at least
that of `G_j` is at least `lambda_j`, for every complete seed and order.
The later-path rank cost is bounded once over the whole timeline by

```math
 c_j=|C_j|+\sum_{\ell>j}(|C_\ell|+|D_\ell|/\kappa).
```

Conditional on `H,D,C`, parity, and test bits outside the focal group,
independent focal thinning gives `E lambda_j >= t(z_j-c_j)`.
These are the source interfaces used in the final accounting, with their
probabilities retained rather than rounded to the source's numerical bounds.

## 2. A quadratic resource for one transaction

Fix an increasing event `A` on finitely many independent bits, and a
predictable query procedure which reads each bit at most once and determines
whether `A` holds. Let `p=Pr(A^c)`. At an intermediate query transcript write
`W` for the remaining coordinates and `I` for its queried positive answers.
Define

```math
 m=\Pr(A^c\mid\text{transcript}),\qquad
 q=\Pr(A^c\text{ with only }W\text{ random and all other bits zero}).
```

The unqueried product law is preserved by predictable queries. Equivalently,
`m` is the failure probability with `I` forced positive, all queried negatives
zero, and `W` random. Increasingness gives `0<=m<=q<=1`. Initially `m=q=p`.

If the next queried coordinate is `e`, the next depleted probability
`q'=f(W\{e})` is determined **before its answer** and satisfies `q'>=q`.
The actual conditional failure probability `m'` is a martingale:
`E[m' | transcript]=m`. For

```math
 \Phi(q,m)=q^2-2qm
```

we therefore have the exact identity

```math
 \mathbb E[\Phi(q',m')\mid\text{transcript}]-\Phi(q,m)
 =(q'-q)(q'+q-2m)\ge0. \tag{Q}
```

At the completed transaction, `m=1_{A^c}`. Failure implies `q=1`, because
`m<=q<=1`. Survival implies `m=0`. Since there are at most the original
number of coordinates to query, sum (Q) over a finite, zero-padded sequence.
The initial potential is `-p^2`; the final expectation is
`E[1_A q^2]-p`. Thus

```math
 \boxed{\mathbb E[\mathbf1_A q^2]\ge p(1-p).} \tag{R}
```

This includes `p=0` and `p=1` without division, logarithms, limiting arguments,
or a positive-hazard assumption. It also applies when no query is needed.
The essential facts are the actual conditional-probability martingale,
the predictability of `q'`, increasingness, and a transcript deciding `A`.

## 3. From one transaction to expected exit hazard

Condition on `H,D` and a listed-group prefix as in the source reverse
computation. Fix a nonloop `d` still alive just before a step. Its fresh
domain is the union of the group restrictions to the current states `S`.
Let `A` be the increasing event that `d` survives the reverse transition
`G_k(c,S)`, and let `p` be its conditional failure probability.

For completeness, the reverse map on a fixed listed-group prefix is
```math
 A_0=F_{\varnothing},\qquad N_j=Q_{j,k}(A_{j-1}),\qquad
 A_j=\operatorname{cl}\bigl(N_j\cup\{e\in G_j\cap S_j:c_e=1\}\bigr),
```
where `F_empty=cl(empty)`, `k<0`, and the output is the vector `(N_j)_j`.
Starting from `X_j(0)=E`, compute `X(k)=G_k(C,X(k+1))` in decreasing time.
For an actual later state, `N_j` is contained in `S_j` for every fresh bit
assignment. Query only `G_j intersect (S_j minus N_j)` after computing `N_j`;
unqueried additions are already spanned. The remaining domain is
`union_j (G_j intersect N_j)`.

The source queries exactly the departing coordinates, in predictable
group batches. These answers determine every output state: omitted bits
lie inside an already spanned flat and cannot change it. In particular,
the completed transcript decides `A`. This verifies the hypotheses of (R),
including failure transcripts, not just positive survival certificates.

Write `S'` for the actual output and `V'` for the remaining coordinates.
For every assignment `c` supported on `V'`, monotonicity gives

```math
 G_{k-1}(c,S')\subseteq G_k(c,S).
```

On the right every just-queried coordinate is zero, which is exactly the
depleted experiment defining `q`. Conditional on the complete post-step
transcript, the bits in `V'` still have their independent product law.
On survival, the next conditional exit probability `r` therefore satisfies
`r>=q`. Both states are frozen for this comparison; earlier states are not
recomputed when the queried bits are reset. No arrival order is conditioned on.

By (R), the next alive **squared** hazard obeys

```math
 \mathbb E[\mathbf1_{\rm survive}r^2]-p^2
 \ge p(1-p)-p^2=p-2p^2. \tag{D}
```

Set the potential to the squared current conditional hazard while alive,
and zero after exit. Every nonloop exits within the source's deterministic
finite reverse horizon. Sum (D), with initial hazard `p_start`, to obtain

```math
 -p_{\rm start}^2\ge
 \sum_i\mathbb E[\mathbf1_{\rm alive}p_i]
 -2\sum_i\mathbb E[\mathbf1_{\rm alive}p_i^2]
 =1-2\mathbb E P,
```

where `P` is the hazard at the actual exit. The first sum is one because
exit is certain; the second is `E P` by conditioning at each possible exit.
Consequently

```math
 \boxed{\mathbb E P\ge(1+p_{\rm start}^2)/2\ge1/2.} \tag{H}
```

This improves the previous `5/16` bound. The source hybrid transition needs
equal guard and test rates, which are still both `t`. Its safety comparison
turns (H) into pre-parity safe mass at least `|D_h intersect Y|/2`, less
the same baseline-birth charge `|D_h|/kappa`. The independent parity halves
both terms. Averaging the density mask, now of rate `rho`, gives

```math
 \mathbb E[\sigma_i\mid H]\ge
 \gamma|Y_i|-\frac{\rho n_i}{2\kappa},\qquad \gamma=\rho/4=5/32. \tag{S}
```

On unlisted groups the extension by zero is valid before averaging over `D`.
No conditioning on listing is introduced.

### A limitation of this abstract exit argument

The `1/2` in (H) is sharp under just these query hypotheses. Take `N`
independent Bernoulli-`t` bits. Each transaction tests the OR of the remaining
bits, querying in fixed order until a positive answer, or until all remaining
bits are negative. On survival, repeat with the remaining suffix. The next
failure probability equals the depleted current probability. Exit is certain
within `N+1` transactions, and every survival has a positive certificate.

Writing `a=1-t`, classify by the last positive bit, including no positives:

```math
 \mathbb E P=a^{2N}+t\sum_{j=0}^{N-1}a^{2j}
 =a^{2N}+\frac{1-a^{2N}}{2-t}.
```

For `t=1/m` and `N=m^2` this tends to `1/2`. Thus a larger universal
constant requires additional structure beyond these abstract hypotheses.
This is **not** a claimed hard matroid instance or an upper bound on the
achievable prophet ratio.

## 4. Integrate the residual tail

Keep the exact source conditioning: fix `H`, the parity, and all `D,C,T`
bits outside a true group `U_i`, before exposing its focal bits or listing.
For `n=|U_i|>=kappa`, the sharper source encoding yields a fixed family
`Rfamily` of size at most

```math
 \exp(A n/\kappa),\qquad A=5\log\kappa+5+4\log2.
```

Indeed, with `q=floor(n/kappa)`, its count is
`4^(3q) S_q(n)^3 S_(2q)(n)`. The first sequence uses only the density
generators; the second also uses the rank witnesses. Floors are handled
by the same binomial-sum bounds as in the source. `kappa>=4` suffices.

The sacrificed mask has independent memberships within the group of rate

```math
 p_O=\rho+(1-\rho)t,\qquad \lambda=-\log p_O>0.
```

Let `e_i` be the actual residual size when listed and `z_i<=n/kappa`, and
zero otherwise, exactly as in the source. Its selected residual is a member
of the fixed family and lies in `O`. If the family has size `N>=1`, for every
real `x>=0` the union bound gives

```math
 \Pr(e_i>x\mid\text{conditioning})\le
 \min\{1,N e^{-\lambda x}\}.
```

No independence is claimed for the selected residual. Integrating the bound
over all `x>=0` gives `(log N+1)/lambda`. Since `n>=kappa`,

```math
 \mathbb E[e_i\mid H]\le\frac{(A+1)n}{\kappa\lambda}.
```

An empty family makes the error zero. The source's deterministic inequality
`sigma_i<=kappa z_i+e_i` remains valid on all branches, including large rank
and unlisted outcomes. Therefore

```math
 \mathbb E[z_i\mid H]\ge
 \frac{\gamma|Y_i|-\epsilon n_i}{\kappa},\qquad
 \epsilon=\frac{\rho}{2\kappa}+\frac{A+1}{\kappa\lambda}. \tag{T}
```

This replaces the earlier cutoff error `delta+Pr(bad)` by its full integral,
uniformly even at `n=kappa`.

For the numerical certificate we round this error upward. The elementary
atanh series gives `log2<=25/36<7/10` and

```math
 \log(8/5)>2(3/13+(3/13)^3/3)=1032/2197>15/32.
```

Since `p_O=(5/8)(1+3t/5)`, set

```math
 \ell=15/32-3t/5>0,\qquad
 \bar\epsilon=\frac{5}{16\kappa}+\frac{473}{10\kappa\ell}
 =\frac{248756209}{5033066496}.
```

Here `lambda>=ell` and, for `kappa=2^11`,
`A+1=59 log2+6<473/10`. In what follows use `bar epsilon` in place of
the smaller error in (T).

## 5. Biased filtering and order-uniform accounting

For a filter mask of rate `h`, the source's elementary filter proof gives

```math
 \mathbb E_H u(Y)=(1-h)W,\qquad
 \mathbb E_H u(U)=\frac{1-h}{h}\mathbb E_H u(\mathrm{greedy}(H))
 \le\frac{1-h}{h}W.
```

To see the identity, condition on the memberships of labels preceding `e`
in rounded priority. Its span test is then fixed. The candidate probability
is `1-h` times that test, whereas greedy selection in `H` has probability
`h` times the same test. Sum weighted contributions. `Y` remains independent
and a subset of `U`. At `h=3/4` the coefficients are `1/4` and `1/3`.

The rank accounting and independent focal test thinning are unchanged.
The density-mask contribution to the later-generator cost becomes
`rho/kappa`, not `1/(4 kappa)`. Put `beta=(B-1)/B` and

```math
 L_0=\bar\epsilon+t\kappa+\frac{t\kappa+\rho}{B-1},\qquad
 s=(1-h)\left(\gamma-\frac{L_0}{h}\right).
```

The source's order-uniform comparison, summed over the large groups, gives

```math
 \mathbb E_R\min_\pi\mathrm{reward}_{\rm main}
 \ge\frac{\beta t s}{\kappa}W-t\gamma m_*.
```

Here `m_*` is the largest rounded nonloop weight. For completeness, the group
estimate is `E lambda_i >= (t/kappa)[gamma |Y_i|-(bar epsilon+t kappa)n_i
-(t kappa+rho)sum_(j>i)n_j]`. The weighted higher-group sum is at most
`u(U)/(B-1)`. Discarding groups with `n_i<kappa` loses comparison mass at
most `kappa m_*/beta`, giving the displayed negative term. These are
deterministic geometric estimates for every `B>1`.

The independent maximum branch has worst-order expectation at least `m_*/4`.
With main probability `p_main=1-t`,

```math
 (1-p_{\rm main})/4=t/4\ge p_{\rm main}t\gamma.
```

Thus mixing cancels the negative term. The minimum over permutations stays
inside the expectation throughout; seed visibility has not been weakened.

## 6. Finer finite phases and the exact coefficient

For any `theta>1`, `B=theta^L`, and positive scalar `x`, write
`k=floor(log_theta x)`. As `J` ranges uniformly over `0,...,L-1`, the rounded
values are `theta^(k-r)`, once each for `r=0,...,L-1`. Since `theta^k>=x/theta`,

```math
 \mathbb E_J u_J(x)\ge
 \frac{1-B^{-1}}{L(\theta-1)}x=\frac{\beta}{5}x.
```

The same lower bound applies to the rounded optimum by applying it to one
fixed true optimal independent set. Zero coordinates are unchanged. This is
the earlier standard finite-offset method with a finer rational mesh, not
a new rounding principle. Every phase is visible to the adversary, and the
fixed-phase guarantee already bounds its worst order.

Combining with the preceding affine guarantee and then using the source's
lossless glued-vector simulation gives

```math
 C=\frac{p_{\rm main}\beta^2 t s}{5\kappa}.
```

Exact integer arithmetic verifies `69^64>120*64^64`, hence `B>120` and
`beta>119/120`. In particular,

```math
 s>\frac{\gamma}{4}-\frac13\left(
 \bar\epsilon+t\kappa+\frac{t\kappa+\rho}{119}\right)
 =\frac{2652290047}{256686391296}>0.
```

Substituting these lower bounds gives `C>C_0>2^-36`, with `C_0` stated above.
The rational certificate checks these inequalities without floating point.

The simulation reveals and sacrifices the mask fixed by the seed, taking
the glued weight from the sample on that mask and the online value elsewhere.
Conditional on the entire seed this vector has the original product value
law, so it is independent of the seed. Ignored samples, sacrificed values,
and unused random bits can still inform the adversary's chosen permutation;
the pointwise minimum over every permutation covers all of them.

## 7. Resources, checks, and remaining review

Per label, draw two fair bits for `H` (three of four outcomes), three for `D`
(five of eight), sixteen each for `C` and `T` (one of `2^16`), and one for
the maximum mask. Shared bits are six for the phase, sixteen for the branch,
and one for parity. This is exactly `38n+23`, including unused-branch coins.

All new scalar constants and the 64 phase multipliers are fixed rationals.
The matroid rank/closure tables and enumeration of flats may be exponential
in `n`; they remain charged preprocessing and storage, not free oracles.
The rule uses only finitely many occupied groups and the source's finite
auxiliary timeline. Group exponents and exact observations need not have
bounded precision. For rational inputs the phase and level comparisons can
use exact rational powers; their costs depend on input bit lengths and
exponents. For arbitrary real observations this remains the original exact,
measurable model. No polynomial running-time, uniform precision, or practical
performance claim is made.

[check_quadratic_hazard.py](verification/check_quadratic_hazard.py) tests
the actual reverse process on the same 170 small matroid/weight instances
as the earlier checker, with nontrivial stress parameters. It checks failure
depletion, squared resource and drift, and the stronger global inequality
including `p_start^2`, using exact fractions.
[check_quadratic_ingredients.py](verification/check_quadratic_ingredients.py)
checks the query identity over all increasing Boolean events on up to four
bits, including adaptive query orders, empty/constant events, and both a
stress rate and the actual guard rate. It also checks biased filtering,
selected residual expectations, rational rounding boundaries, and the
abstract sharpness family. These are finite evidence; the universal proof
is the mathematical argument above.

The same-agent audit rechecked (Q)'s predictable denominator and conditional
martingale, both terminal outcomes, the frozen-state containment, the sign
of the telescope, the integral at `n=kappa`, all changed mask factors,
rational-phase boundaries, and full-seed simulation. Independent review
and formalization remain outstanding. The external announced proof is
still unavailable; strongest-current-result comparison and novelty are
unresolved. This repository contains the manuscript with reproducible evidence; it does not claim independent validation or established priority.
