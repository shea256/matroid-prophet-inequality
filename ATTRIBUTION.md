# Attribution and provenance

## Foundational source

**OpenAI** supplies the original theorem and construction in
*One Sample Suffices for Matroid Prophet Inequalities against an Almighty
Adversary*, September 23, 2026. This project uses revision
`fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb` of
[openai/math](https://github.com/openai/math/tree/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb).
The original density expansions and generator bounds, guarded paths, reverse
exposure, hybrid safety comparison, marked-pivot lemma and residual encoding,
order-uniform rank accounting, and lossless one-sample simulation belong
to that source. The manuscript identifies these dependencies explicitly.

Pinned artifact URLs and SHA-256 hashes are in
[source_manifest.json](verification/source_manifest.json). Upstream manuscripts
and Lean files are fetched into an ignored cache, not redistributed here.
The upstream repository's [root license is Apache 2.0](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/LICENSE).
Its existing licenses and author notices remain applicable.

## This project's claimed contribution

The written refinement introduces a quadratic conditional-probability
potential and uses it to prove a `1/2` expected-exit-hazard bound. A repeated-OR
example shows sharpness for the abstract query hypotheses. The current follow-up adds a joint affine encoding of both residual tests
and a density-size cutoff with an explicit exceptional-event charge. It retains
an integrated residual tail, changed mask probabilities, affine branch mixing,
and finer finite rational rounding phases. The finite-offset technique itself
is standard; no new rounding principle is claimed.

The exact verifiers and paper packaging were developed in the Open Math
Problems project and extracted for this standalone repository at the
maintainer's request. At the maintainer's direction, this standalone project
is distributed under [Apache 2.0](LICENSE). [NOTICE](NOTICE) records the
project's provenance and source attribution. The paper's author is **Ryan Shea**,
who maintains this repository under [shea256](https://github.com/shea256).
Codex assistance is disclosed below; independent review remains pending.

Related announcements and their evidence status are recorded in
[the baseline's related-work note](BASELINE.md#related-work-and-comparison-limits).
The [archive](archive/README.md) preserves earlier derivations from the same
research effort, including their historical wording and review status.

## AI assistance and verification

The research, manuscript, and scripts were developed with Codex assistance.
Exact certificates establish finite arithmetic assertions; enumerations test
specified finite cases. Neither establishes the universal theorem by itself.
The mathematical argument and source dependencies received same-agent second
passes. No independent mathematical review or Lean formalization of this
refinement has been completed. No particular model version or external
reviewer is claimed on the basis of an unrecorded assumption.

The repository is public. Publication does not settle novelty,
correctness, or the strongest current bound. See [BASELINE.md](BASELINE.md)
and [HANDOFF.md](HANDOFF.md) for the outstanding comparison and review tasks.
