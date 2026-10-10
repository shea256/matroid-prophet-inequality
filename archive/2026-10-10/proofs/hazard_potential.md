# A one-step hazard potential and a proposed bound above `2^-43`

October 10, 2026. Follow-up to the `2^-63` derivation in PR #2.
Status: **written proof with completed same-agent verification; independent
review pending**. The announced
`2^-47` coefficient is the numerical target; its proof, exact assumptions,
and possible unadvertised slack remain unavailable. No priority claim follows.
All logarithms are natural unless a base is specified.

## 1. The quantitative target

The old certificate cannot reach `2^-47`; see
[certificate_limit.md](certificate_limit.md). We change its exit argument,
then sharpen the residual-family count and use the actual sacrificed-mask
probability. All algorithmic and adversary assumptions remain those in the
[original derivation](parameter_refinement.md). The proposed tuple is

\[
 \kappa=2^{12},\quad t=2^{-20},\quad B=2^8,\quad
 p=1-t/4=1-2^{-22}.
\]

There are eight equally likely shared phases `J=0,...,7`. The main rule is
otherwise unchanged. The density mask still has rate `1/4`, and guard/test
rates agree. The new claim depends on the potential lemma proved below.

## 2. A local transaction inequality

Fix a pre-step reverse transcript for a nonloop that is still alive. Let `V`
be the unqueried domain, `A` the increasing event that the current transition
survives, and `p=Pr(A^c)>0`. Perform this one transition by the source's
predictable queries. Every survival has a positive certificate composed
solely of this transition's queried positives. Let `V'` be its random
unqueried domain at the end, and set

\[
 q=\Pr(A^c\text{ when only }V'\text{ has random bits and all others are zero}).
\]

Then `p<=q<=1`. The source's *one-query* log-resource calculation, summed
only through this transition, gives the stronger local information

\[
 \mathbb E[\log(q/p)]\ge 1-p. \tag{L}
\]

Here is the full calculation. During the transaction let `W` be the remaining
domain, `I` its queried positives, `f(W)` the failure probability with only
`W` random, and `f_I(W)` the failure probability with `I` forced positive.
Put `Z=f_I(W)/f(W)`. Initially `Z=1`, and always `0<=Z<=1`. For a predictably
chosen coordinate `e`, writing `W'=W\{e}`, the product law gives

\[
 \mathbb E[Z-Z'\mid\text{query transcript}]
 =Z\left(1-\frac{f(W)}{f(W')}\right)
 \le\log f(W')-\log f(W).
\]

At the end, survival implies `Z_end=0`, while otherwise `Z_end<=1`.
Thus `E[1-Z_end]>=Pr(survive)=1-p`. Summing the displayed inequality
over at most `|V|` queries proves (L). Predictable stopping is handled by
zero padding; no optional-stopping limit or infinite horizon is involved.
This is extracted from the source proof of `lem:transactions`, rather than
using only its coarser bound on the number of successful transactions.

## 3. Comparing the depleted event with the next hazard

Write the current reverse transition as `G_k(c,S)` and its output as `S'`.
The queried coordinates are exactly the departing domains, so the remaining
domain is the union of `G_j intersect S'_j`. Conditional on the complete
post-step transcript its bits still have their product law.

On survival, let `r` be the next conditional exit probability. The next
transition uses `G_(k-1)(c,S')`. For each bit assignment supported on `V'`,
monotonicity in time and state gives

\[
 G_{k-1}(c,S')\subseteq G_k(c,S).
\]

In the right-hand map all just-queried coordinates are set to zero, exactly
as in the definition of `q`. Hence the next survival event is a subset of
the depleted current survival event and **`r>=q` on survival**. This comparison
freezes `S` and `S'`; it does not recompute earlier states after changing bits.
It uses the full post-step transcript, not conditioning on the adversary's order.

An exit has conditional probability `p`. On exit `log(q/p)<=log(1/p)`.
Consequently (L) implies

\[
 \mathbb E[\mathbf1_{\rm survive}\log(r/p)]
 \ge1-p-p\log(1/p).
\]

Since `log(r/p)<=(r-p)/p`,

\[
 \mathbb E[\mathbf1_{\rm survive}r]-p
 \ge p-p^2\bigl(2+\log(1/p)\bigr). \tag{D}
\]

This also holds at `p=0` by taking the right side to be zero, since its left
side is nonnegative. At `p=1` it is equality: the next alive potential is zero.

## 4. Telescope the alive hazard

Index reverse steps in their actual processing order. Define the potential
to be the current conditional exit probability while the nonloop is alive,
and zero after it exits. Its initial value `p_start` is nonnegative; its final
value is zero because every nonloop exits by the deterministic final step.

Sum (D) over the finite horizon and take expectations. Since the sum of
expected alive hazards equals the probability of eventual exit, namely one,

\[
 \mathbb E\left[P\bigl(2+\log(1/P)\bigr)\right]
 \ge1+p_{\rm start}\ge1, \tag{G}
\]

where `P` is the hazard at the actual exit. Exits at zero hazard have
probability zero. The function `f(x)=x(2-log x)`, extended by `f(0)=0`,
is increasing and concave on `[0,1]`: `f'(x)=1-log x>0`, `f''(x)=-1/x<0`.
Therefore Jensen gives `f(E P)>=E f(P)>=1`.

The elementary exponential series gives

\[
 e^{6/5}>\sum_{j=0}^{4}\frac{(6/5)^j}{j!}
 =\frac{2059}{625}>\frac{16}{5},
\]

so `log(16/5)<6/5`, and `f(5/16)<(5/16)(2+6/5)=1`. It follows that

\[
 \boxed{\mathbb E P>5/16.}
\]

As in the source, `E P` equals the total squared-exit mass
`sum_b E[1_alive p_(b-1)^2]`. The existing hybrid-transition argument therefore
gives a pre-parity mass greater than `(5/16)|D_h intersect Y|`, less the same
baseline-birth loss `|D_h|/kappa`. After parity and averaging the quarter-rate
density mask, the safe-count estimate is

\[
 \mathbb E[\sigma_i\mid H]\ge
 \gamma|Y_i|-\frac{n_i}{8\kappa},\qquad \gamma=5/128. \tag{S}
\]

The new constant changes an ingredient of the old certificate, so it is not
subject to that certificate's `2^-54` upper bound.

## 5. Two sharper residual estimates

The source's first marked sequence uses only the density generators, at most
`q=floor(n/kappa)` occurrences. Its second uses generators and witnesses,
at most `2q`. Thus the same encoding proof gives the sharper count

\[
 |\mathfrak R_i|\le S_q(n)^2(4^qS_q(n))(4^{2q}S_{2q}(n))
 =4^{3q}S_q(n)^3S_{2q}(n).
\]

The binomial estimates already used in the source yield

\[
 \log|\mathfrak R_i|\le\frac n\kappa
 (5\log\kappa+5+4\log2).
\]

For `kappa=2^a` and `log2>2/3`, the number of bits in this entropy bound is
at most `(5a+12)n/kappa`. No new marked-pivot theorem is being assumed.

Next retain the sacrificed probability `p_O=(1+3t)/4` instead of bounding it
by `1/2`. Since `log(1+3t)<=3t` and `log2>2/3`,

\[
 \log_2(1/p_O)=2-\frac{\log(1+3t)}{\log2}\ge 2-5t=:\ell.
\]

For `a=12` and tail exponent `r_0=12`, choose
`delta=(5a+12+r_0)/(ell kappa)=84/(ell kappa)`. With the same conditioning
as the source residual-family lemma, the family is fixed before any focal bit.
The union bound at every `n>=kappa` is

\[
 \Pr(\exists R\in\mathfrak R_i:R\subseteq O,\ |R|>\delta n)
 \le2^{-r_0 n/\kappa}\le2^{-r_0}.
\]

The transfer error is therefore

\[
 \epsilon=\frac{1}{8\kappa}+\frac{84}{\ell\kappa}+2^{-12}.
\]

All unlisted-group, large-rank, and smallest-group branches are handled exactly
as in the original derivation; the bounds above preserve their quantifiers.

## 6. Final coefficient

The order-uniform rank accounting and affine main-branch bound are unchanged.
Put `beta=(B-1)/B` and

\[
 s=\gamma/2-\epsilon-t\kappa-\frac{t\kappa+1/4}{B-1}.
\]

For the proposed tuple,

\[
 s=\frac{4790554237}{1168228319232}.
\]

Mixing the maximum branch with probability `1-p=t/4` cancels the negative
largest-coordinate term, because `(1-p)/4=t/16>=p t gamma`.
Eight shared phases give an expected rounded optimum of at least `beta/8`
times the true optimum. The resulting coefficient is

\[
 C=\frac{p\beta^2t s}{8\kappa}
 >2^{-43}.
\]

The minimum over permutations remains inside the seed expectation. The same
lossless glued-vector argument gives the proposed one-sample guarantee against
the full-seed adversary, including its access to unused samples and values.
Predrawing all coins uses `44n+26` fair bits: per label `1+2+20+20+1`, and
three phase bits, 22 branch bits, and one parity bit. Exact-real observations,
arbitrary finite matroids, prefix feasibility, integrable optimum, and the
absence of a polynomial-time claim are unchanged.

The coefficient comparison alone exceeds the announced `2^-47` headline.
It cannot establish superiority over an unavailable proof's strongest derived
constant or establish novelty. The potential lemma needs particular scrutiny:
the depleted event and the next-step event must be compared on exactly the
remaining product domain after the complete ordinary transcript.

## 7. Verification actually completed

[certify_hazard_constants.py](../verification/certify_hazard_constants.py)
certifies the exponential partial sum, the entropy and tail constants, mixture,
slack, and final coefficient with exact fractions. The coefficient is

\[
 \frac{25618620910087559025}{216345186630601448946989472415744}
 \approx1.04159\,2^{-43}\approx16.6655\,2^{-47}.
\]

The old residual bound combined with the new exit lemma alone also produces
a coefficient above `2^-47`. Thus the essential gain can be isolated from
the two further residual refinements.

[check_hazard_potential.py](../verification/check_hazard_potential.py) checks
the actual source reverse map on 170 matroid/weight instances: all labeled
matroids of sizes one through three with the specified two-level weights,
plus 18 selected four-element uniform, partition, and triangle-with-loop
examples. It fixes `H` empty, enumerates density masks and guard assignments,
and uses `kappa=2`, guard rate `1/4` to exercise nontrivial paths. It checks
22,399 positive certificates, 3,186 depleted-event comparisons, 4,130 local
log-resource inequalities, 4,916 drift inequalities, and 3,153 global hazard
inequalities. All pass. Logarithms use outward rational bounds from 24 terms
of the atanh series after dyadic range reduction.

The negative control uses 64 steps of hazard `1/16` followed by certain exit.
Its mean exit hazard is less than `5/16`, despite nondecreasing hazards and
finite eventual exit. It fails the needed structural hypotheses and shows
why they cannot be omitted from the potential lemma.

The same-agent second pass rechecked the query-ratio identity, the frozen-state
containment on the precise depleted product domain, the sign of the drift
inequality, zero/one hazard endpoints, and the Jensen step. No gap was found.
These are written mathematical checks supported by finite certificates, not
an independent review or a universal machine-checked proof. The original
source dependencies and strongest-current-baseline limitations remain.
