## The fixed-vector rule and its statistics

Fix a nonnegative hidden vector $w$ before any seed bits. The rule reveals and
sacrifices a seed-chosen mask and must handle every permutation; its target is
$\mathbb{E}_R\min_\pi w(A(w,R,\pi))$ . Write
$\operatorname{r}(A\mid P)=\operatorname{r}(A\cup P)-\operatorname{r}(P)$ and
$F_{\varnothing}=\operatorname{cl}(\varnothing)$ . Fix a label order for every tie.
Higher rounded weight means higher priority. Put $W=\operatorname{OPT}_M(u)$ and let
$I^*$ be priority greedy on the full rounded vector.

Let $\kappa\ge4$ , $0<h,\rho,t<1$ , integer $L\ge1$ , and $\theta>1$ be fixed parameters
supplied by the selected result. The independent masks $H,D,C,T$ have rates $h,\rho,t,t$
respectively. The main branch has probability $1-t$ ; parity is fair. Choose a uniform
shared phase $J\in\{0,\ldots,L-1\}$ , set $B=\theta^L$ , and define

$$
u_J(x)=\theta^J B^{\lfloor\log_B(x/\theta^J)\rfloor}\quad(x>0),\qquad u_J(0)=0.
$$

All random choices are made initially. Each result supplies exact dyadic mask
probabilities and a finite fair-bit implementation. The score variables in the counting
proof below are analysis devices, not algorithmic inputs.

The maximum branch reveals a separate fair mask and accepts the first unmasked positive
nonloop with priority above every revealed positive nonloop. An empty threshold is below
every positive nonloop. If $m_*$ is the largest rounded nonloop weight, expected
worst-order reward is at least $m_*/4$ : the largest-priority nonloop is unmasked and
the second is masked with probability $1/4$ . With only one positive nonloop success has
probability $1/2$ ; with none the bound is zero.

In the main branch reveal and sacrifice $H\cup D\cup C$ . Define

$$
U=\{e\notin H:u_e>0,\ e\notin\operatorname{cl}(H_{>e})\},\qquad Y=I^*\setminus H.
$$

The candidate test uses only revealed $H$ values and the tested value. For a fixed phase
divide weights by $\theta^J$ , so true groups $U_i$ have weight $B^i$ . List those
meeting $D$ in increasing weight order as $G_1,\ldots,G_m$ ; put $D_j=D\cap G_j$ , and
similarly $C_j,T_j$ . The full groups are analysis objects; their revealed $D_j,C_j$
parts suffice for preparation. If there are no listed groups, reject all.

For a flat $P$ , let $Q_j(P)$ be the largest flat $Z\supseteq P$ maximizing
$|D_j\cap Z|-\kappa\operatorname{r}(Z)$ . Take closure first for nonflat arguments. Set
$a_j=-3j$ and enable $Q_{j,k}=Q_j$ for $k\ge a_j$ , with the identity earlier. Starting
from $F_0(k)=F_{\varnothing}$ for $k<0$ and $E$ otherwise, define

$$
X_j(k)=Q_{j,k}(F_{j-1}(k)),\qquad
 F_j(k)=\operatorname{cl}(X_j(k)\cup(C_j\cap X_j(k+1))).
$$

Compute paths in increasing $j$ on the finite relevant auxiliary timeline, and put
$\widehat F=F_m$ . For a candidate nonloop in listed group $j$ , write
$b_j(e)=\min\{k:e\in X_j(k)\}$ . It is eligible precisely when it is unsacrificed, $T$
-positive, has birth $b\ge a_j+2$ of the chosen parity, and lies outside
$\widehat F(b-2)$ . At endpoint $b$ maintain a set $A_b$ ; accept an eligible $e$
exactly when $\operatorname{r}(\{e\}\mid\widehat F(b-2)\cup A_b)=1$ .

The source density and path lemmas give

$$
F_{j-1}(k)\subseteq X_j(k)\subseteq F_j(k)\subseteq X_j(k+1),\qquad
 |D_j\cap(\operatorname{cl}(Q_j(P)\cup Z)\setminus Q_j(P))|\le\kappa\operatorname{r}(Z\mid Q_j(P)).
$$

Nonloops are born at $a_j$ or in $[a_j+2,0]$ , and the entire nominal path uses a
generator set of size at most $|D_j|/\kappa$ . The nested layer bases give prefix
independence. Finite rank operations, fixed tie rules, and countably many rounding
levels give measurability. These structural facts are inherited from the cited source.

For valid selected-parity endpoints $a_j+2\le b\le0$ , define

$$
\begin{aligned}
 K_{j,b}&=\bigcup_{\ell<j}(T_\ell\cap(X_\ell(b)\setminus X_\ell(b-1))),\\
 P_{j,b}&=G_j\cap(X_j(b)\setminus X_j(b-1)),\quad
 O=D\cup C,\quad S_{j,b}=P_{j,b}\setminus O,\\
 z_j&=\sum_b\operatorname{r}(S_{j,b}\mid X_j(b-2)\cup K_{j,b}),\\
 \lambda_j&=\sum_b\operatorname{r}(T_j\cap S_{j,b}\mid\widehat F(b-2)\cup K_{j,b}).
 \end{aligned}
$$

The safe count $\sigma_j$ counts $d\in D_j\cap Y$ with such a birth and
$d\notin Q_j(F_{j-1}(b-2)\cup K_{j,b})$ . For each nominal summand choose a fixed-order
basis extension $Z_b$ , so $\sum_b|Z_b|=z_j$ . The residual is

$$
\mathcal R_j=\bigcup_b\left(P_{j,b}\setminus
 \operatorname{cl}(X_j(b-2)\cup K_{j,b}\cup Z_b)\right)\subseteq O.
$$

Extend $\sigma_i,z_i,\lambda_i$ by zero on unlisted true groups. The source density
argument gives $\sigma_j\le\kappa z_j+|\mathcal R_j|$ . Its order-uniform lemma bounds
the number of accepts of weight at least that of $G_j$ below by $\lambda_j$ , for every
seed and order. One later-path generator budget over the whole timeline is

$$
c_j=|C_j|+\sum_{\ell>j}(|C_\ell|+|D_\ell|/\kappa).
$$

Conditional on $H,D,C$ , parity, and test bits outside the focal group, independent test
thinning gives $\mathbb{E}[\lambda_j\mid\mathcal F_{-j}] \ge t(z_j-c_j)$ . These are the
source interfaces used below.

## A quadratic transaction inequality

**Quadratic transaction lemma.** Let $\mathcal A$ be an increasing event on finitely
many independent bits, and let a predictable query procedure, reading each bit at most
once, determine whether $\mathcal A$ occurs. Write $p=\mathbb{P}(\mathcal A^c)$ . At the
completed transcript let $q$ be the failure probability with only unqueried bits random
and every queried bit reset to zero. Then

$$
\mathbb{E}[\mathbf 1_{\mathcal A}q^2]\ge p(1-p).
$$

**Proof.** At an intermediate transcript, let $W$ be its remaining coordinates and $I$
its queried positives. Let $m$ be the actual conditional failure probability, and $q$
the failure probability with only $W$ random and all other bits zero. Predictable
product exposure identifies $m$ with the probability when $I$ is forced positive and $W$
is random. Increasingness gives $0\le m\le q\le1$ . Initially $m=q=p$ .

For a predictably chosen next coordinate, the depleted probability $q'$ is determined
before the answer and satisfies $q'\ge q$ . The actual conditional failure probability
is a martingale: $\mathbb{E}[m'\mid\text{transcript}]=m$ . Therefore the potential
$\Phi(q,m)=q^2-2qm$ satisfies

$$
\mathbb{E}[\Phi(q',m')\mid\text{transcript}]-\Phi(q,m)
 =(q'-q)(q'+q-2m)\ge0.
$$

At the end $m=\mathbf 1_{\mathcal A^c}$ , and failure forces $q=1$ . The initial
potential is $-p^2$ ; its final expectation is $\mathbb{E}[\mathbf 1_{\mathcal A}q^2]-p$
. Sum the displayed query identity over the finite number of queries, padding stopped
paths by zeros, to obtain the result. The proof includes $p=0,1$ and transactions
needing no queries.

## The reverse exit hazard

Fix the source's filter and density masks, a listed-group prefix, and a nonloop $d$
still alive before a reverse step. Its current states are $S$ , and its transition is
$\mathcal G_k(c,S)$ . The remaining guard coordinates have their product law. Let
$\mathcal A$ be the increasing event that $d$ survives, and let $p$ be the conditional
exit probability.

For completeness, for $k<0$ the source reverse map on a listed-group prefix is defined
recursively by

$$
A_0=F_{\varnothing},\qquad N_j=Q_{j,k}(A_{j-1}),\qquad
 A_j=\operatorname{cl}(N_j\cup\{e\in G_j\cap S_j:c_e=1\}),
$$

with output $(N_j)_j$ . Starting from $X_j(0)=E$ , reverse steps compute
$X(k)=\mathcal G_k(C,X(k+1))$ . For actual later states, $N_j\subseteq S_j$ for every
fresh bit assignment. After computing $N_j$ , query only $G_j\cap(S_j\setminus N_j)$ ;
omitted additions already lie in $N_j$ . The new remaining domain is
$\bigcup_j(G_j\cap N_j)$ .

The source queries exactly the departing coordinates in predictable batches. Their
answers determine all output states: unqueried bits are inside flats already spanned.
Thus the transcript decides $\mathcal A$ , on both survival and failure, so the
quadratic transaction lemma applies.

Let $S'$ be the actual output and $V'$ the remaining coordinates. For each assignment
$c$ supported on $V'$ , monotonicity in time and state gives

$$
\mathcal G_{k-1}(c,S')\subseteq\mathcal G_k(c,S).
$$

The right side has all just-queried coordinates zero, exactly the depleted experiment
defining $q$ . Conditional on the full post-step transcript, the bits in $V'$ remain
independent. On survival the next hazard $r$ therefore satisfies $r\ge q$ . The states
are frozen in this comparison; earlier states are not recomputed after resetting bits.
No order is conditioned on.

The next alive squared hazard consequently obeys

$$
\mathbb{E}[\mathbf 1_{\rm survive}r^2]-p^2\ge p-2p^2.
$$

Telescope this potential over the deterministic finite reverse horizon. Every nonloop
exits, and if $P$ is its hazard at actual exit, then

$$
-p_{\rm start}^2\ge
 \sum_i\mathbb{E}[\mathbf 1_{\rm alive}p_i]-2\sum_i\mathbb{E}[\mathbf 1_{\rm alive}p_i^2]
 =1-2\mathbb{E}P.
$$

Hence

$$
\boxed{\mathbb{E}P\ge(1+p_{\rm start}^2)/2\ge1/2.}
$$

In particular, the source's total squared-exit mass is at least $1/2$ . Its hybrid
comparison still applies because guard and test rates agree. The same baseline-birth
loss and fair parity give, after averaging a density mask of arbitrary rate $\rho$ ,

$$
\mathbb{E}[\sigma_i\mid H]\ge \gamma|Y_i|-\frac{\rho n_i}{2\kappa},
 \qquad\gamma=\rho/4.
$$

This averages before conditioning on listing, extending the statistics by zero on
unlisted groups.

The bound $1/2$ is sharp for the abstract hypotheses. Take $N$ Bernoulli-$t$ bits and
repeatedly test the OR of the remaining suffix, querying until the first positive or
until that suffix is exhausted. The next hazard equals the depleted current failure
probability. With $a=1-t$ , classification by the last positive (or none) gives

$$
\mathbb{E}P=a^{2N}+t\sum_{j=0}^{N-1}a^{2j}
 =a^{2N}+\frac{1-a^{2N}}{2-t}.
$$

For $t=1/m$ , $N=m^2$ , this tends to $1/2$ . This is an abstract limitation, not a hard
matroid instance or a bound on the best prophet algorithm.

## Joint residual encoding

Fix $H$ , parity, and all mask bits outside a true group $U$ of size $n\ge\kappa$ . Do
not condition on its focal bits or listing. Its incoming path $F(k)$ , competition sets
$K_b$ , index, and activation $a$ are fixed. Write $S_d(N)=\sum_{i=0}^d\binom Ni$ .
Suppose a path has density generators $J$ and rank witnesses $Z$ , of sizes $j,z$ . A
generator has insertion time $\tau(g)\in[a,0]$ , and

$$
X(k)=\operatorname{cl}(F(k)\cup\{g\in J:\tau(g)\le k\}).
$$

The source gives two marked streams. First, list $F(k)$ and then generators inserted at
$k$ , marking the block one exactly when $k$ is a valid endpoint of the chosen parity.
Second, start with the fixed $F(b_0)$ marked zero, where $b_0\in\{a-2,a-1\}$ has that
parity. At each subsequent parity endpoint $b$ , insert $K_b,Z_b$ with mark zero, then
$F(b)$ and generators with $b-2<\tau(g)\le b$ with mark one. End at $b_1\in\{0,1\}$ of
that parity; set $K_b=Z_b=\varnothing$ at invalid endpoints.

The second stream has intermediate span $\operatorname{cl}(X(b-2)\cup K_b\cup Z_b)$ and
endpoint span $X(b)$ , since $K_b\subseteq F(b)$ and $Z_b\subseteq X(b)$ . The first
test selects valid births. For a label passing it, the second pivot lies in the same
layer and has mark one exactly on the residual. Thus the intersection of the two
mark-one sets is the residual.

**Joint pivot lemma.** For fixed $J,Z$ , the number of residuals obtained from these
linked streams is at most $3^j4^{2j+z}S_{j+z}(2n)$ .

**Proof.** The source marked-pivot argument first bounds retained greedy bases of
occurrences by $4^s$ when $s$ specified movable occurrences are inserted into an old
sequence spanning the matroid. To recall why, old-only greedy gives an ordered basis.
Only at most $s$ of its positions can be omitted after insertions: their
conditional-rank drops for the full movable set sum to at most $s$ . There are at most
$2^s$ choices of omitted old occurrences and $2^s$ of retained movable occurrences.
Apply this to the two streams with $s=j$ and $s=j+z$ , giving $4^{2j+z}$ pairs of
retained bases. Fix a pair. Each nonloop has a unique minimal support in each basis, by
matroid submodularity, and its pivot is the last support member.

We represent both streams by the same $j+z$ variables. Label the entire ground set
$0,\ldots,N-1$ , put $m=N+1$ , $T=8m$ , and $u_k=(k-a+2)T$ . Give old $F(k)$ occurrences
in the first stream absolute scores $2^{u_k+4m+e}$ , with sign equal to their fixed
marks. In the second stream, the initial $F(b_0)$ has negative scores
$-2^{u_{b_0}+4m+e}$ ; $K_b$ has scores $-2^{u_b+e}$ ; and $F(b)$ has scores
$2^{u_b+4m+e}$ . These are fixed before the focal masks.

Give each generator a variable $x_g=2^{u_{\tau(g)}+6m+g}$ . Its first score is
$\eta_gx_g$ , positive exactly at a valid endpoint. Its second score is $d_gx_g$ , where
$d_g=1$ for the chosen parity and $d_g=2^T$ otherwise. Multiplication by $2^T$ moves an
insertion from $b-1$ into the endpoint $b$ block. Give each witness $e\in Z_b$ a
variable $y_e=2^{u_b+2m+e}$ , used only as the score $-y_e$ in the second stream. There
are only three types for a generator:

$$
(\eta_g,d_g)\in\{(1,1),(-1,1),(-1,2^T)\}.
$$

The middle type includes early insertions of the chosen parity that are not valid
births. Fix all types, at a cost of at most $3^j$ choices. Order every block by label.
Second-stream generators can be reordered within their endpoint block because all have
mark one; this preserves pivot marks and endpoint spans, and all retained bases are
already counted.

In each stream the absolute scores are distinct powers of two in occurrence order. Every
score dominates the sum of its predecessors. The sign of the sum over a support
therefore equals its last member's mark. For fixed bases and types these are $2n$ affine
functions of the same $j+z$ variables. Every realized mark pair is a strict sign
pattern. The hyperplane-region bound gives at most $S_{j+z}(2n)$ patterns, proving the
claim. Ground-set size and timeline length affect coefficients, not this dimension
bound.

## From a rank estimate to the final guarantee

Earlier versions use $a_0=0$ and $\bar\gamma=\rho/4$. The current refinement
keeps a fixed additive error and pays for it with the maximum branch.

The selected result must supply constants $K>0$, $\epsilon,a_0\ge0$, and
$0<\bar\gamma\le\rho/4$ such that, for each
true group of size $n_i\ge\kappa$ ,

$$
\mathbb E[z_i\mid H]\ge\frac{\bar\gamma|Y_i|-\epsilon n_i-a_0}{K}.
$$

The source's later-path cost, including unlisted groups by domination, obeys

$$
\mathbb E[c_i\mid H]\le t n_i+(t+\rho/\kappa)\sum_{j>i}n_j.
$$

Independent focal test thinning therefore gives

$$
\mathbb E[\lambda_i\mid H]\ge\frac tK\left[
\bar\gamma|Y_i|-(\epsilon+Kt)n_i-
(Kt+K\rho/\kappa)\sum_{j>i}n_j-a_0\right].
$$

Both changed cost factors are essential when $K\ne\kappa$ . For general filter rate $h$
, the source filter argument gives

$$
\mathbb E_H u(Y)=(1-h)W,\qquad
\mathbb E_H u(U)=\frac{1-h}{h}\mathbb E_Hu(\operatorname{greedy}(H))
\le\frac{1-h}{h}W.
$$

To verify the identity, condition on memberships preceding each label in rounded
priority. Its span test is fixed. The candidate and sample-greedy probabilities are
respectively $1-h$ and $h$ times this test; sum their weighted contributions. The
comparison set $Y$ remains independent and contained in $U$ .

Set $\beta=(B-1)/B$ and

$$
L_0=\epsilon+Kt+\frac{Kt+K\rho/\kappa}{B-1},\qquad
s=(1-h)(\bar\gamma-L_0/h).
$$

For every fixed seed and arrival permutation, the source order-uniform rank bound
implies that the number accepted at weight at least $B^i$ is at least $\lambda_i$ . An
accepted weight $B^\ell$ contributes at most $\sum_{i\le\ell}B^i=B^\ell/\beta$ to this
cumulative sum. Consequently

$$
\min_\pi u(A_{\mathrm{main}}(R,\pi))
\ge\beta\sum_{i:n_i\ge\kappa}B^i\lambda_i.
$$

The weighted higher-group cost is at most $u(U)/(B-1)$ . Discarding groups smaller than
$\kappa$ loses comparison mass at most $\kappa m_*/\beta$ , where $m_*$ is the largest
rounded nonloop weight. The geometric sum of the weights of analyzed groups
is at most $m_*/\beta$, so their additive errors contribute at most
$t a_0m_*/K$. Applying the filter identities yields

$$
\mathbb E_R\min_\pi\mathrm{reward}_{\mathrm{main}}
\ge\frac{\beta t s}{K}W-\frac{t(\bar\gamma\kappa+a_0)}{K}m_*.
$$

If $(1-t)t(\bar\gamma\kappa+a_0)/K\le t/4$ , the maximum branch cancels the negative term. This
condition is checked by the selected result's exact certificate. For positive $x$ , let
$k=\lfloor\log_\theta x\rfloor$ . Across the $L$ phases its rounded values are
$\theta^{k-r}$ , once each for $r=0,\ldots,L-1$ . Since $\theta^k\ge x/\theta$ , the
geometric sum gives

$$
\mathbb E_Ju_J(x)\ge\frac{\beta}{L(\theta-1)}x.
$$

Apply this to one fixed true optimal independent set to obtain the same factor for the
rounded optimum. Thus, provided $s>0$ , the coefficient is

$$
C=\frac{(1-t)\beta^2 t s}{L(\theta-1)K}.
$$

The minimum over permutations remains inside the seed expectation at every stage,
including phase and branch. The source's glued-vector simulation reveals and sacrifices
the mask fixed by the seed, using the sample there and the online value elsewhere.
Conditional on the entire seed this glued vector has the original product value law, so
it is independent of the seed. Ignored samples, sacrificed values, and unused coins may
still inform the adversary's chosen permutation; the pointwise minimum covers them all.

## Resources and proof dependencies

The rule uses a known finite labeled matroid, independent nonnegative values and
matching independent samples, and exact observations. Only the expected offline optimum
needs to be finite. Rank/closure tables and flat enumeration may be exponential;
preprocessing and storage are part of the construction. There are finitely many occupied
groups and a finite relevant auxiliary timeline. Observation precision and integer level
indices are unbounded in the original measurable model. For rational inputs, exact power
comparisons have costs depending on bit lengths and exponents. No polynomial complexity
or practical performance claim is made.

The source density, generator, path, feasibility, hybrid safety, thinning, order-uniform
rank, and simulation lemmas remain explicit dependencies. The quadratic and joint pivot
proofs above are this project's written refinements. Exact certificates prove their
scalar assertions, and finite checks test their specified cases. Independent
mathematical review and formalization of these refinements remain pending.
