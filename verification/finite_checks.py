#!/usr/bin/env python3
"""Exhaustive small-matroid checks and adversarial negative controls.

These are finite checks of ingredients, not proof of the universal new ratio.
Enumerates independence families directly; no representability assumption.
"""
from fractions import Fraction as Q
from itertools import product
import json


def size(s):
    return bin(s).count('1')


class Matroid:
    def __init__(self, n, independent):
        self.n, self.independent = n, independent
        self.sets = range(1 << n)
        self.rank = [max(size(i) for i in independent if i & s == i) for s in self.sets]
        self.closure = [sum(1 << e for e in range(n)
                            if self.rank[s | (1 << e)] == self.rank[s]) for s in self.sets]
        self.flats = [s for s in self.sets if self.closure[s] == s]

    def optimum(self, w):
        return max(sum(w[e] for e in range(self.n) if i >> e & 1) for i in self.independent)

    def greedy(self, w, available):
        selected = 0
        for e in sorted(range(self.n), key=lambda e: (-w[e], e)):
            if w[e] > 0 and available >> e & 1 and selected | (1 << e) in self.independent:
                selected |= 1 << e
        return selected


def all_matroids(n):
    for encoding in range(1 << ((1 << n)-1)):
        family = {0} | {s for s in range(1, 1 << n) if encoding >> (s-1) & 1}
        if any(s ^ (1 << e) not in family for s in family for e in range(n) if s >> e & 1):
            continue
        if any(not any(i | (1 << e) in family for e in range(n) if (j & ~i) >> e & 1)
               for i in family for j in family if size(i) < size(j)):
            continue
        yield Matroid(n, family)


def rounded(x, b, phase):
    if not x:
        return Q(0)
    k = x.numerator.bit_length() - x.denominator.bit_length()
    if Q(2)**k > x:
        k -= 1
    return Q(2)**(phase + b*((k-phase)//b))


def main():
    counts = dict(matroids=0, density_checks=0, candidate_vectors=0,
                  optimum_rounding_vectors=0, maximum_branch_vectors=0,
                  scalar_boundary_checks=0)
    matroids = [M for n in range(5) for M in all_matroids(n)]
    # This count is an output of direct axiom enumeration, also used as a regression check.
    assert [sum(M.n == n for M in matroids) for n in range(5)] == [1, 2, 5, 16, 68]
    counts['matroids'] = len(matroids)

    for M in matroids:
        n, universe = M.n, (1 << M.n)-1
        # Exercise nontrivial density expansions with small thresholds. The chosen
        # kappa=2^18 would make every expansion trivial at these ground-set sizes.
        for kappa in (2, 4):
            for D in M.sets:
                Qmap = {}
                for P in M.flats:
                    extensions = [Z for Z in M.flats if Z & P == P]
                    best = max(size(D & Z)-kappa*M.rank[Z] for Z in extensions)
                    maximizers = [Z for Z in extensions if size(D & Z)-kappa*M.rank[Z] == best]
                    largest = 0
                    for Z in maximizers:
                        largest |= Z
                    largest = M.closure[largest]
                    assert largest in maximizers
                    Qmap[P] = largest
                    for Z in M.sets:
                        lhs = size(D & (M.closure[largest | Z] & ~largest))
                        rhs = kappa*(M.rank[largest | Z]-M.rank[largest])
                        assert lhs <= rhs
                        counts['density_checks'] += 1
                for P in M.flats:
                    for P2 in M.flats:
                        if P & P2 == P:
                            assert Qmap[P] & Qmap[P2] == Qmap[P]

        for w in product((0, 1, 3, 8), repeat=n):
            W = M.optimum(w)
            opt_set = M.greedy(w, universe)
            mass_y, mass_u, max_reward = 0, 0, 0
            order = sorted(range(n), key=lambda e: (-w[e], e))
            for H in M.sets:
                mass_y += sum(w[e] for e in range(n) if (opt_set & ~H) >> e & 1)
                higher = 0
                for e in order:
                    if not (H >> e & 1) and w[e] > 0 and not (M.closure[higher] >> e & 1):
                        mass_u += w[e]
                    if H >> e & 1:
                        higher |= 1 << e
                eligible = []
                for e in order:
                    if w[e] == 0 or M.rank[1 << e] == 0:
                        continue
                    if H >> e & 1:
                        break
                    eligible.append(w[e])
                # The almighty adversary puts the cheapest eligible label first.
                max_reward += min(eligible) if eligible else 0
            assert 2*mass_y == (1 << n)*W
            assert mass_u <= (1 << n)*W
            maximum = max([w[e] for e in range(n) if M.rank[1 << e]] or [0])
            assert 4*max_reward >= (1 << n)*maximum
            counts['candidate_vectors'] += 1
            counts['maximum_branch_vectors'] += 1

            # All rounded numbers become integers after multiplication by 2^15.
            sum_opt = 0
            for j in range(16):
                scaled = [0 if x == 0 else 2**(15+j+16*((x.bit_length()-1-j)//16)) for x in w]
                sum_opt += M.optimum(scaled)
            assert sum_opt*65536 >= (2**15)*65535*W
            counts['optimum_rounding_vectors'] += 1

    for b in (1, 2, 4, 16, 32):
        factor = Q(2**b-1, b*2**b)
        for k in (-100, -1, 0, 1, 15, 16, 31, 32, 100):
            for offset in (Q(0), Q(1, 2**20), Q(1, 3), 1-Q(1, 2**20)):
                x = Q(2)**k*(1+offset)
                values = [rounded(x, b, j) for j in range(b)]
                assert all(0 < y <= x for y in values)
                assert sum(values)/b >= factor*x
                counts['scalar_boundary_checks'] += 1
    assert rounded(Q(0), 16, 0) == 0

    # Negative control: a fixed unshifted coarse rounding cannot promise this gain.
    x = Q(2**16)-Q(1, 2**20)
    assert rounded(x, 16, 0) < Q(65535, 16*65536)*x
    # Negative control: min E != E min. Uniformly choose first or last arrival.
    H = 2**20
    rewards = ((1, H), (H, 1))  # rows are seeds; columns are the two orders
    minimum_of_means = min(Q(sum(row[col] for row in rewards), 2) for col in range(2))
    mean_of_minima = Q(sum(min(row) for row in rewards), 2)
    assert minimum_of_means == Q(H+1, 2) and mean_of_minima == 1
    counts['negative_controls'] = {
        'unshifted_rounding_rejected': True,
        'fixed_order_minimum_of_means': str(minimum_of_means),
        'seed_visible_mean_of_minima': str(mean_of_minima),
    }
    counts['result'] = 'PASS (finite ingredient checks only)'
    print(json.dumps(counts, indent=2))


if __name__ == '__main__':
    main()
