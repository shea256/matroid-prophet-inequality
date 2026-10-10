#!/usr/bin/env python3
"""Finite exact checks for retained bases, projected residuals, and accounting.

These checks do not prove the universal theorem. The projected stream
construction adapts check_joint_residual.py; its original affine-sign
checker is reused without changing that historical verifier.
"""
import json
import sys
from collections import Counter
from fractions import Fraction as Q
from itertools import combinations, permutations, product
from math import comb
sys.dont_write_bytecode = True
from finite_checks import all_matroids
from reverse_support import cases
from check_online_rule import Rule, bits, subsets, union
from check_joint_residual import inspect_stream as original_inspect
from check_rank_charged import adaptive_tail_checks


def retained(M, stream):
    span, result = 0, []
    for item in stream:
        if M.rank[span | (1 << item[1])] > M.rank[span]:
            result.append(item)
            span |= 1 << item[1]
    return result


def contracted_old(M, stream, selected):
    span = union(1 << item[1] for item in selected)
    result = []
    for item in stream:
        if item[4] is not None:
            continue
        if M.rank[span | (1 << item[1])] > M.rank[span]:
            result.append(item[0])
            span |= 1 << item[1]
    return set(result)


def inspect_stream(M, stream, variables, counts):
    answer = original_inspect(M, stream, variables, counts)
    basis = retained(M, stream)
    selected = [item for item in basis if item[4] is not None]
    old = {item[0] for item in basis if item[4] is None}
    assert old == contracted_old(M, stream, selected)
    counts['old_basis_reconstructions'] += 1
    # First-stream generators and second-stream witnesses are forced.
    is_first = any(item[0][0] == 'F1' for item in stream)
    role = 'J' if is_first else 'Z'
    required = {item[0] for item in stream if item[4] is not None and item[4][0] == role}
    assert required <= {item[0] for item in selected}
    counts['forced_generator_occurrences' if is_first else 'forced_witness_occurrences'] += len(required)
    if not is_first:
        counts['omitted_second_generators'] += sum(item[4] is not None and item[4][0] == 'J'
                                                  and item not in basis for item in stream)
    return answer


def interleaving_checks(counts):
    for n in range(5):
        for M in all_matroids(n):
            for order in {tuple(range(n)), tuple(reversed(range(n)))}:
                old = [(('old', i), e, 0, 0, None, 0) for i, e in enumerate(order)]
                for s in range(3):
                    for labels in product(range(n), repeat=s):
                        movable = [(('moving', i), e, 0, 0, ('M',i), 1) for i,e in enumerate(labels)]
                        bases = set()
                        by_selected = {}
                        for perm in permutations(movable):
                            for slots in combinations(range(n+s), s):
                                old_it, new_it = iter(old), iter(perm)
                                stream = [next(new_it) if i in slots else next(old_it) for i in range(n+s)]
                                basis = retained(M, stream)
                                selected = [item for item in basis if item[4] is not None]
                                old_ids = {item[0] for item in basis if item[4] is None}
                                assert old_ids == contracted_old(M, stream, selected)
                                key = frozenset(item[0] for item in selected)
                                whole = frozenset(item[0] for item in basis)
                                assert by_selected.setdefault(key, whole) == whole
                                bases.add(whole)
                                counts['arbitrary_interleavings'] += 1
                                if len(selected) < s: counts['redundant_movable_cases'] += 1
                        assert len(bases) <= 2**s
                        counts['basis_family_bounds'] += 1
            counts['matroids_for_interleavings'] += 1


def generating_checks(counts):
    for n in range(11):
        for y in range(n+1):
            for v in (Q(1,2), Q(1,704)):
                a, b = Q(1,4096), Q(1,64)
                mass = Q(0)
                for j in range(n+1):
                    for z in range(y+1):
                        signs = sum(comb(2*y,i) for i in range(min(j+z,2*y)+1))
                        assert v**(j+z)*signs <= (1+v)**(2*y)
                        mass += comb(n,j)*comb(y,z)*6**j*signs*a**j*b**z
                upper = (1+6*a/v)**n*(1+b/v)**y*(1+v)**(2*y)
                assert mass <= upper
                counts['projected_generating_bounds'] += 1
    # A constant tail contribution cannot simply be erased: for a fixed
    # singleton residual with no penalties, expected contained size is 1/2,
    # while log(number of family members) is zero.
    singleton_family = (1,)
    expected = sum((Q(1,2)*max([0]+[len(tuple(bits(R))) for R in singleton_family
                                      if R & ~O == 0]) for O in (0,1)), Q(0))
    assert len(singleton_family) == 1 and expected == Q(1,2) > 0
    counts['uncharged_additive_negative_controls'] += 1
    for B in (Q(3,2), Q(2), Q(5)):
        beta = 1-1/B
        for top in range(-3,4):
            for levels in ({top}, set(range(top-10,top+1)), {top-7,top-3,top}):
                mass = sum((B**i for i in levels),Q(0))
                assert beta*mass <= B**top
                for k in (4,192):
                    assert beta*sum((Q(k-1)*B**i for i in levels),Q(0)) < k*B**top
                counts['additive_and_small_group_weight_bounds'] += 1


def check_group(rule, w, T, parity, h, counts):
    M, a = rule.M, -3*h
    incoming, X = rule.F[h-1], rule.X[h]
    groups = [0]+[sum(1 << e for e in range(M.n) if w[e] == v and rule.candidate(e, v))
                  for v in rule.values]
    G, O = groups[h], rule.D | rule.C
    generators, times = 0, {}
    for k in range(a, 1):
        base = M.closure[incoming[k] | generators]
        for e in bits(rule.Dh[h] & X[k]):
            if not (base >> e & 1):
                generators |= 1 << e
                times[e] = k
                base = M.closure[base | (1 << e)]
        assert base == X[k]
        assert rule.kappa*len(times) <= len(tuple(bits(rule.Dh[h])))
    valid = lambda k: a+2 <= k <= 0 and k % 2 == parity
    b0 = next(k for k in (a-2, a-1) if k % 2 == parity)
    b1 = parity
    competitors, witnesses, residual, z, sigma = {}, {}, 0, 0, 0
    Y = M.greedy(w, (1 << M.n)-1)
    for b in range(b0+2, b1+1, 2):
        K = union(T & groups[j] & rule.X[j][b] & ~rule.X[j][b-1]
                  for j in range(1, h)) if valid(b) else 0
        competitors[b] = K
        assert K & ~incoming[b] == 0
        P = G & X[b] & ~X[b-1] if valid(b) else 0
        base, Z = M.closure[X[b-2] | K], 0
        full_z = M.rank[base | (P & ~O)]-M.rank[base]
        for e in bits(P & ~O & Y):
            if not (base >> e & 1):
                Z |= 1 << e
                base = M.closure[base | (1 << e)]
        witnesses[b] = Z
        local_z = len(tuple(bits(Z)))
        assert local_z <= full_z
        counts['strict_projected_rank_savings'] += int(local_z < full_z)
        z += local_z
        counts['strict_residual_projections'] += int(bool(P & ~base & ~Y))
        residual |= P & Y & ~base
        if valid(b):
            sigma += len(tuple(bits(P & rule.Dh[h] & Y & ~rule.q(h, incoming[b-2] | K))))
    assert residual & ~O == 0
    assert sigma <= rule.kappa*z+len(tuple(bits(residual)))
    # A single x_g is used in both streams; y_z occurs only in the second.
    m, variables = M.n+1, {}
    step = 8*m
    score = lambda k, offset, e: 1 << ((k-a+2)*step+offset*m+e)
    for e, k in times.items():
        variables[('J', e)] = score(k, 6, e)
    for b, Z in witnesses.items():
        for e in bits(Z):
            variables[('Z', e)] = score(b, 2, e)
    first = []
    for k in range(a-2, 2):
        mark = int(valid(k))
        for e in bits(incoming[k]):
            first.append((('F1', k, e), e, mark, (2*mark-1)*score(k, 4, e), None, 0))
        for e in sorted(e for e in times if times[e] == k):
            first.append((('J', e), e, mark, 0, ('J', e), 2*mark-1))
    second = [(('initial', e), e, 0, -score(b0, 4, e), None, 0)
              for e in bits(incoming[b0])]
    for b in range(b0+2, b1+1, 2):
        for e in bits(competitors[b]):
            second.append((('K', b, e), e, 0, -score(b, 0, e), None, 0))
        for e in bits(witnesses[b]):
            second.append((('Z', e), e, 0, 0, ('Z', e), -1))
        for e in bits(incoming[b]):
            second.append((('F2', b, e), e, 1, score(b, 4, e), None, 0))
        for e in sorted(e for e in times if b-2 < times[e] <= b):
            k = times[e]
            scale = 1 << (step*(b-k))
            category = (1 if valid(k) else -1, scale)
            assert category in ((1, 1), (-1, 1), (-1, 1 << step))
            if category == (-1, 1):
                counts['early_invalid_density_occurrences'] += 1
            if scale > 1:
                counts['shifted_density_occurrences'] += 1
            second.append((('J', e), e, 1, 0, ('J', e), scale))
    marks1 = inspect_stream(M, first, variables, counts)
    marks2 = inspect_stream(M, second, variables, counts)
    direct_births = union(G & X[b] & ~X[b-1] for b in range(a+2, 1) if valid(b))
    assert marks1 & G == direct_births
    assert marks1 & marks2 & G & Y == residual
    counts['projected_joint_encodings'] += 1
    j, d, r = len(times), len(tuple(bits(rule.Dh[h]))), len(tuple(bits(residual)))
    mu, nu = Q(1,4), Q(1,2)
    excess = max(Q(0), r-mu*j-nu*z)
    assert sigma <= (rule.kappa+nu)*z+mu*d/rule.kappa+excess
    counts['charged_projected_paths'] += 1
    counts['positive_excess_paths'] += int(excess > 0)
    counts['positive_rank_paths'] += int(z > 0)
    counts['positive_generator_paths'] += int(j > 0)


def main():
    counts = Counter()
    interleaving_checks(counts)
    generating_checks(counts)
    adaptive_tail_checks(counts)
    for M,w in cases():
        U = sum(1 << e for e in range(M.n) if w[e] > 0 and M.rank[1 << e])
        for D in subsets(U):
            for C in subsets(U):
                rule = Rule(M, {e:w[e] for e in bits(D|C)}, 0, D, C, 2)
                if not rule.m: counts['unlisted_outcomes'] += 1
                for h in range(1,rule.m+1):
                    lower = sum(1 << e for e in bits(U) if w[e] < rule.values[h-1])
                    for T in subsets(lower):
                        for parity in (0,1):
                            check_group(rule,w,T,parity,h,counts)
        counts['matroid_weight_instances'] += 1
    for key in ('forced_generator_occurrences','forced_witness_occurrences',
                'omitted_second_generators','strict_projected_rank_savings',
                'strict_residual_projections','positive_excess_paths'):
        assert counts[key] > 0, key
    print(json.dumps(dict(counts=counts,stress_threshold=2,
                          arithmetic='Exact integers/rationals and outward log intervals',
                          result='PASS (finite checks, not a universal proof)'),indent=2))


if __name__ == '__main__':
    main()
