# A finite-seed parameter refinement of #111

Date: October 10, 2026. Status: **candidate theorem with a written derivation**.
The numerical inequalities have an exact rational certificate. This is not a
Lean formalization or independent review. A stronger external announcement
of `2^-47` remains unverified; see [BASELINE.md](../BASELINE.md).

The expanded [research note](../manuscript/note.pdf) defines every analysis
statistic and presents the full rule. The [second-pass audit](audit.md) records
source interfaces, conditioning, and additional online-rule checks. This
same-agent pass found no gap; it does not change the candidate classification.

## Statement and source dependency

For every finite known labeled matroid, the construction below is intended to
give a measurable, distribution-independent, one-sample rule with

\[
  \mathbb E[\operatorname{reward}]\ge 2^{-63}
       \mathbb E[\operatorname{OPT}(V)].
\]

All `2n` sample/value coordinates are mutually independent and nonnegative,
the two coordinates at each label have identical laws, the seed is independent
of them, and only the offline optimum must be integrable. The adversary may
choose a measurable arrival permutation after seeing the entire sample,
value, and seed vectors. Decisions use only samples, seed, and arrival history,
and every accepted prefix is independent. The seed has finitely many fair bits.
No polynomial-time implementation is asserted.

We use the algorithm and combinatorial arguments in the September 23 manuscript
at OpenAI/math commit `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`.
The exact sources are [algorithm.tex](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/One-Sample-Suffices-for-Matroid-Prophet-Inequalities-against-an-Almighty-Adversary-September-23-2026/build/sections/algorithm.tex),
[safety.tex](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/One-Sample-Suffices-for-Matroid-Prophet-Inequalities-against-an-Almighty-Adversary-September-23-2026/build/sections/safety.tex),
[transfer.tex](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/One-Sample-Suffices-for-Matroid-Prophet-Inequalities-against-an-Almighty-Adversary-September-23-2026/build/sections/transfer.tex),
and [accounting.tex](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/One-Sample-Suffices-for-Matroid-Prophet-Inequalities-against-an-Almighty-Adversary-September-23-2026/build/sections/accounting.tex).
This proof redoes their numerical implications. It does not claim a new
marked-pivot lemma, density decomposition, or reverse-exposure construction.

## 1. Algorithm and parameters

First consider a fixed nonnegative hidden weight vector. Choose

\[
 B=2^{16},\quad \kappa=2^{18},\quad t=2^{-29},\quad
 p=1-2^{-35},\quad J\sim\operatorname{Unif}\{0,\ldots,15\}.
\]

Round every observed or arriving positive weight to

\[
 u_J(x)=2^J B^{\lfloor\log_B(x/2^J)\rfloor},\qquad u_J(0)=0.
\]

The same offset is used for all labels. Choose the main branch with probability
`p` and the maximum branch otherwise. In the main branch use independent masks
`H,D,C,T`, of rates `1/2,1/4,t,t`, respectively, and a fair layer parity.
Reveal and sacrifice `H union D union C`. The candidate, density, nominal-path,
guarded-path, and layer decisions are precisely those of the source, with the
new `B,kappa,t`. In the maximum branch reveal a fair mask and take the first
unrevealed positive nonloop whose rounded priority exceeds the revealed maximum;
use a fixed label order for ties. All coins are drawn before observing weights.

For clarity, the source main construction uses candidates

\[
 U=\{e\notin H:u_e>0,\ e\notin\operatorname{cl}(H_{>e})\}.
\]

List the groups with a positive `D` count in increasing weight order. For listed
group `h`, `Q_h(P)` is the largest flat containing `P` that maximizes
`|D_h intersect Z| - kappa r(Z)`. Set `a_h=-3h`. The map is enabled at auxiliary
times `k>=a_h`, and is the identity earlier. Starting from `F_0(k)=cl(empty)`
for `k<0` and `E` otherwise, construct

\[
 X_h(k)=Q_{h,k}(F_{h-1}(k)),\qquad
 F_h(k)=\operatorname{cl}(X_h(k)\cup(C_h\cap X_h(k+1))).
\]

A candidate in group `h` with nominal birth `b` is eligible only if it is
unsacrificed, `T`-positive, `b>=a_h+2`, of the selected parity, and outside
the final flat `F_m(b-2)`. At that layer it is accepted exactly when independent
over this flat and the previously accepted labels in the layer. The source's
nesting argument proves feasibility for every ordering and prefix.

## 2. Sharper exit mass, with the original exposure argument

Let `P_exit` be the conditional exit probability at the actual reverse-exposure
exit of a fixed nonloop. The disjoint-query-certificate lemma in the source is
independent of the numerical choices of `B,kappa,t`. Its dyadic band argument,
with cutoff `eta=2^-m`, gives

\[
 \Pr(P_{\rm exit}<2^{-m})
 \le 2^{1-m}((m+2)\log 2+1).
\]

The source chooses `m=12` and then replaces this bound by `1/2`. Instead choose
`m=4`. The positive series

\[
 \log2=2\sum_{j\ge0}\frac{1}{(2j+1)3^{2j+1}}
\]

gives `2/3 < log 2 <= 25/36 < 7/10`: keep the first term, and for the upper
bound replace every later denominator `2j+1` by `3` and sum a geometric series.
Consequently the bad-exit probability is at most

\[
 2^{-3}(6\cdot7/10+1)=13/20.
\]

Since every nonloop exits, the sum of squared exit masses is at least

\[
 \sum_b\mathbb E[\mathbf1_{\{d\in X_h(b)\}}p_{b-1}^2]
 =\mathbb E[P_{\rm exit}]
 \ge (1/16)(7/20)=7/320.
\]

The source's hybrid-transition proof turns each squared exit mass into a
birth-and-safety probability. Its deterministic inclusion and conditional
product law require the guard and test rates to be equal; our rates satisfy
that requirement. They do not require `t=2^-140`.

Write `Y=I* minus H`, for a fixed optimum of the rounded vector. The source
generator bound gives `r(Q_h(cl(empty))) <= |D_h|/kappa`; because `Y` is
independent, at most this many `D_h intersect Y` labels can be lost at the
excluded baseline birth. There is no birth at `a_h+1`. The independent fair
parity therefore gives

\[
 \mathbb E[\sigma_h\mid H,D]
 \ge \frac7{640}|D_h\cap Y|-\frac{|D_h|}{2\kappa}.
\]

Averaging the `D` mask of rate `1/4`, extending statistics by zero on unlisted
true groups, yields

\[
 \mathbb E[\sigma_i\mid H]
 \ge\gamma |Y_i|-\frac{n_i}{8\kappa},
 \qquad \gamma=\frac7{2560}.
 \tag{1}
\]

Listing is not conditioned upon in this averaging.

## 3. Residual count and tail at the smallest analyzed group

For a true group of size `n>=kappa`, the source constructs, before exposing
its own `D,C,T` bits, a family containing every possible residual when its
nominal rank `z` is at most `n/kappa`. Put `q=floor(n/kappa)` and
`S_d(n)=sum_{ell=0}^d binom(n,ell)`. The marked-pivot proof gives

\[
 |\mathfrak R|\le S_q(n)^2(4^{2q}S_{2q}(n))^2.
\]

Using the source's binomial estimate with `1/kappa` and `2/kappa` gives

\[
 \log |\mathfrak R|
 \le \frac n\kappa(6\log\kappa+6+4\log2).
 \tag{2}
\]

This is the sharper estimate already present in its proof, before it is relaxed
to `1000 log(kappa) n/kappa`. It is valid for `kappa>=4`, including `n=kappa`;
the floor inequalities are preserved. No new pivot-counting claim is used.

For `kappa=2^a`, the elementary bound `log2>2/3` turns (2) into

\[
 |\mathfrak R|\le 2^{(6a+13)n/\kappa}.
\]

Here `a=18`, so the exponent coefficient is `121/kappa`. Independently at each
focal label, the sacrificed mask `O=D union C` has probability
`1/4+3t/4 <= 1/2`. Therefore, with `delta=139/kappa`,

\[
 \Pr(\exists R\in\mathfrak R:
       R\subseteq O,\ |R|>\delta n)
 \le 2^{-(139-121)n/\kappa}
 \le 2^{-18}.
 \tag{3}
\]

This bound is conditional on `H`, parity, and masks outside the focal group.
Those determine the family but not its own bits. The bound is valid already
at `n=kappa` and improves as `n` grows. Let the residual error be zero on an
unlisted outcome or an outcome with `z>n/kappa`, and the residual cardinality
otherwise. Its conditional expectation is at most
`(delta+2^-18)n=140n/kappa`.

The deterministic safe-count comparison is `sigma <= kappa z + residual_error`.
Together with (1), this gives

\[
 \mathbb E[z_i\mid H]
 \ge\frac{\gamma |Y_i|-\epsilon n_i}{\kappa},
 \qquad \epsilon=\frac{1}{8\kappa}+\frac{140}{\kappa}
 =\frac{1121}{2^{21}}.
 \tag{4}
\]

These changes retain the source's combinatorial family and handle all its
listing and large-rank branches. They change only the probabilistic and
numerical deductions from that family.

## 4. Exact accounting, including all later-group costs

Let `lambda_i` be the source's final-layer tested-rank statistic. Its
order-uniform rank lemma holds before an arrival order is chosen, and its
common-generator argument charges later path expansions only once. Retain
the exact density-mask expectation `1/(4kappa)`, instead of relaxing it to
`1/kappa`. Independent thinning then yields, for `n_i>=kappa`,

\[
 \mathbb E[\lambda_i\mid H]\ge\frac t\kappa
 \left(\gamma|Y_i|-(\epsilon+t\kappa)n_i
       -(t\kappa+1/4)\sum_{\ell>i}n_\ell\right).
 \tag{5}
\]

The conditioning for thinning includes `H,D,C`, parity, and all `T` bits
outside the focal group, and excludes any chosen arrival order. All true
group counts bound the costs before taking expectations; no selected-group
independence is asserted.

For now fix the offset and rescale weights by `2^-J`, so the positive rounded
weights are powers of `B`. Set `beta=(B-1)/B`, `W=OPT(u)`, and let `m*` be the
largest positive nonloop rounded weight. For each realization,

\[
 \min_\pi u(A_{\rm main}(\pi))
 \ge \beta\sum_{i:n_i\ge\kappa} B^i\lambda_i.
 \tag{6}
\]

Indeed each accepted weight `B^ell` is counted by at most
`sum_{i<=ell} B^i = B^ell/beta`. Also

\[
 \sum_i B^i\sum_{\ell>i}n_\ell
 \le\frac{u(U)}{B-1},\qquad
 \sum_{i:n_i<\kappa}B^i|Y_i|
 \le\frac{\kappa m_*}{\beta}.
\]

The candidate-filter identities are `E u(Y)=W/2` and `E u(U)<=W`.
Combining these facts with (5)-(6) gives an affine bound for every rounded
vector, with no case split on its largest coordinate:

\[
 \mathbb E[\min_\pi u(A_{\rm main}(\pi))]
 \ge A W-t\gamma m_*,
\]

where

\[
 s=\gamma/2-\epsilon-t\kappa-
                  \frac{t\kappa+1/4}{B-1},\qquad
 A=\frac{\beta t}{\kappa}s.
 \tag{7}
\]

In our tuple, `s=3120271/9162457088 > 1/3072 > 0`. This is certified with
integer arithmetic. A negative affine lower bound on some weight vectors
causes no difficulty in the subsequent mixture.

## 5. Mix the branches without the original threshold loss

The maximum branch has worst-order expected reward at least `m*/4`: with
probability `1/4`, the first-priority nonloop is unobserved and the second
is observed. With only one positive nonloop its success probability is `1/2`.
Thus mixing with main probability `p=1-t/64` gives

\[
 \mathbb E[\min_\pi u(A(\pi))]
 \ge p A W + ((1-p)/4-p t\gamma)m_*\ge p A W.
 \tag{8}
\]

The last coefficient is nonnegative because
`(1-p)/4=t/256` and `p gamma <= gamma=7/2560 < 1/256`.
The adversary may see the branch and select its order accordingly: the
minimum is inside the expectation in each branch, so (8) remains valid.

## 6. Finite rounding offsets

For an arbitrary `x>0`, put `k=floor(log_2 x)`. Across the sixteen offsets,
the rounded exponents are exactly `k,k-1,...,k-15`. Hence

\[
 \mathbb E_J u_J(x)
 =\frac{2^{k+1}}{16}(1-2^{-16})
 \ge\frac\beta{16}x.
 \tag{9}
\]

The inequality also holds at zero. Choose an optimum set for the original
fixed vector before drawing `J`. Summing (9) on that set gives

\[
 \mathbb E_J\operatorname{OPT}(u_J)
 \ge\frac\beta{16}\operatorname{OPT}(w).
\]

For each fixed offset the rest of the seed still has its original product
law, and (8) holds for every order. Accepted true weights dominate rounded
ones. Therefore the complete fixed-vector rule satisfies

\[
 \mathbb E_{J,R}[\min_\pi w(A(J,R,\pi))]
 \ge \frac{p\beta^2 t s}{16\kappa}\operatorname{OPT}(w).
 \tag{10}
\]

This argument never requires the adversary to be ignorant of `J`.
Since `p beta^2>3/4`, `s>1/3072`, and `t/kappa=2^-47`, the coefficient in
(10) exceeds

\[
 \frac{3}{4}\frac1{3072}\frac{2^{-47}}{16}=2^{-63}.
\]

Its exact value is

\[
 \frac{105391776668216973667425}
 {696898287454081973172991196020261297061888},
\]

approximately `1.39485 * 2^-63`. Fixed-offset rounding alone, after the other
changes, gives more than `2^-75`; the sixteen offsets improve that certified
coefficient by `(B-1)/16`. Using offsets on the original parameters instead
gives `(1-2^-32)2^-266`; that separate local improvement is also recorded by
the certificate.

## 7. One-sample transfer and resource accounting

Use the source's lossless gluing reduction. For the complete initial seed
`R'`, let `B0(R')` be the sacrificed mask and define the analysis vector
`w_e=S_e` on it and `w_e=V_e` off it. Conditional on any seed, the mask is fixed,
so the glued vector has the product law of `V`, independent of the seed.
The fixed-vector rule uses only the sampled coordinates on this mask and
online values elsewhere. Every accepted weight is an actual online value.
For every realization its reward under the actual adversarial order is at
least the minimum over all permutations for that glued vector and seed.
Integrating (10) proves the proposed prophet inequality. This also allows
the order to depend on unused samples and values. Prefix feasibility bounds
reward by `OPT(V)` and supplies integrability, including when loop values
have no finite expectation.

All random choices have bounded fair-bit implementations: four offset bits,
35 branch bits (take the rare branch if all are zero), one main-parity bit,
and, for each label, one `H` bit, two `D` bits, 29 `C` bits, 29 `T` bits,
and one maximum-branch mask bit. Predrawing even unused branch coins uses
`62n+40` fair bits. No extra sample is needed. The seed law depends only on
the finite labeled matroid (in this implementation just its size).

An explicit finite implementation can query all subsets once to build a rank
and closure table, then enumerate flats in each density maximization. This
may require exponentially many queries, work, and stored entries; those costs
are not omitted from a claim of polynomial efficiency, because no such claim
is made. There are at most `n` listed groups and `O(n)` relevant auxiliary
times. Numerical values use the source's exact-real measurable model. For
rational input, dyadic levels can be located by exact integer comparisons,
with costs depending on bit length; arbitrary real observations do not have
a uniform finite-precision implementation. Uniform phase selection and the
new branch choice add the explicit finite-bit costs above. Reporting the
selected labels costs at least their output size.

Empty sets, loops, rank zero, ties, zero values, unbounded distributional
support, and weight levels of arbitrary positive or negative exponent are
covered by these same arguments. No linear representation is used.

## 8. Scope of verification

The source's complete TeX argument was read, and its parameter-dependent
inequalities were revisited above. Source combinatorial ingredients remain
external dependencies. The local scripts check scalar arithmetic and small
finite instances, not arbitrary matroids or all conditioning arguments.
No new Lean build was performed, and the source Lean development was not
compiled in this run. A second pass by this same agent is not independent
peer review. A proof of the external `2^-47` announcement would supersede
the numerical candidate here if it preserves the same model.
