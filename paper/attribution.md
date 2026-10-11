## Sources, attribution, and comparison limits

OpenAI supplies the original qualitative constant guarantee and construction
in *One Sample Suffices for Matroid Prophet Inequalities against an Almighty
Adversary*, September 23, 2026, pinned at
[revision fd4aeeb2ee4f](https://github.com/openai/math/tree/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb).
Its density paths, reverse exposure, hybrid comparison, marked-pivot machinery,
rank accounting, and lossless sample/value simulation are fundamental
inputs. The manuscript derives $2^{-293}$, stronger than its $2^{-310}$
headline. The secretary consequence is in the same manuscript. Primary
sources and hashes are recorded in [the baseline](../BASELINE.md).

This project's quadratic potential, joint affine encoding, and application
of weighted residual counting refine that construction's quantitative
analysis. The current version reconstructs old retained bases by contraction,
uses forced retained occurrences, projects witnesses onto the comparison
optimum, and pays the tail's additive constant through the maximum branch.
It further conditions safety on activation membership, assigns fixed scores
to activation generators, and uses the joint generator/witness/residual
mask law with its generator-residual overlap correction.
The selected refinement merges the two parity descriptions of generators
omitted from the second retained basis and restricts the overlap charge to
states that can actually be residual. All inherited costs remain charged.
Greedy scanning in a contracted matroid is standard; the claimed refinement
is its application and the resulting quantitative accounting here. Exponential weighting, union bounds, finite-offset rounding,
and binomial estimates are established methods; no new general principle
is claimed for them. Each version retains its specific evidence and source
credit in the result registry and archives.

Daniel (@firsttimelifer) [announced](https://x.com/firsttimelifer/status/2108282829809541468)
a $2^{-47}$ guarantee on October 8, 2026. A supporting manuscript was not
located in the October 11 audit; its assumptions and proof remain unverified.
It is acknowledged as an announcement, not an established comparison baseline.
The $1/2$ prophet result in
[Abdi, Banihashem, Hajiaghayi, and Mittal, arXiv:2609.19118v1](https://arxiv.org/abs/2609.19118v1)
assumes a fixed order independent of samples and values and therefore uses
a different adversary model.

This work was developed with Codex assistance. The paper's author is Ryan
Shea. The written arguments and exact programs have same-agent verification;
independent mathematical review and formalization of these refinements
remain pending. No exhaustive priority search, confirmed best-known-bound
claim, or practical performance claim is made. The repository uses Apache
2.0, with source attribution in [NOTICE](../NOTICE).
