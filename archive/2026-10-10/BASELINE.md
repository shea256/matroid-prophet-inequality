# Baseline audit — October 10, 2026

**The strongest same-model guarantee found in an accessible primary manuscript
is `2^-293`, not the advertised `2^-310`. A stronger `2^-47` announcement is
known but its proof and assumptions have not been located. Consequently this
audit does not establish the strongest current result overall.**

## Versioned primary source

Started from [OpenAI's manuscript index](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/CONTENTS.md).
Family 111 lists one manuscript:
[One Sample Suffices for Matroid Prophet Inequalities against an Almighty Adversary](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/One-Sample-Suffices-for-Matroid-Prophet-Inequalities-against-an-Almighty-Adversary-September-23-2026/final.pdf),
nominally dated September 23, 2026. The complete seven-section TeX argument and
bibliography were retrieved and read. The secretary consequence is in its last
section, rather than a separately listed companion manuscript.

Pinned repository commit: `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`,
committed October 8, 2026 at 05:20 UTC. The initial release was
`adc7f1241b42e322a6451854ab7e4b4c146bf78a`, October 6 at 21:58:50 UTC.
The [source manifest](verification/source_manifest.json) records byte lengths,
SHA-256 hashes, and immutable download URLs. Source PDFs and full source texts
are cached under the gitignored `.context/111-sources/` rather than committed.

### Exact theorem and resources

For every finite known labeled matroid `M`, there is a measurable online rule
and a finite seed law depending only on `M`. For every collection of mutually
independent nonnegative random variables `(S_e,V_e)` with identical laws at
each sample/value pair, and every independent seed with that law, assume only
`E OPT_M(V)<infinity`. For every measurable permutation depending on all
samples, online values, and the full seed, the rule makes irrevocable decisions,
is independent after every prefix, and obtains expected reward at least
`2^-310 E OPT_M(V)` in the headline theorem. The rule has no value-distribution
description and receives one sample per label. No polynomial running-time or
oracle-query bound is claimed. Exact real observations and measurable decisions
are used, not a uniform bounded-precision computational model.

The end of [accounting.tex](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/One-Sample-Suffices-for-Matroid-Prophet-Inequalities-against-an-Almighty-Adversary-September-23-2026/build/sections/accounting.tex)
actually derives `2^-293`. The introduction explicitly notes this stronger
constant. [The simulation lemma](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/One-Sample-Suffices-for-Matroid-Prophet-Inequalities-against-an-Almighty-Adversary-September-23-2026/build/sections/setup.tex)
preserves the ratio exactly, including the minimum over orders inside the
expectation. The 17-bit difference is announced-statement slack, not a loss in
the reduction and not an improvement available to claim as new.

The hidden-vector theorem fixes the weights before drawing the seed, reveals
and sacrifices a mask determined by that seed, and guarantees
`E_R min_pi reward(w,R,pi) >= 2^-293 OPT(w)`.
The secretary consequence has a random rejected prefix followed by a suffix
that may be reordered after the adversary sees the prefix and full seed, with
the same ratio. None of these statements permits choosing the fixed weights
after observing the seed.

### Verification stage

The repository supplies Lean solution modules as well as comparator statements.
The comparator `MatroidProphet.lean` contains the expected challenge `sorry`;
this is not the implementation. Its JSON points to
`OAI.Probability.MatroidProphet.Main`, whose retrieved source includes the proof
of `complete_hidden_guarantee` at `2^-293`. The public one-sample challenge uses
`2^-310`. The formalization scope note also advertises `2^-310` for the prophet
statement and `2^-293` for hidden-vector selection.

This run inspected the main proof source, constants source, comparator
statements and metadata. **It did not build the Lean project or audit every
imported proof file.** The new parameter proof has no Lean formalization.
Repository-provided formalization, a manuscript argument, local arithmetic
verification, and an independently compiled proof are different evidence stages.

## Quantitative dependency map

All rows refer to the pinned source, with labels matching its TeX.

| Component | Source argument | Original loss or bound |
|---|---|---|
| Rounding | `eq:rounding` | `B=2^32`, rounded optimum at least `OPT/B` |
| Candidate filter | `lem:filter` | `E u(Y)=W/2`, `E u(U)<=W` |
| Density charge | `lem:density`, `lem:generators` | `kappa=2^100`; entire path uses at most `|D_h|/kappa` generators |
| Masks | algorithm section | `H:1/2`, `D:1/4`, `C:T:t=2^-140` |
| Exit bound | `lem:exit` | `eta=2^-12`; squared exit mass at least `eta/2` |
| Safety | `lem:safe` | parity `1/2`, baseline-birth penalty at most `|D_h|/(2kappa)` before relaxation |
| Average sample count | `eq:averaged-safe-count` | `gamma=eta/16=2^-16`; penalty subsequently relaxed to `n/kappa` |
| Residual family | `eq:raw-pattern-count` | `S_q(n)^2 (4^(2q) S_(2q)(n))^2`, `q=floor(n/kappa)` |
| Entropy relaxation | proof of `lem:pattern-family` | `(6 log kappa+6+4 log 2)n/kappa`, then relaxed to `1000 log kappa n/kappa` |
| Residual tail | `eq:residual-tail` | `delta=2^-26`; error at most `2^-25 n` for `n>=kappa` |
| Rank transfer | `lem:transfer` | `E z_i >= (gamma |Y_i|-2^-23 n_i)/kappa` |
| Later path expansions | `lem:rank-cost` | one common generator budget; exact `D` contribution `1/(4kappa)` relaxed to `1/kappa` |
| Eligibility | `lem:thinning` | independent thinning factor `t` |
| Summing levels | `eq:minimum-before-expectation` | uses `1/2` although `(B-1)/B` suffices |
| Total group error | `eq:error-constant` | `2^-23+t kappa+(1+t kappa)/(B-1)<2^-21` |
| Small groups | `eq:small-groups` | discarded mass `<2 kappa m*` |
| Main/maximum split | final accounting | main handles `m*<=W/(8kappa)`; fair branch mixture gives `t gamma W/(32kappa)` |
| Final coefficient | final accounting | `t gamma/(32 kappa B)=2^-293` |
| One-sample transfer | `lem:simulation` | no loss |

## Recent related primary sources

| Source and checked version | Relevant claim | Comparison with #111 |
|---|---|---|
| [Abdi–Banihashem–Hajiaghayi–Mittal, arXiv:2609.19118v1](https://arxiv.org/html/2609.19118v1), September 16, 2026, Theorem 1.3 | `1/2` single-sample prophet ratio, `O(n^2)` independence queries | Arrival order fixed independently of samples and values; does not supply a full-seed almighty guarantee |
| [Singla, arXiv:2609.14555v2](https://arxiv.org/html/2609.14555v2), September 29, 2026 | Random-order matroid secretary; v1's announced `1/8` single-sample application is omitted in v2 in light of ABHM | The v1 statement used a known adversarial order; not the adaptive order in #111 |
| [Huang, arXiv:2609.30421](https://arxiv.org/abs/2609.30421), September 24, 2026 | Strong ordinary matroid secretary result | Uniform random arrivals throughout; no automatic transfer to an almighty suffix |
| [Feldman–Svensson–Zenklusen, arXiv:2507.09507](https://arxiv.org/abs/2507.09507), SODA 2026 | `1/4-epsilon` prophet ratio with a sample budget growing with size/rank | Same strong adversary is relevant, but more than one sample is used |
| [Chawla–Dang, arXiv:2610.03660v1](https://arxiv.org/abs/2610.03660v1), October 2, 2026 | Single-sample combinatorial allocation via supporting prices | Checked for relevance; not a stated replacement for arbitrary-matroid one-sample selection in #111's model |

These papers are comparators, not premises of the new proof. This run checked
the directly relevant statements and model restrictions; it did not independently
validate all their proofs. In particular, a large ratio with a different sample
budget or adversary is not an improvement to this track's theorem.

## The `2^-47` announcement and repository history

The user supplied [Daniel's post](https://x.com/firsttimelifer/status/2108282829809541468).
X's public oEmbed endpoint confirms the October 8, 2026 announcement of an
improvement from `2^-310` to `2^-47`. The accessed post contains no manuscript
link, proof, parameters, or explicit adversary assumptions. A public mirror
also returned the same text without a linked artifact. Searches did not locate
a supporting proof. **The claim is unverified here, not refuted or dismissed.**
It is numerically stronger than our `2^-63` candidate, by `2^16` relative to
the simplified constants.

At the user's suggestion, the full public `main` commit history was checked
through the GitHub API. It had three commits: the October 6 initial release,
the October 8 update commit, and its merge. Path histories for the #111 paper,
the scope note, and both `MatroidProphet` and `MatroidSecretary` solution
directories showed only the initial release. Initial/current SHA-256 comparisons
of the PDF, accounting TeX, constants Lean file, and scope note were identical;
see [history_check.json](verification/history_check.json). The
[update log](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/history.md)
does not identify an update to #111. Thus the `2^-47` post does not report a
merged change to these #111 sources as of this check. Its intended provenance
remains unknown; it could refer to separate unpublished work.

Searches included the exact manuscript title, corrections, recent matroid
prophet follow-ups, and X announcements. Ordinary search failed to surface
Daniel's post before the user supplied it. No exhaustive priority search is
claimed. Missing proof access prevents a verified strongest-current-baseline
claim and prevents calling our current result a confirmed advance over SOTA.

## Historical project notes

The provenance notice, matrix-profile obstruction, and attention-probe notes
were inspected. They concern different objects and computational models; no
lemma was transferred. Separate #109/#130 problem directories were not present
in this checkout. None of those exploratory materials is used as a premise.
