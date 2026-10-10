#!/usr/bin/env python3
"""Exact boundary/adaptive-query checks for the new proof ingredients."""
import sys
sys.dont_write_bytecode = True
from collections import Counter
from fractions import Fraction as Q
from functools import lru_cache
from itertools import product
import json

from finite_checks import all_matroids, size
from check_online_rule import subsets, bits
from reverse_support import log_bounds


def increasing_events(n):
    for encoding in range(1 << (1 << n)):
        A = {s for s in range(1 << n) if encoding >> s & 1}
        if all(s | (1 << e) in A for s in A for e in range(n) if not (s >> e & 1)):
            yield A


def query_checks(counts):
    event_counts = []
    for n in range(5):
        number = 0
        for A in increasing_events(n):
            number += 1
            for t in (Q(1, 4), Q(1, 2**16)):
                @lru_cache(None)
                def failure(W, I):
                    return sum((t**size(C)*(1-t)**(size(W)-size(C))
                                for C in subsets(W) if I | C not in A), Q(0))

                def visit(W, I):
                    m, q = failure(W, I), failure(W, 0)
                    assert 0 <= m <= q <= 1
                    if m in (0, 1):
                        if m == 1:
                            assert q == 1
                            return Q(0)
                        assert I in A  # positive certificate
                        return q*q
                    # The choice is predictable and depends on past answers.
                    e = (max if size(I) % 2 else min)(bits(W))
                    W2 = W & ~(1 << e)
                    q2 = failure(W2, 0)
                    m0, m1 = failure(W2, I), failure(W2, I | (1 << e))
                    assert m == (1-t)*m0+t*m1
                    phi = q*q-2*q*m
                    expected_phi2 = q2*q2-2*q2*((1-t)*m0+t*m1)
                    assert expected_phi2-phi == (q2-q)*(q2+q-2*m) >= 0
                    counts['single_query_potential_identities'] += 1
                    return (1-t)*visit(W2, I)+t*visit(W2, I | (1 << e))

                V = (1 << n)-1
                p = failure(V, 0)
                assert visit(V, 0) >= p*(1-p)
                counts['adaptive_event_transactions'] += 1
        event_counts.append(number)
    assert event_counts == [2, 3, 6, 20, 168]
    counts['increasing_events_by_size'] = event_counts


def filter_checks(counts):
    h = Q(3, 4)
    for n in range(5):
        for M in all_matroids(n):
            for w in product((0, 1, 4), repeat=n):
                W = M.optimum(w)
                I = M.greedy(w, (1 << n)-1)
                EY, EU, Egreedy = Q(0), Q(0), Q(0)
                order = sorted(range(n), key=lambda e: (-w[e], e))
                for H in M.sets:
                    prob = h**size(H)*(1-h)**(n-size(H))
                    EY += prob*sum(w[e] for e in bits(I & ~H))
                    Egreedy += prob*sum(w[e] for e in bits(M.greedy(w, H)))
                    higher = 0
                    for e in order:
                        if not (H >> e & 1) and w[e] > 0 and not (M.closure[higher] >> e & 1):
                            EU += prob*w[e]
                        if H >> e & 1:
                            higher |= 1 << e
                assert EY == (1-h)*W
                assert EU == (1-h)/h*Egreedy <= (1-h)/h*W
                counts['biased_filter_vectors'] += 1


def residual_checks(counts):
    for n in range(1, 5):
        if n <= 3:
            families = [[s for s in range(1 << n) if mask >> s & 1]
                        for mask in range(1, 1 << (1 << n))]
        else:
            families = [list(range(1 << n)), [(1 << n)-1]]
            families += [[s for s in range(1 << n) if size(s) == j] for j in range(n+1)]
        for family in families:
            for t in (Q(1, 4), Q(1, 2**16)):
                pO = Q(5, 8)+Q(3, 8)*t
                expected = Q(0)
                for O in range(1 << n):
                    prob = pO**size(O)*(1-pO)**(n-size(O))
                    expected += prob*max([size(R) for R in family if R & ~O == 0] or [0])
                # Compare to a LOWER enclosure of the proved upper bound.
                # These finite instances have enough slack to certify this stronger check.
                bound_lower = (log_bounds(Q(len(family)))[0]+1)/log_bounds(1/pO)[1]
                assert expected <= bound_lower
                counts['selected_residual_expectations'] += 1


def rounding_checks(counts):
    q, L = Q(69, 64), 64
    B = q**L
    factor = (1-1/B)/(L*(q-1))
    for k in (-130, -65, -64, -1, 0, 1, 63, 64, 65, 130):
        for perturbation in (1-Q(1, 2**30), Q(1), 1+Q(1, 2**30), q-Q(1, 2**30)):
            x = q**k*perturbation
            floor_index = k
            while q**floor_index > x:
                floor_index -= 1
            while q**(floor_index+1) <= x:
                floor_index += 1
            values = [q**(j+L*((floor_index-j)//L)) for j in range(L)]
            assert all(0 < u <= x < B*u for u in values)
            assert sum(values)/L >= factor*x
            counts['rational_mesh_boundary_checks'] += 1
    # A single fixed phase cannot support the averaged guarantee.
    x = B-Q(1, 2**30)
    assert 1 < factor*x
    counts['rounding_negative_controls'] += 1


def sharpness_checks(counts):
    # Repeated OR of remaining bits, querying until the first success.
    # At final failure, the hazard is a^(bits after the last positive).
    for n in range(1, 10):
        for t in (Q(1, 4), Q(1, 16)):
            a = 1-t
            expected = Q(0)
            for C in range(1 << n):
                probability = t**size(C)*a**(n-size(C))
                remaining = n if C == 0 else n-1-max(bits(C))
                expected += probability*a**remaining
            formula = a**(2*n)+(1-a**(2*n))/(2-t)
            assert expected == formula >= (1+a**(2*n))/2
            counts['abstract_sharpness_examples'] += 1


def main():
    counts = Counter()
    query_checks(counts)
    filter_checks(counts)
    residual_checks(counts)
    rounding_checks(counts)
    sharpness_checks(counts)
    print(json.dumps({'counts': dict(counts),
                      'arithmetic': 'exact fractions; residual log comparisons use rational intervals',
                      'result': 'PASS (finite ingredient checks, not a universal proof)'}, indent=2))


if __name__ == '__main__':
    main()
