# Research and repository instructions

The maintainer has made this repository public and announced the initial
`2^-36` paper. Do not change visibility or post announcements without an
explicit user instruction. Proposed updates go through pull requests.

The project license is Apache 2.0. Preserve LICENSE and the source attribution
in NOTICE when redistributing the package. No inherited MIT license applies;
the earlier MIT text was introduced during project preparation in error.

Preserve the exact one-sample model and full-seed almighty-adversary quantifier.
Distinguish a universal written proof from finite tests, scalar certificates,
same-agent audits, independent review, and formalization. Credit the pinned
OpenAI framework and verify newer primary results before claiming novelty.
Do not infer the contents or strongest coefficient of an unavailable proof.

Keep the artifacts listed in every archive manifest unchanged as
historical snapshots. Explain corrections in the archive index rather than
silently rewriting old claims. Run scripts/check_archive.py after archive changes.

Keep `manuscript.md`, `manuscript.pdf`, and `tex/manuscript.tex` as stable,
generated entry points. Edit `paper/framework.md`, the selected result record,
and `results/registry.json`; do not hand-edit generated paper text, current
metadata, RESULT.md, IMPROVEMENTS.md, or the README's marked headline block.
Follow `results/README.md` for the versioned update workflow. Preserve earlier
result records and archive the committed publication before replacing it.
Candidate entries cannot be selected. A proposed entry needs a written proof
and completed same-agent checks; independent review is separate.

Run relevant verification with `python3 -B scripts/run_checks.py` and validate
package links, immutable archives, generated files, and artifact hashes with
`python3 -B scripts/validate_repository.py`. Rebuild with
`python3 -B scripts/build_manuscript.py`; it writes the build receipt itself.
Run `python3 -B scripts/build_manuscript.py --check` before handoff. For changes
to the registry/build workflow, run `python3 -B -m unittest discover -s scripts/tests`.
Run `git diff --check`. Never describe these checks as independent proof review.
