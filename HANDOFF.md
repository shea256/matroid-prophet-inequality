# Review and next work

The current manuscript derives more than `2^-34`. The next decisive step
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
4. Check the two marked sequences and their shared generator variables, the
   three coefficient types including early births, and the hyperplane count.
   Check the density cutoff and Chernoff charge without conditioning the focal
   product law on the good event. See the [audit](proofs/joint_residual_audit.md).
5. Verify every changed filter, density, guard/test, parity, branch, and
   phase factor. Keep the minimum over orders inside the seed expectation
   and preserve all unused-coordinate information in the simulation.

The [baseline](BASELINE.md) distinguishes accessible manuscripts from
unverified announcements. Compare any newly available proof's assumptions,
strongest coefficient, and method before updating a novelty or priority claim.

The [archive](archive/README.md) preserves the superseded `2^-63` and
`2^-43` checkpoints, including original proof artifacts and certificates.
Use the root manuscript for the current claim; do not treat archive wording
as the current comparison or review status.

Further mathematical improvements could target the residual-family complexity
or use additional matroid structure in the safety/rank comparison. The
abstract query hypotheses alone cannot raise the exit bound above `1/2`,
as shown by the repeated-OR example. Parameter search is not globally optimal.

For future updates, change the manuscript, rerun the relevant exact checks,
update `results/current.json` and the improvement record, and rebuild the
PDF. Keep the stable root entry points and preserve previous public commits.
Record independent review or formalization only after it actually occurs.

The published `2^-36` commit remains unchanged. This branch proposes the
`2^-34` follow-up. A next attack is to charge witness-dependent residual
entropy to nominal rank rather than cap both witness and generator counts
at the same threshold. That idea is not part of the current theorem.
