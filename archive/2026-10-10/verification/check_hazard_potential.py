#!/usr/bin/env python3
"""Finite exact checks of the new reverse-hazard potential and its interface.

Logarithms use rational intervals from the atanh series after dyadic reduction.
This verifies small instances, not the universal proof or novelty.
"""
import sys
sys.dont_write_bytecode = True
from collections import Counter
from fractions import Fraction as Q
from functools import lru_cache
from itertools import product
import json

from finite_checks import Matroid, all_matroids, size
from check_online_rule import Rule, bits, subsets, union


def atanh_log_bounds(y, terms=24):
    assert 0 <= y <= Q(1, 3)
    total = sum((2*y**(2*j+1)/Q(2*j+1) for j in range(terms)), Q(0))
    tail = 2*y**(2*terms+1)/(Q(2*terms+1)*(1-y*y))
    return total, total+tail


LN2 = atanh_log_bounds(Q(1, 3))


@lru_cache(None)
def log_bounds(x):
    assert x > 0
    if x < 1:
        lo, hi = log_bounds(1/x)
        return -hi, -lo
    k = x.numerator.bit_length()-x.denominator.bit_length()
    if Q(2)**k > x:
        k -= 1
    y = x/Q(2)**k
    lo, hi = atanh_log_bounds((y-1)/(y+1))
    return lo+k*LN2[0], hi+k*LN2[1]


@lru_cache(None)
def mask_law(V):
    # Independent rate-1/4 guards. Irrelevant coordinates are marginalized.
    n = size(V)
    return tuple((C, Q(3**(n-size(C)), 4**n)) for C in subsets(V))


class Reverse:
    def __init__(self, rule, w, h):
        self.rule, self.M, self.h = rule, rule.M, h
        self.G = tuple(sum(1 << e for e in range(rule.M.n)
                           if w[e] == v and rule.candidate(e, v))
                       for v in rule.values[:h])
        self.U = union(self.G)
        self.initial = ((1 << rule.M.n)-1,)*h

    @lru_cache(None)
    def transition(self, k, S, C):
        A, N, queried = self.M.closure[0], [], 0
        for j in range(self.h):
            Nj = self.rule.q(j+1, A) if k >= -3*(j+1) else A
            assert Nj & ~S[j] == 0
            batch = self.G[j] & S[j] & ~Nj
            queried |= batch
            A = self.M.closure[Nj | (C & batch)]
            N.append(Nj)
        return tuple(N), queried

    @lru_cache(None)
    def failure(self, k, S, V, d):
        return sum((prob for C, prob in mask_law(V)
                    if not (self.transition(k, S, C)[0][-1] >> d & 1)), Q(0))

    def states(self, C):
        S, V = self.initial, self.U
        for k in range(-1, -3*self.h-2, -1):
            yield k, S, V
            S, queried = self.transition(k, S, C)
            V &= ~queried
            assert V == union(self.G[j] & S[j] for j in range(self.h))
        assert S[-1] == self.M.closure[0]


def cases():
    for n in range(1, 4):
        for M in all_matroids(n):
            for w in product((1, 4), repeat=n):
                yield M, w
    families = [set(s for s in range(16) if size(s) <= r) for r in (1, 2, 3, 4)]
    families += [set(s for s in range(16) if size(s & 3) <= 1 and size(s & 12) <= 1),
                 set(s for s in range(8) if size(s) <= 2)]
    for I in families:
        for w in ((1, 1, 4, 4), (1, 4, 16, 64), (0, 1, 1, 4)):
            yield Matroid(4, I), w


def main():
    counts, minimum = Counter(), Q(1)
    for M, w in cases():
        U = sum(1 << e for e in range(M.n) if w[e] > 0 and M.rank[1 << e])
        for D in subsets(U):
            rule = Rule(M, {e: w[e] for e in bits(D)}, 0, D, 0, 2)
            for h in range(1, rule.m+1):
                rev = Reverse(rule, w, h)
                nodes = set()
                for C, prob in mask_law(rev.U):
                    nodes.update(rev.states(C))
                for k, S, V in sorted(nodes):
                    for d in bits(S[-1] & ~M.closure[0]):
                        p = rev.failure(k, S, V, d)
                        resource_lo, next_alive = Q(0), Q(0)
                        for C, prob in mask_law(V):
                            N, queried = rev.transition(k, S, C)
                            V2 = V & ~queried
                            # The queried positives alone reproduce this transition.
                            assert rev.transition(k, S, C & queried)[0] == N
                            counts['positive_certificate_checks'] += 1
                            if p:
                                q = rev.failure(k, S, V2, d)
                                assert p <= q <= 1
                                resource_lo += prob*log_bounds(q/p)[0]
                            if N[-1] >> d & 1:
                                r = rev.failure(k-1, N, V2, d)
                                if p:
                                    assert r >= q
                                    counts['depleted_event_comparisons'] += 1
                                next_alive += prob*r
                        if p:
                            assert resource_lo >= 1-p
                            # Upper bound on the RHS using a lower bound on ln(1/p).
                            rhs_upper = p-p*p*(2+log_bounds(1/p)[0])
                            assert next_alive-p >= rhs_upper
                            counts['local_log_resource_checks'] += 1
                        else:
                            assert next_alive >= 0
                        counts['drift_checks'] += 1
                for d in bits(((1 << M.n)-1) & ~M.closure[0]):
                    mean_hazard, potential_lo, mass = Q(0), Q(0), Q(0)
                    for C, prob in mask_law(rev.U):
                        for k, S, V in rev.states(C):
                            N, _ = rev.transition(k, S, C)
                            if not (N[-1] >> d & 1):
                                p = rev.failure(k, S, V, d)
                                assert p > 0
                                mass += prob
                                mean_hazard += prob*p
                                potential_lo += prob*p*(2+log_bounds(1/p)[0])
                                break
                    assert mass == 1
                    initial = rev.failure(-1, rev.initial, rev.U, d)
                    assert potential_lo >= 1+initial
                    assert mean_hazard > Q(5, 16)
                    minimum = min(minimum, mean_hazard)
                    counts['global_hazard_checks'] += 1
                counts['group_prefixes'] += 1
                # Caches are per instance mathematically; release stored self keys.
                rev.transition.cache_clear()
                rev.failure.cache_clear()
        counts['matroid_weight_instances'] += 1
    # Nondecreasing hazards and eventual exit alone do not imply the new lemma.
    # 64 steps of hazard 1/16 followed by certain exit violate its conclusion.
    p = Q(1, 16)
    control = p*(1-(1-p)**64)+(1-p)**64
    assert control < Q(5, 16)
    print(json.dumps({
        'counts': dict(counts),
        'guard_rate': '1/4', 'density_threshold': 2, 'filter_mask': 'H empty',
        'smallest_observed_mean_exit_hazard': str(minimum),
        'negative_control_mean_hazard': str(control),
        'negative_control': 'monotone hazards alone fail; depleted-event comparison is essential',
        'logarithms': 'rational atanh-series intervals, 24 terms after dyadic reduction',
        'result': 'PASS (finite verification of the new potential interfaces)',
    }, indent=2))


if __name__ == '__main__':
    main()
