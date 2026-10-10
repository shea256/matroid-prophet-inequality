# Baseline and primary sources

Audit date: October 10, 2026. Pinned OpenAI/math revision:
`fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`.

The strongest same-model guarantee found in an accessible primary manuscript
is `2^-293`, stronger than the original `2^-310` headline. A `2^-47` public
announcement is known, but its proof and assumptions have not been located.
This audit therefore does not establish the strongest current result overall.

## Source and theorem

- [Pinned manuscript index](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/CONTENTS.md)
- [Original manuscript PDF](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/One-Sample-Suffices-for-Matroid-Prophet-Inequalities-against-an-Almighty-Adversary-September-23-2026/final.pdf)
- [Formalization scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/111.md)
- [Source manifest with exact section URLs and hashes](verification/source_manifest.json)

For every known finite labeled matroid, the source supplies a measurable
distribution-independent rule with one independent sample per label and a
finite seed law. All sample/value coordinates are mutually independent,
nonnegative, and have matching laws at each label. The seed is independent.
Only the expected offline optimum must be finite. Choices are irrevocable
and feasible after every prefix. The arrival permutation may depend measurably
on every sample, value, and seed coordinate, including unused coins.
No polynomial running-time or bounded observation-precision claim is made.

The manuscript's accounting derives
`2^(-140-16-5-100-32)=2^-293`. The sample/value simulation is lossless;
the 17-bit difference from the headline is statement slack, not a reduction
loss that this project can claim to recover.

The complete source TeX sections used by this refinement were inspected.
The source supplies Lean proof modules as well as challenge comparators.
This project has not built the upstream Lean project or formalized the new
proof. Source availability, written proof review, finite certificates, and
an independently reproduced formal proof are separate evidence stages.

## Quantitative interfaces

| Component | Source interface | Change in this paper |
|---|---|---|
| Density/path construction | `lem:density`, `lem:paths`, `lem:generators` | Same structural arguments, smaller threshold |
| Reverse exposure | `eq:reverse-map`, `eq:departing-query` | New quadratic transaction and exit potential |
| Hybrid safety | `eq:hybrid-containment`, `eq:birth-safety-probability` | Same coupling; equal guard/test rates retained |
| Residual encoding | `lem:pivot-patterns`, `lem:pattern-family` | First sequence counted with its actual `q` movable occurrences |
| Residual tail | `eq:residual-tail` | Integrate the entire union-bound tail |
| Candidate filter | `lem:filter` | Rate `3/4`, with both expectation factors recalculated |
| Rank cost | `lem:all-orders`, `lem:rank-cost`, `lem:thinning` | Same deterministic/conditional lemmas; density rate `5/8` charged exactly |
| Rounding and branches | Source geometric levels and maximum branch | 64 rational phases and affine mixture |
| One-sample simulation | `lem:simulation` | Same lossless full-seed reduction |

## Related work and comparison limits

[Daniel's announcement](https://x.com/firsttimelifer/status/2108282829809541468)
claims an improvement from `2^-310` to `2^-47`. The accessed first-party
oEmbed record contains no proof or artifact link. Its text and audit date
are recorded in [announcement.json](verification/announcement.json).
Searches did not locate a supporting manuscript. The claim is unverified
here, not refuted. Relevant OpenAI #111 files were unchanged from their
initial release in the checked source history; the latest main revision
was checked again during preparation.

The larger constant in [Abdi–Banihashem–Hajiaghayi–Mittal,
arXiv:2609.19118v1](https://arxiv.org/html/2609.19118v1) concerns an arrival
order fixed independently of samples and values. It does not supply this
paper's almighty-order quantifier. Related secretary results with random
arrivals and prophet results using more than one sample are also different
models. Their constants cannot be substituted into the comparison table
without a reduction preserving every assumption.

The current written coefficient exceeds the announced `2^-47` headline.
It does not establish superiority to the strongest coefficient in an unseen
proof, an exhaustive priority search, or novelty of every proof ingredient.
