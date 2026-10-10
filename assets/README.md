# README progress graphic

[PNG](guarantee-progress.png) · [SVG](guarantee-progress.svg) ·
[Exact data and hashes](guarantee-progress.json) ·
[Renderer](../scripts/build_progress_graphic.py)

The left panel compares the pinned OpenAI manuscript's derived `2^-293`
bound with the selected coefficient on a base-2 logarithmic scale. The right
panel uses a linear scale for gains relative to the first announced exact
certificate. Its x-axis lists successive refinements, not elapsed time.
The common one-sample/full-seed model and pending independent-review status
are stated on the image. See [BASELINE](../BASELINE.md) for source provenance.

The renderer reads the [result registry](../results/registry.json), validates
its certificate values, starts at `announcement_baseline`, and stops at
`current`, excluding candidate entries. Gains are calculated with exact
fractions before conversion for plotting. The source bound is the named
constant `SOURCE_EXPONENT` in the renderer, tied to the source revision
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
