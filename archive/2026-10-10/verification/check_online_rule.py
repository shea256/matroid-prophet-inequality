#!/usr/bin/env python3
"""Exact small-instance checks of the online rule and order-uniform lemmas.

Uses small kappa to exercise density expansions. This does not certify the
universal theorem or execute it on a large matroid at kappa=2**18.
Only revealed weights enter preparation; other weights enter on arrival.
"""
import sys
sys.dont_write_bytecode = True
from collections import Counter
from fractions import Fraction as Q
from itertools import permutations, product
import json

from finite_checks import Matroid, all_matroids, size


def subsets(s):
    a = s
    while True:
        yield a
        if not a:
            break
        a = (a-1) & s


def bits(s):
    while s:
        bit = s & -s
        yield bit.bit_length()-1
        s ^= bit


def union(sets):
    result = 0
    for s in sets:
        result |= s
    return result


class Rule:
    def __init__(self, M, revealed, H, D, C, kappa):
        self.M, self.H, self.D, self.C, self.kappa = M, H, D, C, kappa
        self.revealed = revealed
        assert set(revealed) == set(bits(H | D | C))
        self.values = sorted({revealed[e] for e in bits(D)
                              if self.candidate(e, revealed[e])})
        self.m = len(self.values)
        self.lo = -3*self.m-2
        self.Dh = [0] + [sum(1 << e for e in bits(D)
                             if revealed[e] == v and self.candidate(e, v))
                         for v in self.values]
        self.Ch = [0] + [sum(1 << e for e in bits(C)
                             if revealed[e] == v and self.candidate(e, v))
                         for v in self.values]
        self.qmaps = [{}]
        for Dg in self.Dh[1:]:
            qmap = {}
            for P in M.flats:
                choices = [Z for Z in M.flats if P & ~Z == 0]
                best = max(size(Dg & Z)-kappa*M.rank[Z] for Z in choices)
                qmap[P] = M.closure[union(Z for Z in choices
                                         if size(Dg & Z)-kappa*M.rank[Z] == best)]
            self.qmaps.append(qmap)
        E, L = (1 << M.n)-1, M.closure[0]
        self.X = [{}]
        self.F = [{k: (L if k < 0 else E) for k in range(self.lo, 2)}]
        for h in range(1, self.m+1):
            X = {k: self.q(h, self.F[h-1][k]) if k >= -3*h else self.F[h-1][k]
                 for k in range(self.lo, 2)}
            F = {k: M.closure[X[k] | (self.Ch[h] & X[k+1])]
                 for k in range(self.lo, 1)}
            F[1] = E
            self.X.append(X)
            self.F.append(F)

    def candidate(self, e, value):
        if self.H >> e & 1 or value <= 0:
            return False
        higher = sum(1 << f for f in bits(self.H)
                     if (-self.revealed[f], f) < (-value, e))
        return not (self.M.closure[higher] >> e & 1)

    def q(self, h, P):
        return self.qmaps[h][self.M.closure[P]]

    def birth(self, h, e):
        return next(k for k in range(-3*h, 1) if self.X[h][k] >> e & 1)

    def run(self, arrivals, T, parity):
        accepted, layers = 0, {}
        for e, value in arrivals:
            if (self.H | self.D | self.C) >> e & 1:
                continue
            if not self.candidate(e, value) or value not in self.values:
                continue
            h = self.values.index(value)+1
            b = self.birth(h, e)
            if b < -3*h+2 or b % 2 != parity or not (T >> e & 1):
                continue
            base = self.F[-1][b-2] | layers.get(b, 0)
            if self.M.rank[base | (1 << e)] > self.M.rank[base]:
                layers[b] = layers.get(b, 0) | (1 << e)
                accepted |= 1 << e
                assert accepted in self.M.independent  # every accepted prefix
        return accepted

    def statistics(self, w, T, parity, Y):
        M, O = self.M, self.D | self.C
        rank = lambda S, P: M.rank[S | P]-M.rank[P]
        G = [0] + [sum(1 << e for e in range(M.n)
                      if w[e] == v and self.candidate(e, v)) for v in self.values]
        rows = []
        for h in range(1, self.m+1):
            sigma, z, lam, final_rank = 0, 0, 0, 0
            for b in range(-3*h+2, 1):
                if b % 2 != parity:
                    continue
                P = G[h] & self.X[h][b] & ~self.X[h][b-1]
                K = union(T & G[j] & self.X[j][b] & ~self.X[j][b-1]
                          for j in range(1, h))
                assert K & ~self.F[h-1][b] == 0
                sigma += size(P & self.Dh[h] & Y & ~self.q(h, self.F[h-1][b-2] | K))
                z += rank(P & ~O, self.X[h][b-2] | K)
                final_rank += rank(P & ~O, self.F[-1][b-2] | K)
                lam += rank(P & ~O & T, self.F[-1][b-2] | K)
            cost = Q(size(self.Ch[h])) + sum(
                (size(self.Ch[j]) + Q(size(self.Dh[j]), self.kappa)
                 for j in range(h+1, self.m+1)), Q(0))
            assert final_rank >= z-cost
            rows.append((self.values[h-1], sigma, z, lam))
        return rows

    def check_paths(self, counts):
        M = self.M
        for h in range(1, self.m+1):
            generators = 0
            for k in range(-3*h, 1):
                assert self.F[h-1][k] & ~self.X[h][k] == 0
                assert self.X[h][k] & ~self.F[h][k] == 0
                assert self.F[h][k] & ~self.X[h][k+1] == 0
                assert self.X[h][k-1] & ~self.X[h][k] == 0
                if self.X[h][k] != self.F[h-1][k]:
                    counts['nontrivial_density_states'] += 1
                if self.F[h][k] != self.X[h][k]:
                    counts['nontrivial_guard_states'] += 1
                base = M.closure[self.F[h-1][k] | generators]
                for e in bits(self.Dh[h] & self.X[h][k]):
                    if not (base >> e & 1):
                        generators |= 1 << e
                        base = M.closure[base | (1 << e)]
                assert base == self.X[h][k]
                assert self.kappa*size(generators) <= size(self.Dh[h])
            assert self.X[h][-3*h] == self.X[h][-3*h+1]


def cases():
    # All labeled matroids through n=3; positive ties, multiple levels, and zeros.
    for n in range(4):
        for M in all_matroids(n):
            weights = set(product((1, 4), repeat=n))
            weights.add((0,)*n)
            weights.add(tuple(0 if e == 0 else 4 for e in range(n)))
            for w in sorted(weights):
                yield M, w, 2
    # Larger targeted examples exercise multiple groups, parallelism, and circuits.
    n = 4
    families = [set(s for s in range(16) if size(s) <= r) for r in (1, 2, 3, 4)]
    families.append(set(s for s in range(16) if size(s & 3) <= 1 and size(s & 12) <= 1))
    families.append(set(s for s in range(8) if size(s) <= 2))  # triangle plus loop
    for independent in families:
        M = Matroid(n, independent)
        for w in ((1, 1, 4, 4), (1, 4, 16, 64), (0, 1, 1, 4)):
            yield M, w, 2
    # Check the actual large density threshold on small instances too.
    for independent in families:
        yield Matroid(n, independent), (1, 1, 4, 4), 2**18


def main():
    counts = Counter()
    minimum_positive = None
    # Quarter-rate C,T stress the parameter-uniform safety argument. At t=1/4
    # the product probability of O is still at most 1/2. Masks outside U are
    # marginalized exactly: neither decisions nor analysis depends on their bits.
    for M, w, kappa in cases():
        n, E = M.n, (1 << M.n)-1
        orders = list(permutations(range(n)))
        optimum_set = M.greedy(w, E)
        expected_worst = Q(0)
        for H in M.sets:
            probe = Rule(M, {e: w[e] for e in bits(H)}, H, 0, 0, kappa)
            U = sum(1 << e for e in range(n) if probe.candidate(e, w[e]))
            Y = optimum_set & ~H
            u = size(U)
            for D in subsets(U):
                safe_total = Counter()
                for C in subsets(U):
                    rule = Rule(M, {e: w[e] for e in bits(H | D | C)}, H, D, C, kappa)
                    rule.check_paths(counts)
                    counts['prepared_rules'] += 1
                    for T in subsets(U):
                        ct_numerator = 3**(2*u-size(C)-size(T))
                        dct_numerator = ct_numerator * 3**(u-size(D))
                        for parity in (0, 1):
                            rows = rule.statistics(w, T, parity, Y)
                            for value, sigma, z, lam in rows:
                                safe_total[value] += ct_numerator*sigma
                            rewards = []
                            for order in orders:
                                A = rule.run(((e, w[e]) for e in order), T, parity)
                                for value, sigma, z, lam in rows:
                                    assert sum(w[e] >= value for e in bits(A)) >= lam
                                    counts['order_uniform_inequalities'] += 1
                                rewards.append(sum(w[e] for e in bits(A)))
                                counts['order_runs'] += 1
                            worst = min(rewards)
                            expected_worst += Q(dct_numerator*worst, 2**n * 2 * 4**(3*u))
                            counts['seed_states'] += 1
                # Conditional on H,D; only C,T and parity are averaged here.
                for value in probe.values + sorted({w[e] for e in bits(D)}):
                    Dg = sum(1 << e for e in bits(D) if w[e] == value)
                    lower = Q(7, 640)*size(Dg & Y)-Q(size(Dg), 2*kappa)
                    assert Q(safe_total[value], 2*4**(2*u)) >= lower
                    counts['conditional_safety_inequalities'] += 1
        W = M.optimum(w)
        assert 0 <= expected_worst <= W
        if expected_worst and W:
            ratio = expected_worst/W
            minimum_positive = ratio if minimum_positive is None else min(minimum_positive, ratio)
        counts['instances'] += 1
    assert counts['nontrivial_density_states'] and counts['nontrivial_guard_states']
    print(json.dumps({
        'counts': dict(counts),
        'guard_and_test_rate': '1/4 (stress-test rate, not proposed 2^-29)',
        'density_thresholds': [2, 2**18],
        'minimum_positive_main_ratio_in_test_set': str(minimum_positive),
        'result': 'PASS (finite exact checks; not universal proof or performance claim)',
    }, indent=2))


if __name__ == '__main__':
    main()
