#!/usr/bin/env python3
"""Exact finite checks of the quadratic hazard lemma; not a universal proof."""
import sys
sys.dont_write_bytecode = True
from collections import Counter
from fractions import Fraction as Q
import json

from reverse_support import Reverse, cases, mask_law
from check_online_rule import Rule, bits, subsets


def main():
    counts, minimum = Counter(), Q(1)
    for M, w in cases():
        U = sum(1 << e for e in range(M.n) if w[e] > 0 and M.rank[1 << e])
        for D in subsets(U):
            rule = Rule(M, {e: w[e] for e in bits(D)}, 0, D, 0, 2)
            for h in range(1, rule.m+1):
                rev = Reverse(rule, w, h)
                nodes = set()
                for C, _ in mask_law(rev.U):
                    nodes.update(rev.states(C))
                for k, S, V in sorted(nodes):
                    for d in bits(S[-1] & ~M.closure[0]):
                        p = rev.failure(k, S, V, d)
                        resource, surviving_resource, next_square = Q(0), Q(0), Q(0)
                        for C, prob in mask_law(V):
                            N, queried = rev.transition(k, S, C)
                            V2 = V & ~queried
                            assert rev.transition(k, S, C & queried)[0] == N
                            q = rev.failure(k, S, V2, d)
                            assert p <= q <= 1
                            resource += prob*q*q
                            counts['positive_certificate_checks'] += 1
                            if N[-1] >> d & 1:
                                r = rev.failure(k-1, N, V2, d)
                                assert r >= q
                                surviving_resource += prob*q*q
                                next_square += prob*r*r
                                counts['depleted_event_comparisons'] += 1
                            else:
                                # A completed failure transcript forces failure
                                # even with its positives removed.
                                assert q == 1
                                counts['failure_depletion_checks'] += 1
                        assert resource >= 2*p-p*p
                        assert surviving_resource >= p*(1-p)
                        assert next_square-p*p >= p-2*p*p
                        counts['quadratic_resource_checks'] += 1
                        counts['quadratic_drift_checks'] += 1
                        if p == 0:
                            counts['zero_hazard_nodes'] += 1
                        if p == 1:
                            counts['unit_hazard_nodes'] += 1
                for d in bits(((1 << M.n)-1) & ~M.closure[0]):
                    mean_hazard, mass = Q(0), Q(0)
                    for C, prob in mask_law(rev.U):
                        for k, S, V in rev.states(C):
                            N, _ = rev.transition(k, S, C)
                            if not (N[-1] >> d & 1):
                                p = rev.failure(k, S, V, d)
                                assert p > 0
                                mass += prob
                                mean_hazard += prob*p
                                break
                    assert mass == 1
                    initial = rev.failure(-1, rev.initial, rev.U, d)
                    assert mean_hazard >= (1+initial*initial)/2
                    minimum = min(minimum, mean_hazard)
                    counts['global_quadratic_checks'] += 1
                counts['group_prefixes'] += 1
                rev.transition.cache_clear()
                rev.failure.cache_clear()
        counts['matroid_weight_instances'] += 1
    # Monotone hazards alone do not satisfy this theorem's query hypotheses.
    p = Q(1, 16)
    control = p*(1-(1-p)**64)+(1-p)**64
    assert control < Q(1, 2)
    print(json.dumps({
        'counts': dict(counts),
        'guard_rate': '1/4', 'density_threshold': 2, 'filter_mask': 'H empty',
        'smallest_observed_mean_exit_hazard': str(minimum),
        'negative_control_mean_hazard': str(control),
        'negative_control': 'monotone hazards alone fail the quadratic conclusion',
        'arithmetic': 'exact fractions throughout; no transcendental evaluation',
        'result': 'PASS (finite checks; universal claim rests on the written proof)',
    }, indent=2))


if __name__ == '__main__':
    main()
