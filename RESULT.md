# Current result

**Written theorem claim: a guarantee greater than `2^-34`**, with exact
certificate `C_1=14995972860899/244123247301151948800000`, approximately
`1.0553229 * 2^-34`. It is about 4.057 times the published certificate at
[commit 669e97c](https://github.com/shea256/matroid-prophet-inequality/tree/669e97c863aa7863c93258a5a1e2c6d9165b2d2b).
The construction uses `37n+24` independent fair bits and preserves the same
one-sample model and full-seed almighty adversary.

The new proof shares generator variables between both residual pivot tests,
giving `192^q S_q(n)^2 S_(2q)(2n)`, then applies a density cutoff with an
explicit Chernoff charge. The quadratic exit potential and all structural
source interfaces remain in use. The abstract exit bound `1/2` is sharp;
this is not an upper bound for the matroid prophet problem.

| Evidence category | Status |
|---|---|
| Universal mathematical claim | Written proof with explicit source dependencies |
| Exact coefficient | Rational logarithm enclosures and scalar certificate |
| Joint encoding | 45,824 encodings and 331,491 signs on 170 finite cases |
| Boundary checks | Early births, parity shifts, floors, binomial tails, rational phases, missing-shift negative control |
| Same-agent audit | Completed; no remaining gap identified |
| Independent mathematical review | Pending |
| Lean formalization of this refinement | Not performed |
| Strongest-current-result / novelty | Not established; comparisons use accessible manuscripts |
| Practical or polynomial-time algorithm | Not claimed |

Finite tests support the argument; the universal claim rests on the written
proof. The source baseline is OpenAI's derived `2^-293`; the immediate
published baseline from this project is `>2^-36`. Earlier stages are
preserved in Git history and the [archive](archive/README.md).

See [the paper](manuscript.md), [verification scope](verification/README.md),
[baseline](BASELINE.md), and [review questions](HANDOFF.md).
