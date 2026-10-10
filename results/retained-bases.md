## Retained bases and projected residuals

The [shared framework](../paper/framework.md) supplies the construction,
quadratic safety estimate, two marked streams, joint affine representation,
and order-uniform accounting. We improve the residual count, retain its
fixed tail error as an additive term, and restrict the witnesses and tested
labels to the comparison optimum. Only the algorithm's parameters change;
the comparison optimum remains an analysis object.

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

### Weighted entropy and the additive error

Put $p=\rho+(1-\rho)t$, $\lambda=-\log p$, and choose penalties $\mu,\nu>0$
and tilts $0<u,w,v<1$ with

$$
6e^{-\lambda\mu}/v\le u,\qquad e^{-\lambda\nu}/v\le w.
$$

For every integer $d\ge0$, $v^dS_d(2y)\le(1+v)^{2y}$, because
$v^d\le v^i$ for $i\le d$ and the binomial expansion bounds the sum.
The binomial theorem therefore gives

$$
\begin{aligned}
\sum_{j=0}^n\sum_{z'=0}^y|\mathcal F_{j,z'}|
 e^{-\lambda(\mu j+\nu z')}
&\le(1+u)^n(1+w)^y(1+v)^{2y}\\
&\le\exp\bigl(n\,u+y(w+2v)\bigr).
\end{aligned}
$$

On listed outcomes set $e=(|R_Y|-\mu j-\nu z')_+$ and set
$e=0$ otherwise. Each fixed family member has containment probability
$\Pr(R\subseteq O)=p^{|R|}$ under the original product law. Taking a union
over all fixed families handles the mask-dependent selection and gives

$$
\Pr(e>x)\le\min\{1,\exp(n\,u+y(w+2v)-\lambda x)\},\qquad
\mathbb E e\le\frac{n\,u+y(w+2v)+1}{\lambda}.
$$

The integral splits at $[n\,u+y(w+2v)]/\lambda$. We keep its constant
$1/\lambda$ additive. No probability for $J\subseteq D$ is multiplied into
the containment bound, since those sets could overlap.

The projected residual comparison and generator budget imply pointwise

$$
\sigma\le(\kappa+\nu)z'+\frac\mu\kappa|D\cap U|+e.
$$

On unlisted outcomes $\sigma=z'=e=0$, so this inequality still holds.
Average the tail bound and then use the quadratic safety estimate, averaged
over parity. For any $0<d\le\lambda$, the framework's rank interface holds
with

$$
K=\kappa+\nu,\qquad
\bar\gamma=\rho/4-(w+2v)/d,\qquad
\epsilon=\frac\rho{2\kappa}+\frac{\mu\rho}{\kappa}+u/d,
\qquad a_0=1/d.
$$

We require $\bar\gamma>0$. The tail bound holds for each parity and outside
mask; the safety estimate is used only after averaging those conditions.
The framework carries both changed cost factors, $Kt$ and $K\rho/\kappa$,
and charges the additive term through the geometric weight sum. Its maximum
branch cancels the combined loss precisely when

$$
(1-t)(\bar\gamma\kappa+a_0)/K\le1/4.
$$

This additional condition is essential. Dropping the constant without
charging it would be invalid. The order minimum remains inside all seed
expectations, including branch and phase, and the original lossless
one-sample simulation still applies.

### Parameters and final coefficient

Choose the algorithmic parameters

$$
\kappa=192,\quad\rho=3/8,\quad h=3/4,\quad t=21/2^{18},\qquad
\theta=261/256,\quad L=256,\quad p_{\rm main}=1-t,
$$

and analysis constants

$$
\begin{gathered}
\mu=119/8,\quad\nu=243/16,\quad K=3315/16,\\
u=1/512,\quad w=1/4096,\quad v=1/704,\quad d=49/50.
\end{gathered}
$$

The [exact certificate](../verification/certify_retained_basis.py) verifies
$\lambda>d$, both tilt inequalities, and $B>140$ using outward rational log
intervals. Separate exact power comparisons,

$$
6^8p^{119}<(uv)^8,\qquad p^{243}<(wv)^{16},
$$

verify the same tilts. A separate 20-term positive atanh sum checks the decay
lower bound without range reduction. Using the rounded $49/50$ alone for the
first tilt would fail; it is used only in the error accounting.

Direct substitution gives

$$
\bar\gamma=\frac{100013}{1103872},\qquad
\epsilon=\frac{6427}{200704},\qquad a_0=\frac{50}{49},\qquad
s>\frac{1280616385}{235681087488}>0.
$$

Use $\beta>139/140$, $B-1>139$, and $L(\theta-1)=5$ in the framework's final
coefficient. The maximum-branch condition holds, and the coefficient exceeds

$$
C_3=\frac{548933908320757}{1325382348737372749824000}
>\frac74\,2^{-32}.
$$

This is approximately $4.14170227062\times10^{-10}$, or $1.71459364062$ times
the preceding exact $C_2$: a $71.46\%$ increase in the guaranteed fraction.
It remains below $2^{-31}$. It is approximately $27.35368$ times the earlier
announced $C_0$ certificate above $2^{-36}$. These compare guarantees, not
measured performance. The certificate separately reconstructs $C_2$ before
comparing it.

All probabilities are dyadic. The seed uses $2+3+18+18+1=42$ fair bits per
label and $8+18+1=27$ shared bits, compared with the previous $36n+23$ total.
Every bit is drawn initially, including unused-branch randomness. The new
witnesses, tilts, and penalties are analysis devices; they require no access
to the optimum, additional samples, or algorithmic work. The shared exact-real
and potentially exponential preprocessing/storage model is unchanged.

### Verification and review

The [numerical search](../experiments/search_retained_basis.py) uses 16
deterministic starts per cumulative mode. Its best floating multiple of
$2^{-32}$ was about $1.78594$; the certified coefficient is about $1.77885$.
No global optimum or ceiling is established.

The [finite checker](../verification/check_retained_basis.py) tests 74,881
interleavings over all 92 labeled matroids through four elements, with up to
two movable occurrences and forward/reverse old orders. It checks 3,349
basis-family bounds and 45,824 projected encodings/charges on 170 small
matroid-weight instances. Actual paths use threshold 2, an empty filter mask,
and stress penalties, with omitted second generators, strict rank/projection
savings, adaptive containment tails, and an additive-error negative control.
These checks do not prove the universal statements for arbitrary matroids.

The [same-agent audit](../proofs/retained_basis_audit.md) records the proof
obligations. Independent mathematical review and formalization remain pending.
The source refresh and comparison limits are recorded in [BASELINE](../BASELINE.md).
