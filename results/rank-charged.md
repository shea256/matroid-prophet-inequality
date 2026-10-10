## Rank-charged residual entropy

This result retains the shared construction, quadratic hazard lemma, and
joint pivot lemma in [the framework](../paper/framework.md). It replaces
the density cutoff by a weighted count over both generator and witness sizes.
The full one-sample and seed-visible adversary quantifiers are unchanged.

### A weighted family bound

Use the framework's conditioning for a true group $U$ of size $n\ge\kappa$.
For each fixed generator and witness pair $J,Z$ of sizes $j,z$, the joint
pivot lemma gives at most $3^j4^{2j+z}S_{j+z}(2n)$ residuals. That proof
has no equal-cutoff hypothesis. Therefore there is a family fixed before
focal masks for each $0\le j,z\le n$, with

$$
|\mathcal F_{j,z}|\le N_{j,z}:=
\binom nj\binom nz48^j4^z S_{j+z}(2n).
$$

Here $S_d(N)=\sum_{i=0}^{\min(d,N)}\binom Ni$. All insertion times and
witness-layer assignments are included in the joint affine count. Allowing
arbitrary, possibly overlapping subsets only increases this bound. The
actual witness union has size exactly the nominal rank $z$, because its
layers are disjoint. Choose the source's generators by a fixed rule; their
count satisfies $\kappa j\le|D\cap U|$ on each listed outcome.

Let $p_O=\rho+(1-\rho)t$ and $\lambda=-\log p_O>0$. Choose positive penalties
$\mu,\nu$ and $0<\xi,\eta,\zeta<1$ satisfying

$$
48e^{-\lambda\mu}/\zeta\le\xi,\qquad
4e^{-\lambda\nu}/\zeta\le\eta.
$$

For every integer $d\ge0$, including zero and $d\ge2n$,

$$
\zeta^dS_d(2n)\le(1+\zeta)^{2n}.
$$

Indeed, $\zeta^d\le\zeta^i$ for $i\le d$; sum and extend the binomial
expansion. Applying this at $d=j+z$ and summing over both sizes gives

$$
\begin{aligned}
\sum_{j,z=0}^nN_{j,z}e^{-\lambda(\mu j+\nu z)}
&\le(1+\zeta)^{2n}
\left(1+\frac{48e^{-\lambda\mu}}\zeta\right)^n
\left(1+\frac{4e^{-\lambda\nu}}\zeta\right)^n\\
&\le(1+\xi)^n(1+\eta)^n(1+\zeta)^{2n}\le e^{nd_0},
\qquad d_0=\xi+\eta+2\zeta.
\end{aligned}
$$

The last step uses $\log(1+x)\le x$. These are ordinary exponential
weighting and binomial identities; the contribution is their use in this
residual-to-rank estimate and the final theorem.

### Adaptive residuals and both charges

On a listed outcome, let $R$ be the actual residual with actual counts $j,z$,
and set $e=(|R|-\mu j-\nu z)_+$. Set $e=0$ on unlisted outcomes. For real
$x\ge0$, the event $e>x$ implies that some fixed $R\in\mathcal F_{j,z}$
satisfies $R\subseteq O$ and $|R|>x+\mu j+\nu z$. For each fixed residual,
the original conditional product law gives $\Pr(R\subseteq O)=p_O^{|R|}$.
The union bound and weighted count yield

$$
\Pr(e>x)\le\min\{1,e^{nd_0-\lambda x}\},\qquad
\mathbb E e\le\frac{nd_0+1}{\lambda}.
$$

The integral splits at $nd_0/\lambda$. The selected residual and its sizes
may depend on the mask; no independence of that selection is asserted.
The proof never multiplies this containment probability by a probability
for the selected generator set, which could overlap the residual.

The source comparison and generator bound imply pointwise

$$
\sigma\le\kappa z+|R|
\le(\kappa+\nu)z+\mu j+e
\le Kz+\frac\mu\kappa|D\cap U|+e,\qquad K=\kappa+\nu.
$$

On unlisted outcomes $\sigma=z=e=0$, so the final inequality also holds.
Since $\mathbb E|D\cap U|=\rho n$, the framework's safety estimate gives
its required rank interface with

$$
\mathbb E[z_i\mid H]\ge\frac{\gamma|Y_i|-\epsilon n_i}{K},\qquad
\epsilon=\frac\rho{2\kappa}+\frac{\mu\rho}{\kappa}
+\frac{d_0+1/\kappa}{\lambda},\qquad\gamma=\rho/4.
$$

Absorbing the additive one uses only $n_i\ge\kappa$. The inequality also
holds for negative numerators by direct rearrangement. Both charges are
necessary: the witness penalty increases $K$, and the generator penalty
contributes $\mu\rho/\kappa$. There is no density cutoff or exceptional event.

### Parameters and exact coefficient

Use

$$
\kappa=272,\quad\rho=13/32,\quad h=3/4,\quad t=2^{-14},\quad
\theta=261/256,\quad L=256,\quad p_{\mathrm{main}}=1-t,
$$

and analysis-only constants

$$
\mu=\nu=39/2,\quad K=583/2,\qquad
\xi=1/640,\quad\eta=1/8192,\quad\zeta=1/1280.
$$

The [exact certificate](../verification/certify_rank_charged.py) uses outward
rational atanh-series logarithm enclosures after dyadic range reduction and
verifies

$$
\lambda>9/10,\qquad
\mu\lambda>\log\frac{48}{\xi\zeta},\qquad
\nu\lambda>\log\frac4{\eta\zeta},\qquad B>140.
$$

The two penalty comparisons use the unrounded rigorous interval for
$\lambda$. The coarser $9/10$ alone is insufficient for the witness comparison
and is used only in the error below. With $d_0=133/40960$,

$$
\bar\epsilon=\frac\rho{2\kappa}+\frac{\mu\rho}{\kappa}
+\frac{d_0+1/\kappa}{9/10}=\frac{7847}{208896}.
$$

Use $\beta>139/140$, $B-1>139$, and $L(\theta-1)=5$. The framework's
slack satisfies

$$
s>\frac14\left[\frac{13}{128}-\frac43\left(
\bar\epsilon+Kt+\frac{Kt+K\rho/\kappa}{139}\right)\right]
=\frac{1019519}{174219264}>0.
$$

The factors $Kt$ and $K\rho/\kappa$ account for the changed denominator.
The small-group loss still uses the size threshold $\kappa$, giving
$t\gamma\kappa/K$ times the maximum. Since $K\ge\kappa$ and
$\gamma\le1/4$, the maximum branch cancels this loss. The final coefficient
is strictly greater than

$$
C_2=\frac{773895463001}{3203794364409053184000}
>\frac{33}{32}\,2^{-32}.
$$

It is approximately $1.0374747334\cdot2^{-32}$, or $3.93234995$ times the
preceding exact certificate and $15.95344868$ times the earlier $2^{-36}$
certificate. These compare guarantee coefficients, not measured performance.

The seed uses $2+5+14+14+1=36$ fair bits per label and $8+14+1=23$ shared
bits. The density mask accepts 13 of 32 equally likely outcomes; filter,
guard/test, and phase probabilities are likewise exact. Every coin is drawn
initially, including unused-branch randomness. The analysis penalties and
tilts require no algorithmic samples, bits, or computation.

### Verification and review

The [numerical search](../experiments/search_rank_charged.py) ran two attacks:
charge witness entropy with the old cutoff, then charge generator entropy
as well. It used 16 deterministic starts per mode and a declared 15-tuple
grid. No global optimality claim follows from this search.

The [finite checker](../verification/check_rank_charged.py) covers 78 weighted
generating bounds, 972 adaptive tail bounds, 216 integrated expectations,
and 45,824 path charges on 170 matroid/weight instances. The path checks use
small stress penalties and threshold 2 to exercise nonzero residuals and
ranks. Two abstract negative controls show why omitting either charge is
invalid; they are not hard matroid instances. The previous quadratic and
joint-encoding checkers remain in the reproducibility suite.

The [same-agent audit](../proofs/rank_charged_audit.md) checks the stratified
family, adaptive union bound, both charges, changed accounting factors, and
full-seed simulation. Independent mathematical review and formalization are
pending. Finite tests do not prove the universal theorem; its claim rests on
the written proof and cited source interfaces. No exhaustive novelty or
strongest-known-bound claim is made.
