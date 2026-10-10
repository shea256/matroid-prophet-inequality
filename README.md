# One-sample matroid prophet inequalities: a sharper guarantee

A research project on **OpenAI Math Problem #111**, improving the quantitative
guarantee for one-sample selection on arbitrary finite matroids against an
adversary that sees every sample, value, and random seed bit.

**[Read the paper (PDF)](manuscript.pdf)** · [Read online](manuscript.md) · [LaTeX source](tex/manuscript.tex)

The current written proof gives

```math
\mathbb E[\mathrm{reward}]\ge 2^{-36}\,\mathbb E[\mathrm{OPT}].
```

It uses one independent sample per label and **`38n+23` initial fair bits**.
The rule needs no description of the value distributions, maintains matroid
independence at every arrival prefix, and retains the full-seed almighty
adversary. Only the offline optimum must be integrable. Computation and
storage may be exponential, and observations are exact; no polynomial-time
or practical-performance claim is made.

**Status: research draft with a written proof and same-agent
verification. Independent mathematical review and formalization are pending.**
Exact arithmetic and finite tests accompany the proof; they do not prove
its universal assertions. No best-known-bound or priority claim is made.

The repository is **private pending a release decision**. Announcement text is prepared
for a future release; no public announcement is recorded.

## Contribution

The main proof change is a **quadratic query potential**. It yields expected
reverse-exit hazard at least `1/2`, and an abstract query example shows this
constant is sharp under that lemma's hypotheses. This `1/2` is an auxiliary
lemma, not the final prophet guarantee. The final coefficient also uses an
integrated residual tail, revised filter and density probabilities, and
64 shared rational rounding phases.

The source's density paths, hybrid safety comparison, marked-pivot machinery,
rank accounting, and sample/value simulation remain fundamental dependencies.
OpenAI already established the qualitative constant guarantee. This project
supplies a sharper quantitative analysis of that construction, with the
new argument and its limitations made explicit. See [attribution](ATTRIBUTION.md)
and [the improvement record](IMPROVEMENTS.md).

| Comparison | Guarantee | Evidence available here |
|---|---:|---|
| OpenAI manuscript's derived constant | `2^-293` | Accessible pinned primary manuscript; headline is `2^-310` |
| Daniel's announcement | `2^-47` | Announcement verified; proof, exact assumptions, and strongest coefficient unavailable |
| This written derivation | `> 2^-36` | Written proof, exact certificates, finite checks; independent review pending |

The simplified `2^-36` coefficient is 2,048 times the announced `2^-47`
headline. That comparison does not establish superiority to an unavailable
proof's strongest result. These are guarantee coefficients, not measured
speedups or observed performance. [Baseline and sources](BASELINE.md)

The compact exact coefficient certified in the paper is

```math
C_0=\frac{9652683394380719}{637507023635152349901619200}
\approx1.0405020\cdot2^{-36}.
```

## Reproduce

Python **3.9+**, standard library only:

```sh
python3 -B scripts/run_checks.py
```

This runs the current exact constant certificate, finite reverse-hazard checks,
and query/filter/residual/rounding checks, and compares them with the recorded
outputs. It also validates local documentation links and the paper's build
receipt. Run the retained exhaustive small-matroid and arrival-order checks
as well with:

```sh
python3 -B scripts/run_checks.py --full
```

For the declared exact parameter search:

```sh
python3 -B experiments/search_quadratic_parameters.py
```

Rebuild the PDF with Python and pdfLaTeX, including `amsmath`, `amssymb`,
`amsthm`, `geometry`, and `hyperref`:

```sh
python3 -B scripts/build_manuscript.py > verification/paper_build.json
```

The build uses three passes with shell escape disabled. Its receipt records
source and PDF hashes; byte-identical PDF rebuilds are not promised.
Optionally retrieve the pinned primary sources into the ignored cache,
checking their recorded hashes:

```sh
python3 -B verification/fetch_sources.py
```

## Evidence and review

- [Verification scope and recorded outputs](verification/README.md)
- [Result record](RESULT.md) and [machine-readable current result](results/current.json)
- [Executed approaches](ATTEMPT.md) and [reproduction log](RUNLOG.md)
- [Review questions and next work](HANDOFF.md)
- [Prepared announcement text](announcement.md), not a social-media posting record

This work was developed with AI assistance using Codex. Same-agent second
passes are not independent peer review. The paper and stable entry points
will be updated as the proof is reviewed or improved; earlier public versions
remain available in Git history. The [MIT license](LICENSE) preserves the
original project notice; cited external works retain their own terms.
