# Baseline and primary sources

Audit date: October 10, 2026. Pinned OpenAI/math revision:
`fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`.

The source manuscript derives `2^-293`, stronger than its `2^-310` headline.
The immediate comparison for the current refinement is the preceding
`>(7/4)*2^-32` retained-basis certificate at
[merged master 6d94154](https://github.com/shea256/matroid-prophet-inequality/tree/6d94154ae9961733b7604918a2d3b642d218d61e),
following [PR #4](https://github.com/shea256/matroid-prophet-inequality/pull/4)
and the README update in [PR #5](https://github.com/shea256/matroid-prophet-inequality/pull/5).
Its exact coefficient is `548933908320757/1325382348737372749824000`. Both versions
have written proofs and same-agent checks; independent review is pending.
These are the documented comparisons. The audit does not establish an
exhaustive strongest-current-result or priority claim.

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
| Hybrid safety | `eq:hybrid-containment`, `eq:birth-safety-probability` | Same coupling and equal guard/test rates; safety conditioned on activation membership |
| Residual encoding | `lem:pivot-patterns`, `lem:pattern-family` | Shared variables, retained bases, projected witnesses, and fixed activation scores |
| Residual tail | `eq:residual-tail` | Joint mask membership with the overlap correction; additive tail error still charged |
| Candidate filter | `lem:filter` | Rate `3/4`, with both expectation factors recalculated |
| Rank cost | `lem:all-orders`, `lem:rank-cost`, `lem:thinning` | Same deterministic/conditional lemmas; density rate `3/8` and effective rank coefficient charged exactly |
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

## Baseline for the rank-charged update

The preceding public result is the `2^-34` derivation merged in
[PR #1](https://github.com/shea256/matroid-prophet-inequality/pull/1), commit
`08300e2d9c4a8529db0198631716b7ef20dd8aa5`. Its coefficient is
`14995972860899/244123247301151948800000`. That update's exact certificate is
approximately 3.93235 times that value; the comparison preserves all original
quantifiers. The [unchanged snapshot](archive/joint-residual/README.md)
preserves the earlier paper. Both versions have written proofs and same-agent
checks, with independent mathematical review pending.

## Baseline for the retained-basis update

That version's coefficient
`548933908320757/1325382348737372749824000` is approximately
`1.71459364062` times the exact PR #2 coefficient, a **71.46% increase**.
It exceeds `(7/4)*2^-32` and remains below `2^-31`. The certificate
reconstructs the previous coefficient before comparing it. The preceding
paper and its publication sources are preserved in the
[rank-charged snapshot](archive/rank-charged/README.md).

The [October 10 source refresh](verification/retained_basis_baseline_audit.json)
re-fetched nine primary artifacts: index, scope, introduction, algorithm,
safety, transfer, accounting, setup, and secretary consequence. Their hashes
matched the pinned source; the upstream head was unchanged. The fixed-order
`2609.19118v1` and random-order `2609.14555v2` papers do not provide the same
almighty-adversary guarantee. No proof of the external `2^-47` announcement
was located. These findings remain a scoped comparison, not an exhaustive
novelty claim. The historical receipt also records PR #2's state at that audit;
it does not assert its current merge status.

## Baseline for the activation-split update

The selected coefficient is
`8003458533570087953/16807475946150704657203200000`, approximately
`1.14973122069` times the exact retained-basis coefficient: **14.97% higher**.
It exceeds `(51/50)*2^-31` and remains below `2^-30`. The scalar verifier
reruns the preceding verifier before comparing coefficients. The preceding
publication and sources are preserved in the
[retained-basis snapshot](archive/retained-bases/README.md), with 17 unchanged
artifacts from merged commit `6d94154`.

The [activation source refresh](verification/activation_baseline_audit.json)
again checked nine primary artifacts and both related arXiv versions. Their
model distinctions remain as above; the pinned OpenAI revision was unchanged.
No supporting proof for the external announcement was located in that scoped
search. No exhaustive priority or best-known-bound claim is made.
