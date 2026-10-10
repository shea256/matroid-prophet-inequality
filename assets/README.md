# README progress graphic

[PNG](guarantee-progress.png) · [SVG](guarantee-progress.svg) ·
[Exact data and hashes](guarantee-progress.json) ·
[Renderer](../scripts/build_progress_graphic.py)

The chart places OpenAI's derived `2^-293` bound and the project's exact
coefficients on one base-2 logarithmic y-axis with a marked break. The
source segment spans `2^-294` to `2^-292`; the refinement segment currently
spans `2^-37` to `2^-30`. The omitted interval is written in the gap, with
break marks on the y-axis and the interrupted connector. Both visible
segments use the same vertical distance per doubling.

Project points are labeled with their simplified strict lower bounds,
from `>2^-36` through `>(51/50)*2^-31`. The x-axis lists the source and
successive refinements. The expectation guarantee and current numerical
coefficient appear below the plot.
The common one-sample/full-seed model and pending independent-review status
are stated on the image. See [BASELINE](../BASELINE.md) for source provenance.

The renderer reads the [result registry](../results/registry.json), validates
its certificate values, prepends the pinned source bound, and includes
project records from `announcement_baseline` through `current`, excluding
candidate entries. Exact coefficient fractions are
plotted directly on the logarithmic axis; the point labels use
the registry's simplified bounds, which are lower than the plotted values.
The source bound is the named constant `SOURCE_EXPONENT` in the renderer, tied to the source revision
recorded in the data receipt. Recheck that baseline if the source changes.

After selecting a new result, regenerate both formats and the receipt:

```sh
python3 -m venv .context/chart-venv
.context/chart-venv/bin/python -m pip install matplotlib==3.9.4
.context/chart-venv/bin/python -B scripts/build_progress_graphic.py
```

Matplotlib is needed only to render. Standard-library-only checks compare
the data, registry/renderer hashes, and both image hashes:

```sh
python3 -B scripts/build_progress_graphic.py --check
python3 -B scripts/validate_repository.py
```

The normal verification runner includes package validation, so selecting a
new result without rebuilding the chart fails its final consistency check.
Exact certificate checks and image freshness do not establish the universal
mathematical claims. PNG/SVG byte reproduction can depend on the rendering
environment; their committed hashes identify the reviewed artifacts.
