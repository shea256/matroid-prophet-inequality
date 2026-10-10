# Prepared announcement text

Draft wording for a future release. The repository is currently private.
This file is not a social-media posting record.

## Post 1

Imagine filling a few team slots, one candidate at a time. Decisions are final;
you get one past performance sample per candidate.

An opponent sees all samples, values, and your coin flips, then chooses the arrival order.

Can you still compete with perfect hindsight?

## Post 2

OpenAI proved a fixed fraction is possible. We sharpen #111’s
guarantee to above 2⁻³⁶ of the expected hindsight optimum, under matroid
constraints.

Developed with Codex. Proof + exact checks; independent review welcome.

https://github.com/shea256/one-sample-matroid-prophet

## Context / follow-up

This builds extensively on OpenAI's construction. It is an AI-assisted
paper with same-agent verification; independent review and
formalization are pending. Finite checks support the written proof but
do not prove the universal theorem. No efficient implementation is claimed.

The hiring scenario illustrates a capacity constraint, one example of a
matroid. The theorem assumes independent nonnegative values and matching
independent samples; it does not assert that real hiring data satisfy those
assumptions or demonstrate a practical hiring algorithm. The main technical
ingredient is a quadratic potential giving a sharp `1/2` bound for an
auxiliary exit-hazard lemma, with tighter residual estimates and revised
sampling and rounding in the final coefficient.

The comparison uses the 2^-293 coefficient derived in OpenAI's manuscript,
which is stronger than its 2^-310 headline. I'm not claiming priority or a
confirmed best-known bound. The earlier 2^-63 and 2^-43 derivations are
archived as superseded checkpoints within this research effort.
Mathematical review, particularly of the conditional query argument and its
connection to the reverse process, would be welcome.
