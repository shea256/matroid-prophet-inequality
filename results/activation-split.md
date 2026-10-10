## Activation generators and joint mask membership

The [shared framework](../paper/framework.md) supplies the rule, quadratic
exit bound, linked streams, and final payoff calculation. We retain the
preceding reconstruction and projection lemmas, recalled here in full, then
improve three linked estimates: safety conditional on activation membership,
the fixed scores of activation generators, and the joint mask-membership
probability. The comparison optimum and new classifications are analysis
objects; the online rule uses neither.

### Retained insertions determine the old basis


**Reconstruction lemma.** Fix an ordered list of old occurrences in a finite
matroid and interleave specified movable occurrences arbitrarily. If the
greedy scan retains movable occurrence set $T$, its retained old occurrences
are exactly the greedy scan of the old list after contracting the labels
of $T$. Thus $s$ specified movable occurrences admit at most $2^s$ retained
bases of occurrences.

**Proof.** Let $A$ be the retained old occurrences preceding an old occurrence
$e$. If the interleaved scan rejects $e$, its label is spanned by $A$ and
the movable occurrences already retained, a subset of $T$. It is therefore
spanned by $A\cup T$. If the scan retains $e$, the final retained set is
independent and contains $A\cup T\cup\{e\}$, so $e$ increases rank over
$A\cup T$. Induction over the old list proves the contraction-scan identity.
Occurrences are distinguished even when labels repeat; retained occurrences
cannot repeat a label or be loops. The argument includes $T=\varnothing$.
For fixed $T$ the whole retained basis is fixed, and there are at most $2^s$
choices of $T$.

In particular, the source's general marked-pivot bound improves from
$4^sS_s(m)$ to $2^sS_s(m)$ with its affine-sign proof unchanged. For the
actual two streams, forced retention gives a stronger bound still.

Choose the density generators by the source's canonical forward extension
rule. At time $k$, the first-stream prefix before the new generators spans
$\operatorname{cl}(F(k)\cup X(k-1))$. Each new generator increases rank over
this flat and earlier generators in its batch. Every generator is therefore
retained in that stream, so its retained basis has one possibility for fixed
generator set $J$.

Every witness in $Z_b$ is retained in the second stream: its prefix spans
$X(b-2)\cup K_b$, and $Z_b$ is an independent extension over that base.
The same-mark generator reorderings in the joint affine representation
leave endpoint spans unchanged, so this remains true after reordering.
For fixed $J,Z$, the second retained movable set is $Z\cup J'$ for some
$J'\subseteq J$. The reconstruction lemma gives at most $2^j$ second bases,
where $j=|J|$, with no factor depending on $z=|Z|$. Second-stream generators
are not all forced; the finite checks include omitted ones.

Keep the three generator types and the same $j+z$ variables from the joint
affine representation. On any fixed set of $m$ tested labels, its $2m$
affine forms have at most $S_{j+z}(2m)$ strict sign patterns. Consequently,
for fixed $J,Z$, the residual count is at most

$$
6^jS_{j+z}(2m).
$$

This counts the restricted streams having the forced-retention properties;
every actual stream belongs to this family. Old paths, retained bases for
each subset, and affine coefficients are fixed before the focal masks.
Timeline length affects coefficients, not dimension. All three generator
types, including early invalid insertions, remain charged.

### Project the witnesses and residual onto the comparison optimum

Fix a phase and filter $H$, and let $I^*$ be the fixed tie-broken optimum of
the rounded full vector. Put $Y=I^*\setminus H$. For a true group $U$, write
$n=|U|$ and $y=|Y\cap U|$. Condition further on parity and masks outside $U$,
without conditioning on listing or any focal bits. Both $U$ and $Y\cap U$
are fixed. The online rule does not receive or compute $I^*$.

At each valid nominal birth layer choose, by fixed label order, a basis
extension

$$
Z_b'\subseteq(P_b\cap Y)\setminus O
\quad\text{over }X(b-2)\cup K_b,\qquad O=D\cup C.
$$

Let $z'=\sum_b|Z_b'|$ and

$$
R_Y=\bigcup_b\left[(P_b\cap Y)\setminus
\operatorname{cl}(X(b-2)\cup K_b\cup Z_b')\right].
$$

The layers are disjoint, so $Z'=\bigcup_bZ_b'$ has size $z'$ and is contained
in $Y\cap U$. Its spanning property gives $R_Y\subseteq O$. All safe samples
counted in $\sigma$ lie in $Y$. A safe sample at layer $b$ outside $R_Y$
lies in the witness span but outside $Q'_b=Q(F(b-2)\cup K_b)$. Since
$X(b-2)\cup K_b\subseteq Q'_b$, the source density inequality bounds their
number by $\kappa\operatorname{r}(Z_b'\mid Q'_b)\le\kappa|Z_b'|$. Thus

$$
\sigma\le\kappa z'+|R_Y|.
$$

The full nominal statistic satisfies $z\ge z'$ by rank monotonicity in each
layer. Lower-bounding $z'$ therefore lower-bounds the full $z$ in the original
test-thinning lemma. The alternative witnesses use no focal test bits.

Use $Z_b'$ in the two streams and test only $Y\cap U$. Their mark-one
intersection is exactly $R_Y$, and both forced-retention properties continue
to hold. Summing over generator and witness subsets gives fixed families

$$
|\mathcal F_{j,z'}|\le
\binom nj\binom y{z'}6^jS_{j+z'}(2y).
$$

Impossible subset choices only overcount. Generators may overlap the tested
labels; no independence involving their adaptive selection is used. This
bound includes zero sizes and dimensions exceeding $2y$.

In the refinement below, write $z$ for the projected statistic $z'$ just
defined, and $z_{\rm full}$ for the original nominal statistic. For a true
group $U$, put $n=|U|$ and $y=|Y\cap U|$.

### Keep activation loss conditional on activation generators

Fix the rounded full vector, $H,D$, and a listed group. Put
$J_0=\{g\in J:\tau(g)=a\}$ and $J_1=J\setminus J_0$, and write their sizes
as $j_0,j_1$. The canonical forward construction gives

$$
j_0=\operatorname{r}(Q(F_{\varnothing})),\qquad
\tau(g)\ge a+2\ (g\in J_1),\qquad
\kappa(j_0+j_1)\le |D\cap U|.
$$

There are no generators at $a+1$, because the nominal flat does not change.
Write $Y=I^*\setminus H$, as before. Membership in $Q(F_{\varnothing})$ is determined
by $H,D$ and the fixed weights, before any guard or test bits are drawn.
For each sampled $d\in Y\cap U$ outside that flat, every possible birth is valid
(before the parity restriction). Apply the quadratic exit bound to this
fixed label. Its squared-exit mass is at least $1/2$, all at valid births;
the hybrid implication and independent parity therefore give safety
probability at least $1/4$. Sum only over these labels. Since $Y$ is
independent, at most $j_0$ of its sampled labels lie in $Q(F_{\varnothing})$. Thus

$$
\mathbb E[\sigma\mid H,D]
\ge\frac{|D\cap Y\cap U|-|D\cap Y\cap U\cap Q(F_{\varnothing})|}{4}
\ge\frac{|D\cap Y\cap U|-j_0}{4}.
$$

This does not subtract a unit exit contribution from an unconditional
half-exit bound. It applies the half-exit bound directly to the labels with
no excluded birth. On unlisted groups all these statistics are zero. On
averaging $D$, for a true group with $y=|Y\cap U|$,

$$
\mathbb E\sigma\ge \rho y/4-\mathbb E j_0/4.
$$

### Activation generators require no time variables

Fix $H$, parity, and all masks outside a true group $U$; its potential
listed index and activation $a$ are fixed, without conditioning on listing.
Fix disjoint label sets $J_0,J_1,Z$, where $Z$ is the projected witness
set of the preceding proof. Every generator belongs to $D$, every witness
belongs to $Y\setminus(D\cup C)$, and all these role sets are disjoint.

In both marked streams, $J_0$ has a fixed insertion position and fixed
scores. In the first stream its time is $a$, with negative mark. In the
second it is inserted at endpoint $a$ or $a+1$, depending on parity, with
positive mark. Both endpoints are invalid births; there are no competitors
or witnesses there, and their incoming old flat is the loop flat. Thus
these occurrences are retained. Incorporate them into the fixed old lists.
Their labels are still enumerated; only their insertion-time variables
and type choices disappear.

All active generators are retained in the first stream. Old-basis
reconstruction therefore fixes that retained basis for the specified sets.
In the second stream all witnesses are retained, and an arbitrary subset
of the $j_1$ active generators can be retained. There are at most $2^{j_1}$
second bases. It would be invalid to force every active generator there.

Because every active time is at least $a+2$, the shared affine representation
has only two active-generator types: $(1,1)$ for a valid-parity insertion
and $(-1,2^T)$ for the preceding-parity insertion shifted to its endpoint.
The earlier third type was an activation occurrence, now a fixed constant.
All fixed coefficients depend only on the enumerated role sets and the
outside conditioning. There are $j_1+z$ common variables, with $z=|Z|$,
and at most $2y$ affine forms on the tested labels $Y\cap U$.
For each fixed role assignment the number of residuals is at most

$$
4^{j_1}S_{j_1+z}(2y),\qquad
S_d(m)=\sum_{i=0}^{\min(d,m)}\binom mi.
$$

This counts all actual streams before exposing the focal bits. It includes
zero sizes, loops in old lists, repeated old occurrences, and dimensions
exceeding $2y$. The old reconstruction and affine proofs apply with the
fixed activation occurrences added to their old lists.

### Use the joint mask-membership event

Let $O=D\cup C$, $p=\rho+(1-\rho)t$, and $\lambda=-\log p$. For each fixed
role assignment and fixed candidate residual $R\subseteq Y\setminus Z$,
put $J=J_0\cup J_1$. Across labels the focal mask pairs are independent,
so the exact joint probability is

$$
\Pr(J\subseteq D,\ Z\cap O=\varnothing,\ R\subseteq O)
=\rho^{|J|}(1-p)^{|Z|}p^{|R\setminus J|}
\le\rho^{|J|}p^{-|J\cap Y|}(1-p)^{|Z|}p^{|R|}.
$$

The correction $p^{-|J\cap Y|}$ is essential: a generator can also
be in the residual, so multiplying independent-looking generator and
residual probabilities would undercount. Witnesses are disjoint from
both the generators and the residual; invalid assignments can be omitted.

Choose $\mu>1/4$, $\nu>0$, and positive tilts $u,w,v<1$ satisfying

$$
\rho\left(p^{\mu-1/4}+\frac{4p^\mu}{v}\right)\le u,
\qquad \frac{(1-p)p^\nu}{v}\le w.
$$

On listed outcomes let
$e=(|R|-(\mu-1/4)j_0-\mu j_1-\nu z)_+$; otherwise let $e=0$.
Use the residual count, the joint probability bound, and
$v^d S_d(2y)\le(1+v)^{2y}$ in a union bound for $e>x$, with $x\ge0$.
For labels outside $Y$, the disjoint roles are none, activation generator,
and active generator. For labels in $Y$, there is also the witness role,
and generator roles pay the factor $1/p$. Their generating products give

$$
\Pr(e>x)\le \min\{1,Mp^x\},\qquad
M\le(1+u)^{n-y}(1+u/p+w)^y(1+v)^{2y}.
$$

To see the generating weights explicitly, an activation generator has
weight $\rho p^{\mu-1/4}$, an active generator $4\rho p^\mu/v$, and a witness
$(1-p)p^\nu/v$. The first two sum to at most $u$, and the last is at most
$w$. Enumerating these disjoint choices per label proves the displayed
tail bound. The actual selected sets may depend on the whole mask; only
each fixed choice uses the joint probability formula. No conditional
independence of the selected residual is assumed.

Writing

$$
A=\log(1+u),\qquad
B_Y=\log\frac{1+u/p+w}{1+u}+2\log(1+v),
$$

integration gives $\mathbb E e\le(nA+yB_Y+1)/\lambda$. The additive constant
remains and will be paid by the maximum branch. For any $0<d\le\lambda$,
use $p\ge\rho$ and $\log(1+x)\le x$ to obtain the convenient rational bounds

$$
\mathbb Ee\le\frac{n u+y b_Y+1}{d},\qquad
b_Y=\frac{u(1/\rho-1)+w}{1+u}+2v.
$$

### Cancel activation loss before averaging the generator budget

The projected residual comparison is still $\sigma\le\kappa z+|R|$.
By the definition of $e$, pointwise

$$
\sigma+j_0/4
\le(\kappa+\nu)z+\mu(j_0+j_1)+e.
$$

Take expectations and combine the safety bound, the integrated tail, and
the generator budget. The $\mathbb E j_0/4$ terms
cancel. The full nominal rank is at least the projected witness rank, so
it satisfies the existing rank interface with

$$
\begin{gathered}
K=\kappa+\nu,\qquad
\bar\gamma=\rho/4-b_Y/d,\qquad
\epsilon=\mu\rho/\kappa+u/d,\qquad a_0=1/d,\\
\mathbb E[z_{\rm full}\mid H]\ge
\frac{\bar\gamma y-\epsilon n-a_0}{K}.
\end{gathered}
$$

The old explicit $\rho/(2\kappa)$ error has disappeared because the
activation penalty is smaller by $1/4$, not because activation births
are assumed safe. All projected witnesses still avoid focal test bits.

The preceding full payoff calculation applies unchanged after substituting
the new rank interface. In particular retain both later-cost factors and define

$$
L_0=\epsilon+Kt+\frac{Kt+K\rho/\kappa}{B-1},\qquad
s=(1-h)(\bar\gamma-L_0/h).
$$

Small groups and the additive error cost at most
$t(\bar\gamma\kappa+a_0)m_*/K$. Verify
$(1-t)(\bar\gamma\kappa+a_0)/K\le1/4$, so the maximum branch cancels them.
The phase average then gives

$$
C=\frac{(1-t)\beta^2 t s}{L(\theta-1)K},\qquad
\beta=(B-1)/B.
$$

All order minima remain inside seed expectations. The same lossless
sample/value simulation covers the adversary's knowledge of ignored
samples, sacrificed values, and unused seed bits.

### Exact parameters, resources, and limitations

The algorithmic parameters are

$$
\begin{gathered}
\kappa=176,\quad\rho=3/8,\quad h=3/4,\quad t=11/2^{17},\\
\theta=261/256,\quad L=256,\quad B=\theta^L,\quad p_{\rm main}=1-t.
\end{gathered}
$$

Choose

$$
\begin{gathered}
\mu=113/8,\quad\mu_0=111/8,\quad\nu=117/8,\quad K=1525/8,\\
u=1/1056,\quad w=1/4096,\quad v=1/648,\quad d=49/50.
\end{gathered}
$$

The [exact certificate](../verification/certify_activation_split.py)
checks $\lambda>d$ by outward log intervals and a separate 20-term positive
atanh sum. Since $p>(3/4)^4$, we have $p^{-1/4}<4/3$. Set
$A_*=\rho(4+4v/3)$. The separate exact power inequalities

$$
A_*^8p^{113}<(uv)^8,\qquad
(1-p)^8p^{117}<(wv)^8
$$

prove both tilt inequalities; log intervals independently cross-check these finite scalar
comparisons. The same certificate verifies $B>140$, $L(\theta-1)=5$,
positive slack, maximum-branch cancellation, and

$$
\begin{gathered}
\bar\gamma=\frac{23826973}{268494912},\qquad
\epsilon=\frac{51433}{1655808},\qquad a_0=\frac{50}{49},\\
s>\frac{9225899434547}{1681525638955008}>0.
\end{gathered}
$$

Using $\beta>139/140$ and $B-1>139$ in the final coefficient yields $C>C_4$. It also reruns
the preceding certificate before comparing the improvement, and checks
that $C_4<2^{-30}$. No claim is made to cross that next threshold.

The resulting conservative coefficient is

$$
C_4=\frac{8003458533570087953}{16807475946150704657203200000}
>\frac{51}{50}\,2^{-31}>2^{-31}.
$$

This is approximately $4.76184440734\times10^{-10}$, or $1.14973122069$
times the preceding exact $C_3$: a $14.97\%$ increase in the guaranteed
fraction. It is approximately $31.44938$ times the initial announced $C_0$
certificate above $2^{-36}$. These compare guarantees, not measured performance.

The fair-bit implementation uses $2+3+17+17+1=40$ bits per label and
$8+17+1=26$ shared bits, all drawn initially. The phase distribution is
still uniform on 256 rational offsets. No additional sample, access to the
comparison optimum, or bounded-precision assumption is introduced.

The [numerical search](../experiments/search_activation_split.py) executes
24 deterministic starts in the previous formula and each of three cumulative
modes: conditional safety, activation splitting, and joint membership.
Its selected dyadic certificate is conservative; the search is not a global
optimum proof. The [finite checker](../verification/check_activation_split.py)
checks activation-fixed affine streams and conditional safety over all filter
masks on the inherited small matroid/weight cases, exact joint membership
laws with overlaps, disjoint-role generating products, and adaptive family
selection. These finite facts do not prove the universal assertions above.

See the [same-agent audit](../proofs/activation_split_audit.md) and
[baseline refresh](../verification/activation_baseline_audit.json).
Independent review and formalization remain pending. No priority or confirmed
strongest-known-bound claim is made.
