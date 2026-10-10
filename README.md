# One-sample matroid prophet inequalities: a sharper guarantee

By **Ryan Shea**. A living research project on
[OpenAI Math Problem #111](https://github.com/openai/math/blob/main/lean/docs/111.md).

<!-- current-result:start -->

**[Read the latest paper (PDF)](manuscript.pdf)** · [Read online](manuscript.md) · [LaTeX source](tex/manuscript.tex)

Current result: **[Retained bases and projected residuals](results/retained-bases.md)**, 2026-10-10.

```math
\mathbb E[\mathrm{reward}]\ge C_\star\mathbb E[\mathrm{OPT}],\qquad
C_\star=\frac{548933908320757}{1325382348737372749824000}>\frac{7}{4}\, 2^{-32}.
```

The exact certificate is approximately **1.71459 times** the preceding [`2^-32` certificate](results/rank-charged.md) (**71.46% higher**). This compares guaranteed fractions, not measured performance. The construction uses **`42n+27` fair bits**.

Retained-basis reconstruction, projected witnesses, and an additive maximum-branch charge improve the guarantee.

**Written proof with same-agent verification; independent mathematical review and formalization pending.** Finite checks accompany the written proof; they do not prove
its universal assertions. No priority or confirmed best-known-bound claim
is made. These paper links remain stable as results are updated.

<!-- current-result:end -->

The source construction is in
[OpenAI's accompanying paper](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/One-Sample-Suffices-for-Matroid-Prophet-Inequalities-against-an-Almighty-Adversary-September-23-2026/final.pdf).
This project develops quantitative refinements of that construction. It
retains one independent sample per label, unknown independent nonnegative
value distributions, prefix feasibility, and the adversary seeing every
sample, value, and initial seed bit. Only the offline optimum must be
integrable. Computation and storage may be exponential, and observations
are exact; no polynomial-time or practical-performance claim is made.

## Reproduce

Python **3.9+**, standard library only for verification:

```sh
python3 -B scripts/run_checks.py
```

The registry selects the current result explicitly and retains earlier
verifiers. Fresh JSON must equal each recorded reference. Package checks
also reject stale generated text, certificate mismatches, altered archive
artifacts, and stale paper hashes. Include the retained exhaustive small
matroid and arrival-order regressions with:

```sh
python3 -B scripts/run_checks.py --full
```

## Update the paper

The [shared proof](paper/framework.md), [versioned results](results/README.md),
and [registry](results/registry.json) are the editable sources. Follow the
[update workflow](results/README.md) to preserve the previous publication,
add a written result and certificate, and explicitly select its ID.

Rebuild the manuscript, LaTeX, PDF, current-result metadata, README headline,
and improvement history with **Pandoc 3.x and pdfLaTeX**:

```sh
python3 -B scripts/build_manuscript.py
```

`--markdown-only` regenerates the text and metadata without compiling the
PDF. `--check` checks text freshness and the paper's recorded input/artifact
hashes without writing files. The build uses three pdfLaTeX passes with shell
escape disabled; byte-identical PDF rebuilds are not promised.

## Evidence and history

- [Current result](RESULT.md) and [machine-readable metadata](results/current.json)
- [Improvement history](IMPROVEMENTS.md) and [unchanged earlier artifacts](archive/README.md)
- [Verification scope](verification/README.md), [executed attempts](ATTEMPT.md), and [run log](RUNLOG.md)
- [Source attribution](ATTRIBUTION.md), [baseline](BASELINE.md), and [review questions](HANDOFF.md)
- [Earlier prepared announcement](announcement.md), retained as historical wording

The author announced the earlier `2^-36` version on October 10, 2026.
Subsequent results update the same paper links and retain earlier versions.
This work was developed with Codex assistance. Same-agent checks are not
independent mathematical review, and finite tests do not prove the universal
claims. Review and formalization remain pending.

## License

This project uses the [Apache License 2.0](LICENSE).
See [NOTICE](NOTICE) and [attribution](ATTRIBUTION.md) for provenance;
cited external works retain their own terms.
