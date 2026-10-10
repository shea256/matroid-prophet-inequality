# Versioned results and paper updates

The reusable construction and proof interfaces are in
[paper/framework.md](../paper/framework.md). Each refinement has its own
written result record, exact certificate, and verifier.
[registry.json](registry.json) explicitly selects the current result. The
builder combines the framework, that record, and
[attribution](../paper/attribution.md) into the complete paper.

`proposed` means a written proof with completed same-agent scalar and finite
checks; independent review is a separate question. `candidate` means the
required argument or verification is incomplete and cannot be selected.
`historical` preserves an earlier incorporated result and its evidence. The
registry does not select a result automatically when its number increases.
Historical publications are reproduced through their snapshots or Git commits,
not reassembled against a changed current framework.

## Add a refinement

1. Pin the sources and write `results/<id>.md`. State the changed argument,
   exact assumptions, source dependencies, final-theorem implication, and
   resources. Use ordinary relative Markdown links and `$...$` / `$$...$$`
   mathematics. Update the shared framework only when its argument changes;
   review every dependent result affected by such a change.
2. Add the verifier, finite checks, and reviewed reference JSON. The scalar
   certificate supplies the coefficient, algorithm parameters, seed count,
   and simplified guarantee. Add a registry entry with status `candidate`
   while the proof or checks are incomplete. Earlier entries are preserved.
3. Before replacing a published paper, preserve its committed artifacts:

   ```sh
   python3 -B scripts/archive_paper.py --result-id OLD_ID --commit COMMIT_SHA
   ```

   This records unchanged PDF/Markdown/LaTeX, result metadata, applicable paper
   sources, and build/check receipts with a SHA-256 manifest. It refuses to
   overwrite an existing snapshot. Add its path to the old registry entry's
   `archive` field. Archive links retain the original repository context.
4. Once the written derivation and relevant checks pass, mark the new entry
   `proposed`, explicitly select its ID in `current`, and mark the previous
   selection `historical`. Independent-review flags remain false unless that
   review actually occurs. Each entry's `checks` supplies script/reference
   pairs; the runner discovers them from the registry. Shared and extended
   regressions are retained separately.
5. Run the complete build and checks:

   ```sh
   python3 -B scripts/build_manuscript.py
   python3 -B scripts/run_checks.py --full
   python3 -B -m unittest discover -s scripts/tests
   python3 -B scripts/build_manuscript.py --check
   git diff --check
   ```

   Full builds require Pandoc 3.x and pdfLaTeX with `amsmath`, `amssymb`,
   `geometry`, `longtable`, `booktabs`, `array`, `calc`, and `hyperref`.
   Python checks use the standard library. Render and inspect the resulting
   PDF, update provenance and the run log, then submit a PR.

The stable generated entry points are `manuscript.md`, `tex/manuscript.tex`,
`manuscript.pdf`, `results/current.json`, `RESULT.md`, `IMPROVEMENTS.md`, and
the marked current-result block in README. Edit their source records instead
of the generated content. The rest of README remains directly editable.

`--markdown-only` updates text and metadata without compiling the PDF; package
validation will then require a full rebuild if paper inputs changed.
`--check` writes nothing and verifies generated text plus the recorded input,
LaTeX, Markdown, and PDF hashes. A failed compilation leaves the existing
publication outputs intact. These checks establish publication consistency,
not mathematical correctness or independent review.
