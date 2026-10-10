# Baseline and primary sources

Audit date: October 10, 2026. Pinned OpenAI/math revision:
`fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`.

The source manuscript derives `2^-293`, stronger than its `2^-310` headline.
The immediate published baseline for this follow-up is this project's
`>2^-36` version at [commit 669e97c](https://github.com/shea256/matroid-prophet-inequality/tree/669e97c863aa7863c93258a5a1e2c6d9165b2d2b),
with the same-agent review status. These are the documented comparisons. The audit does not establish
an exhaustive strongest-current-result or priority claim.

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
| Residual encoding | `lem:pivot-patterns`, `lem:pattern-family` | Two linked pivot tests share `j+z` variables |
| Residual tail | `eq:residual-tail` | Joint count, density cutoff, and integrated union-bound tail |
| Candidate filter | `lem:filter` | Rate `3/4`, with both expectation factors recalculated |
| Rank cost | `lem:all-orders`, `lem:rank-cost`, `lem:thinning` | Same deterministic/conditional lemmas; density rate `7/16` charged exactly |
| Rounding and branches | Source geometric levels and maximum branch | 256 rational phases and affine mixture |
| One-sample simulation | `lem:simulation` | Same lossless full-seed reduction |

## Related work and comparison limits

[Daniel (@firsttimelifer)](https://x.com/firsttimelifer/status/2108282829809541468)
publicly announced a `2^-47` guarantee on October 8, 2026. A supporting
write-up was unavailable for comparison at the October 10 audit; we have
not verified its assumptions or proof. This is an unverified announcement,
not an established baseline. The accessed post is recorded in
[announcement.json](verification/announcement.json).

The larger constant in [Abdi–Banihashem–Hajiaghayi–Mittal,
arXiv:2609.19118v1](https://arxiv.org/html/2609.19118v1) concerns an arrival
order fixed independently of samples and values. It does not supply this
paper's almighty-order quantifier. Related secretary results with random
arrivals and prophet results using more than one sample are also different
models. Their constants cannot be substituted into the comparison table
without a reduction preserving every assumption.

The main comparison establishes a larger written coefficient than the
accessible OpenAI manuscript. It does not establish an exhaustive priority
search, superiority to an unavailable proof, or novelty of every ingredient.

The October 10 refresh re-fetched the index, problem page, transfer, and
accounting sections; all matched the pinned hashes. The repository's latest
OpenAI commit remained unchanged. [Audit receipt](verification/joint_baseline_audit.json).
No supporting manuscript for the external announcement was located. This
is not an exhaustive literature or priority search.
