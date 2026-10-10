# Review and next work

The current manuscript derives more than `2^-36`. The next decisive step
is independent mathematical review of the written proof and its interfaces
to the pinned source. Exact arithmetic and finite checks have passed.

Review in this order:

1. Verify that `m` is the actual conditional failure probability and `q'`
   is determined before the next query answer. Check the potential identity
   and both terminal outcomes, especially `m=q=1` on failure.
2. Check that the reverse transcript decides the event on all completions,
   and that the depleted current event contains the next survival event on
   exactly the remaining product domain. Freeze the states in this comparison.
3. Check the sign and weighting in the squared-hazard telescope, including
   zero and unit hazards and the deterministic final exit.
4. Check both marked sequences, their movable counts, the conditioning before
   focal bits or listing, and the integrated residual bound at `n=kappa`.
5. Verify every changed filter, density, guard/test, parity, branch, and
   phase factor. Keep the minimum over orders inside the seed expectation
   and preserve all unused-coordinate information in the simulation.

The proof behind Daniel's `2^-47` announcement is still needed for comparison
of assumptions, strongest derived coefficient, method, and novelty. Its
absence is not evidence that the announced result is false or weaker.

Further mathematical improvements could target the residual-family complexity
or use additional matroid structure in the safety/rank comparison. The
abstract query hypotheses alone cannot raise the exit bound above `1/2`,
as shown by the repeated-OR example. Parameter search is not globally optimal.

For future updates, change the manuscript, rerun the relevant exact checks,
update `results/current.json` and the improvement record, and rebuild the
PDF. Keep the stable root entry points and preserve previous public commits.
Record independent review or formalization only after it actually occurs.
