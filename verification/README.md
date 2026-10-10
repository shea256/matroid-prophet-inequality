# Verification scope

Run `python3 -B scripts/run_checks.py` from the repository root. Python 3.9+
and the standard library suffice. The runner discovers script/reference pairs
from the [result registry](../results/registry.json), including earlier scalar
certificates and shared structural checks. Fresh JSON must match each reference.

The [current receipt](current_run_receipt.json) records actual runs and script
hashes. Earlier receipts refer to the versions and suites named within them.
Build and publication checks are separate from mathematical verification.

| Check | Scope |
|---|---|
| `certify_activation_split.py` | Exact joint-membership tilts by log intervals and integer powers, positive-series decay cross-check, activation charge cancellation, old/new coefficients, and 40n+26 seed count |
| `check_activation_split.py` | 2,222 exact joint mask probabilities, 70,296 projected encodings/charges, 140,592 fixed-activation basis checks, 2,716 conditional safety bounds, and adaptive excess tails |
| `certify_retained_basis.py` | Exact log intervals, integer-power tilt cross-checks, independent positive-series decay bound, projected rank interface, additive cancellation, old/new coefficients, and 42n+27 seed count |
| `check_retained_basis.py` | 74,881 interleavings, 3,349 basis families, 45,824 projected encodings/charges, forced/omitted occurrences, adaptive tails, and an additive-error negative control |
| `certify_rank_charged.py` | Exact log enclosures, both tilt inequalities, rank/density charges, final error/slack, coefficient, branch mixture, and seed count |
| `check_rank_charged.py` | 78 weighted generating bounds, 972 adaptive tail bounds, 216 integrated expectations, 45,824 actual path charges, two omitted-charge negative controls |
| `certify_joint_residual.py` | Retained exact `2^-34` coefficient, cutoff exception, and changed probabilities |
| `check_joint_residual.py` | 45,824 actual residual encodings, 331,491 affine signs, early/parity cases, a missing-shift control, binomial tails/floors, and current phase mesh |
| `certify_quadratic_constants.py` | Retained exact `2^-36` coefficient |
| `check_quadratic_hazard.py` | 4,916 local and 3,153 global quadratic inequalities on 170 small matroid/weight cases |
| `check_quadratic_ingredients.py` | Adaptive Boolean queries, biased filters, selected residual expectations, phase boundaries, and abstract sharpness |
| Archived scalar certificates | Original `2^-63` and `2^-43` finite arithmetic assertions |

The activation path checker uses all 1,400 filter configurations on 170
small matroid/weight instances, threshold 2, and guard/test rate `1/4`.
It includes 184 omitted active second-stream generators, 504,544 affine
signs, and positive residual, rank, and generator charges. Separate mask
tests use both stress rates and the final `rho=3/8`, `t=11/2^17` rates.
Adaptive selectors see the entire mask; 26 of 40 integrated-expectation
cases have strictly positive excess. A negative control rejects naive
multiplication of generator and residual membership probabilities.

The retained-basis path checker uses an empty filter mask, threshold 2 and small stress penalties `1/4,1/2`
to exercise nonzero generators, witness ranks, and excess residuals. Its
negative controls are abstract scalar examples, not hard matroid instances.
The adaptive family check lets a selector inspect the entire mask before
choosing an overlapping family member. Exact final algorithm probabilities
and penalties are certified separately.

The retained hazard checker uses stress guard rate `1/4`; the Boolean-event
suite also tests the earlier published guard rate `2^-16`. The joint checker
checks the same 256-phase mesh used by the current result. These finite cases
do not establish a theorem about every matroid. Reusing `reverse_support.py`
and the earlier finite models is not independent review.

## Extended and archived checks

`--full` adds `finite_checks.py` and `check_online_rule.py`: 92 small labeled
matroids and 5,347,942 complete arrival-order runs under the documented older
stress configurations. These are retained structural regressions, not observed
performance of the final competitive guarantee.

`python3 -B scripts/check_archive.py` verifies unchanged archival artifacts
and runs the earlier archive's default three checks; `--full` also runs its
exhaustive structural checks. The 23 initial artifacts, six-file `2^-34`
publication snapshot, 16-file rank-charged snapshot, and 17-file
retained-basis snapshot have recorded hashes (62 preserved artifacts in total).

## Generated publication checks

`python3 -B scripts/build_manuscript.py --check` verifies registry/certificate
agreement, generated text, and recorded hashes for all paper inputs and
Markdown/LaTeX/PDF outputs. It writes nothing and requires no LaTeX installation.
The package validator additionally checks immutable archives and current local
links. Historical documents retain their original relative-link context;
their current indexes and immutable hashes are validated.

`python3 -B -m unittest discover -s scripts/tests` tests rejection of coefficient
mismatches, scaled-threshold errors, unfinished selections, path escapes, stale headlines, changed
paper inputs/PDFs, and modified archives. It also checks that a bigger candidate
does not select itself and a failed compilation preserves publication outputs.
These are software regression tests, not mathematical proof checks.

Full paper builds require Pandoc and pdfLaTeX. The build receipt records their
output hashes and source inputs; compilation does not establish the theorem.
No independent review or Lean formalization of these refinements is recorded.
See [review questions](../HANDOFF.md).
