# Executed approaches

The published `2^-36` derivation used these three linked attacks:

1. **Quadratic query potential.** Track the actual conditional failure
   probability `m` and the depleted failure probability `q`. The potential
   `q^2-2qm` has conditional increment `(q'-q)(q'+q-2m)>=0`. A completed
   failure has `m=q=1`. This gives `E[1_survive q^2]>=p(1-p)`, and the
   next-event containment and finite telescope imply expected exit hazard
   at least `1/2`. A repeated-OR family proves sharpness under the abstract
   hypotheses. Earlier logarithmic potentials were superseded.
2. **Integrated residual tail.** A family fixed before focal bits yields
   `Pr(e>x)<=min(1,N p_O^x)`. Integration gives
   `(log N+1)/log(1/p_O)`, uniformly down to the smallest analyzed group
   `n=kappa`. The selected residual is allowed to depend on the mask.
3. **Recalibrated masks and phases.** Recompute the filter expectation,
   safety probability, and density cost for changed mask rates. Use 64
   finite phases with rational mesh `69/64`, giving rounding factor
   `beta/5`. Combined with affine branch mixing, this yields the coefficient
   above `2^-36` with the same adversary and one-sample model.

The recorded exact parameter search examines 8,064 tuples with density
rate fixed at `5/8`; 3,234 have positive certificates. The chosen tuple
is best in that declared grid. This is not a global optimum. Floating-point
exploration guided discovery, but the published coefficient is certified
by exact fractions. [Search code](experiments/search_quadratic_parameters.py)
and [recorded output](experiments/quadratic_search_output.txt).

No independent agent review, external author consultation, or formal proof
build is claimed. The universal derivation and inherited structural lemmas
are in [the manuscript](manuscript.md).

## Joint-encoding follow-up

Executed three comparisons using the same analytic objective: parameter-only
retuning, a density-size cutoff with the old count, and the cutoff with joint
pivot encoding. The numerical search used 12 deterministic starts per mode
and a declared 275-tuple grid. It is not a global optimum or proof.
[Code](experiments/search_joint_residual.py),
[output](experiments/joint_residual_search_output.json).

The selected dyadic tuple has `kappa=640`, `rho=7/16`, `h=3/4`, `t=2^-15`,
256 phases, and analysis cutoff `33/64`. The exact certificate exceeds
`(21/20)*2^-34`. The written proof charges all basis choices, three generator
types, both affine tests, and the density exception without conditioning
away independence. [Detailed argument](proofs/joint_residual.md),
[same-agent audit](proofs/joint_residual_audit.md).
