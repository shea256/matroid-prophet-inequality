# Research and repository instructions

This repository is private at the maintainer's request. Do not change its
visibility or post an announcement without an explicit user instruction.

The project license is Apache 2.0. Preserve LICENSE and the source attribution
in NOTICE when redistributing the package. No inherited MIT license applies;
the earlier MIT text was introduced during project preparation in error.

Preserve the exact one-sample model and full-seed almighty-adversary quantifier.
Distinguish a universal written proof from finite tests, scalar certificates,
same-agent audits, independent review, and formalization. Credit the pinned
OpenAI framework and verify newer primary results before claiming novelty.
Do not infer the contents or strongest coefficient of an unavailable proof.

Keep the artifacts listed in archive/2026-10-10/manifest.json unchanged as
historical snapshots. Explain corrections in the archive index rather than
silently rewriting old claims. Run scripts/check_archive.py after archive changes.

Keep `manuscript.md`, `manuscript.pdf`, and `tex/manuscript.tex` as stable
entry points. Mathematical changes belong in the proof, the result record,
and reproducible verifiers. Update `results/current.json`, `RESULT.md`,
`IMPROVEMENTS.md`, and `RUNLOG.md` when the result changes. Preserve prior
public versions in Git history if a public release is later authorized.

Before handoff, run relevant verification with `python3 -B scripts/run_checks.py`
and validate package links and artifact hashes with
`python3 -B scripts/validate_repository.py`. Rebuild changed TeX via
`python3 -B scripts/build_manuscript.py > verification/paper_build.json`.
Run `git diff --check`. Never describe these checks as an independent proof review.
