## Three-state generator encoding and restricted overlap

The [shared framework](../paper/framework.md) supplies the rule, quadratic
exit bound, linked streams, and final payoff calculation. We recall the
retained-basis, projection, and activation lemmas, then sharpen the count
by merging two insertion types for generators omitted from the second
basis. Residual support restrictions also reduce the overlap charge.
These are analysis objects; the algorithm does not receive the comparison
optimum or its witnesses. The resulting coefficient is 7.10% above the
preceding [activation-split certificate](activation-split.md), with the
same one-sample and full-seed adversary assumptions.

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
Before the further compression below, this gives the preceding bound

$$
4^{j_1}S_{j_1+z}(2y),\qquad
S_d(m)=\sum_{i=0}^{\min(d,m)}\binom mi.
$$

This counts all actual streams before exposing the focal bits. It includes
zero sizes, loops in old lists, repeated old occurrences, and dimensions
exceeding $2y$. The old reconstruction and affine proofs apply with the
fixed activation occurrences added to their old lists.


### Three states suffice for each active generator

Fix the disjoint label sets $J_0,J_1,Z$. Freeze $J_0$ into the old lists
as above, and partition $J_1$ into three states: $J_+$ consists of generators
retained in the second basis with valid parity; $J_-$ consists of those
retained there with the other parity; and $J_o$ consists of those omitted
from the second basis. Their first-stream occurrences are all retained.

For $g\in J_+\cup J_-$, keep the positive score variable $x_g$ from the
shared encoding. Write $q=8(N+1)$ for its fixed block-spacing exponent,
where $N$ is the entire ground-set size. For $g\in J_o$, replace $x_g$ by
the signed variable $s_g=\eta_gx_g$, its actual first score. The scores
in the retained bases have the following form:

| State | First score | Second score | Residual status on $Y$ |
|---|---|---|---|
| $J_+$ | $x_g$ | $x_g$ | Present |
| $J_-$ | $-x_g$ | $2^q x_g$ | Absent |
| $J_o$ | $s_g$, either sign | No term | May be present |

An omitted generator has no occurrence in the second retained basis,
and hence no term in any of its support sums. Its unused second score
and parity need not be recorded separately: the signed first variable
already represents every actual first score. Witnesses retain their
negative score variables.

For a fixed assignment of these three states, the retained active subset
in the second stream is $J_+\cup J_-$. The first retained old basis is the
contraction complement of $J_1$, and the second is the contraction complement
of $J_+\cup J_-\cup Z$, with fixed activation occurrences in both old lists.
Their supports and old scores are therefore fixed. Both pivot tests are
affine functions of the same $j_1+z$ variables: positive $x_g$ for retained
active generators, signed $s_g$ for omitted ones, and witness variables.

Every actual stream supplies an assignment representing its support sums.
Their signs equal their last occurrences' marks because the actual absolute
scores are distinct powers with each exceeding the sum of preceding scores.
Allowing arbitrary real signed variables can only enlarge the family.
For each state assignment the $2y$ tested affine forms have at most
$S_{j_1+z}(2y)$ strict sign patterns. Thus the fixed-role family has size at most

$$
3^{j_1}S_{j_1+z}(2y).
$$

There is no extra factor for the second retained basis: the three states
already determine it. The bound covers zero sizes, repeated old occurrences,
old loops, and dimensions exceeding $2y$ by the same reconstruction and
arrangement arguments.

For a generator retained in both streams, its own occurrence is its pivot
in each. This proves the $J_+$ and $J_-$ residual statuses in the table.
Activation generators have negative first pivots, and witnesses have
negative second pivots. Consequently

$$
R\cap J\subseteq Y\cap(J_+\cup J_o),\qquad
R\cap(J_0\cup J_-\cup Z)=\varnothing.
$$

An omitted generator can still be residual. For an explicit example, use
binary vectors $(a,g,a+g,a+g)$ on labels $0,1,2,3$, weights $(1,2,2,2)$,
threshold $2$, $H=\varnothing$, $D=\{0,1,3\}$, $C=\{0\}$, and empty lower
test mask. Here $a,g$ are independent binary vectors. The higher group has
active generator $1$ at auxiliary time $-1$ and projected witness $2$ for
odd parity. In the second stream, witness $2$ followed by old label $0$
spans generator $1$, so its occurrence is omitted but its last support
pivot is positive. Label $1$ is residual. The finite verifier checks this
actual density path, so the overlap charge on $J_o$ cannot simply be removed.

### Joint mask law and restricted overlap

Put $O=D\cup C$, $p=\rho+(1-\rho)t$, and $\lambda=-\log p$. Fix disjoint
label sets $J_0,J_+,J_-,J_o,Z$, with $Z\subseteq Y\cap U$, and put
$J=J_0\cup J_+\cup J_-\cup J_o$. Restrict the fixed family of residuals
to those obeying the support exclusions above; every actual residual is
still included. For each fixed candidate $R\subseteq(Y\cap U)\setminus Z$,
the independent focal mask pairs give

$$
\begin{aligned}
&\Pr(J\subseteq D,\ Z\cap O=\varnothing,\ R\subseteq O)\\
&\quad=\rho^{|J|}(1-p)^z p^{|R\setminus J|}\\
&\quad\le\rho^{|J|}(1-p)^z p^{|R|-|(J_+\cup J_o)\cap Y|}.
\end{aligned}
$$

The potentially overlapping states retain their full correction $1/p$.
This is a fixed-family calculation before focal bits are exposed; it
asserts no independence for the eventual adaptively selected sets.

Choose $\mu>1/4$, $\nu>0$, and $0<u,w,v<1$ satisfying

$$
\rho\left(p^{\mu-1/4}+\frac{3p^\mu}{v}\right)\le u,
\qquad \frac{(1-p)p^\nu}{v}\le w.
$$

Write the generating weights as

$$
\alpha_0=\rho p^{\mu-1/4},\qquad
\alpha_1=\rho p^\mu/v,\qquad \omega=(1-p)p^\nu/v.
$$

On listed outcomes let $e=(|R|-(\mu-1/4)j_0-\mu j_1-\nu z)_+$;
otherwise set $e=0$. For $x\ge0$, apply the preceding joint probability
bound to each fixed member with positive excess above $x$. The arrangement
bound and $v^dS_d(2y)\le(1+v)^{2y}$ assign one factor $1/v$ to each active
generator and witness. The disjoint label roles have total weight
$1+\alpha_0+3\alpha_1$ outside $Y$ and
$1+\alpha_0+\alpha_1+2\alpha_1/p+\omega$ inside $Y$. Thus a union bound gives

$$
\begin{gathered}
\Pr(e>x)\le\min\{1,Mp^x\},\\
M\le(1+\alpha_0+3\alpha_1)^{n-y}
(1+\alpha_0+\alpha_1+2\alpha_1/p+\omega)^y(1+v)^{2y}.
\end{gathered}
$$

The tilts imply $\alpha_0+3\alpha_1\le u$, $\alpha_1\le u/3$, and
$\omega\le w$. Hence we may take the deterministic upper bound

$$
M_*= (1+u)^{n-y}
\left(1+u+\frac23u(1/p-1)+w\right)^y(1+v)^{2y}\ge1.
$$

Integrating $\min\{1,M_*p^x\}$ gives
$\mathbb E e\le(\log M_*+1)/\lambda$. For any $0<d\le\lambda$, the
inequalities $p\ge\rho$ and $\log(1+x)\le x$ imply the rational interface

$$
\mathbb E e\le\frac{n u+y b_Y+1}{d},\qquad
b_Y=\frac{\frac23u(1/\rho-1)+w}{1+u}+2v.
$$

The previous coefficient $1$ on $u(1/\rho-1)$ has become $2/3$, and
the active-generator tilt uses $3$ instead of $4$. The additive term remains.

### Carry the refinement through the final guarantee

The residual comparison and definition of $e$ give, pointwise,

$$
\sigma+j_0/4\le(\kappa+\nu)z+\mu(j_0+j_1)+e.
$$

Take expectations, cancel the activation quarter charge against the
conditional safety estimate, and use the generator budget. The full
nominal rank is at least the projected rank, giving

$$
\begin{gathered}
\mathbb E[z_{\rm full}\mid H]\ge
\frac{\bar\gamma y-\epsilon n-a_0}{K},\\
K=\kappa+\nu,\quad\bar\gamma=\rho/4-b_Y/d,\quad
\epsilon=\mu\rho/\kappa+u/d,\quad a_0=1/d.
\end{gathered}
$$

The projected witnesses use no focal test bits. The unchanged thinning and
rank-cost argument therefore applies, with both later costs retained:

$$
L_0=\epsilon+Kt+\frac{Kt+K\rho/\kappa}{B-1},\qquad
s=(1-h)(\bar\gamma-L_0/h),\qquad\beta=(B-1)/B.
$$

Small groups and the additive term cost at most
$t(\bar\gamma\kappa+a_0)m_*/K$. The maximum branch pays them when
$(1-t)(\bar\gamma\kappa+a_0)/K\le1/4$. The shared finite phase average gives

$$
C=\frac{(1-t)\beta^2 t s}{L(\theta-1)K}.
$$

All order minima stay inside seed expectations. The lossless sample/value
simulation preserves the adversary's access to ignored samples, sacrificed
values, and unused seed bits.

### Exact parameters, resources, and limitations

Use the algorithm parameters

$$
\begin{gathered}
\kappa=164,\quad\rho=93/256,\quad h=3/4,\quad t=23/2^{18},\\
\theta=261/256,\quad L=256,\quad B=\theta^L,\quad p_{\rm main}=1-t,
\end{gathered}
$$

and analysis parameters

$$
\begin{gathered}
\mu=105/8,\quad\mu_0=103/8,\quad\nu=113/8,\quad K=1425/8,\\
u=1/864,\quad w=1/4000,\quad v=1/624,\quad d=253/250.
\end{gathered}
$$

The [exact certificate](../verification/certify_support_refinement.py)
proves $\lambda>d$ with an outward log interval and a separate 20-term
positive atanh sum. Since $p>(3/4)^4$, put $A_*=\rho(3+4v/3)$; exact
rational power comparisons give

$$
A_*^8p^{105}<(uv)^8,\qquad (1-p)^8p^{113}<(wv)^8.
$$

These prove the two tilts; separate log intervals cross-check them. The
certificate also checks $B>140$, $L(\theta-1)=5$, maximum-branch cancellation,
and the following rational bounds:

$$
\begin{gathered}
\bar\gamma=\frac{69959099203}{812800834560},\qquad
\epsilon=\frac{69328715}{2294341632},\quad a_0=250/253,\\
s>\frac{4874403782709953}{928041574520586240}>0.
\end{gathered}
$$

Replacing $\beta$ by $139/140$ and $B-1$ by $139$ in the final expression
gives $C>C_5$, where

$$
C_5=\frac{4084754449786906742230661}
{8009094702029267287249256448000000}
>\frac{35}{32}\,2^{-31}.
$$

This conservative coefficient is approximately $5.10014502482\times10^{-10}$,
or $1.07104403012$ times the preceding exact $C_4$: a $7.1044\%$ increase.
It remains below $2^{-30}$. The verifier reruns the preceding certificate
before the exact comparison. No global optimum or next-threshold claim is made.

The masks require $2+8+18+18+1=47$ fair bits per label, and the shared phase,
branch, and parity require $8+18+1=27$ bits. This increases the initial seed
from $40N+26$ to $47N+27$. No extra sample or optimum access is introduced.
Exact observations, unbounded level indices, and potentially exponential
preprocessing and storage remain allowed.

The [finite checker](../verification/check_support_refinement.py) checks
compressed support signs on actual paths, conditional activation safety,
restricted-overlap probabilities, generating products, and adaptive tails.
It includes the omitted-but-residual generator example. Small thresholds
exercise transitions that threshold $164$ would hide on small matroids.
These finite facts do not prove the universal theorem.

The [numerical search](../experiments/search_support_refinement.py) uses
24 deterministic starts in four modes: the preceding formula, overlap
exclusions, three-state compression, and a proposed removal of forced
pivot tests. The fourth mode is numerical evidence only and is excluded
from this proof and certificate. None of the searches proves a ceiling.

See the [same-agent audit](../proofs/support_refinement_audit.md) and
[October 11 baseline refresh](../verification/support_baseline_audit.json).
Independent review and formalization remain pending; no priority or
confirmed strongest-known-bound claim is made.
