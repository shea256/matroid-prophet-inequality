# Improvement record

<!-- Generated from results/registry.json. -->

| Result | Guarantee | Change | Review stage |
|---|---:|---|---|
| [Parameter refinement](results/parameter-refinement.md) | $>2^{-63}$ | Refined source parameters, affine branch mixing, and finite rounding offsets. | Written proof; independent review pending |
| [Logarithmic hazard potential](results/logarithmic-hazard.md) | $>2^{-43}$ | Introduced a logarithmic hazard potential and tighter residual accounting. | Written proof; independent review pending |
| [Quadratic hazard potential](results/quadratic-hazard.md) | $>2^{-36}$ | A quadratic exit potential, integrated residual tail, and revised masks and finite phases. | Written proof; independent review pending |
| [Joint residual encoding](results/joint-residual.md) | $>2^{-34}$ | Shared generator variables across two pivot tests and charged a density-sample cutoff. | Written proof; independent review pending |
| [Rank-charged residual entropy](results/rank-charged.md) | $>2^{-32}$ | The refinement weights residual families by generator and witness counts, charges their entropy to expected sample size and nominal rank, and removes the density cutoff. | Written proof; independent review pending |

The registry explicitly selects `rank-charged`. Historical records and
certificates remain unchanged. Review status and mathematical validity are
distinct: these records have written proofs and same-agent checks, with
independent review and formalization pending. No priority claim is made.

## 2026-10-10 — Parameter refinement

Refined source parameters, affine branch mixing, and finite rounding offsets.

[Result record](results/parameter-refinement.md) · [Certificate](archive/2026-10-10/verification/constants_output.json)

## 2026-10-10 — Logarithmic hazard potential

Introduced a logarithmic hazard potential and tighter residual accounting.

[Result record](results/logarithmic-hazard.md) · [Certificate](archive/2026-10-10/verification/hazard_constants_output.json)

## 2026-10-10 — Quadratic hazard potential

A quadratic exit potential, integrated residual tail, and revised masks and finite phases.

[Result record](results/quadratic-hazard.md) · [Certificate](verification/reference/quadratic_constants_output.json)

## 2026-10-10 — Joint residual encoding

Shared generator variables across two pivot tests and charged a density-sample cutoff.

[Result record](results/joint-residual.md) · [Certificate](verification/reference/joint_residual_constants_output.json) · [Preserved publication](archive/joint-residual/README.md)

## 2026-10-10 — Rank-charged residual entropy

The refinement weights residual families by generator and witness counts, charges their entropy to expected sample size and nominal rank, and removes the density cutoff.

[Result record](results/rank-charged.md) · [Certificate](verification/reference/rank_charged_constants_output.json)
