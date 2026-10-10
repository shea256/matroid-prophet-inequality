#!/usr/bin/env python3
"""Exact finite checks of activation splitting and joint mask membership.

Finite evidence only: the universal argument is in the accompanying proof.
All filter masks are tested on the inherited small matroid/weight cases.
"""
import json
import sys
from collections import Counter
from fractions import Fraction as Q
from itertools import product
from math import comb
sys.dont_write_bytecode = True
from reverse_support import cases, log_bounds
from check_online_rule import Rule, bits, subsets, union
from check_retained_basis import retained, contracted_old
from check_joint_residual import inspect_stream


def size(mask):
    return len(tuple(bits(mask)))


def joint_law(n,rho,t):
    full = (1 << n)-1
    law = Counter()
    for D in subsets(full):
        for C in subsets(full):
            law[D,D|C] += rho**size(D)*(1-rho)**(n-size(D))*t**size(C)*(1-t)**(n-size(C))
    assert sum(law.values()) == 1
    return law


def probability_checks(counts):
    for n in range(4):
        full = (1 << n)-1
        for rho,t in ((Q(1,3),Q(1,4)),(Q(3,8),Q(11,2**17))):
            p = rho+(1-rho)*t
            law = joint_law(n,rho,t)
            for Y in subsets(full):
                for roles in product(range(4),repeat=n):
                    J0,J1,Z = (sum(1 << e for e,r in enumerate(roles) if r == k) for k in (1,2,3))
                    if Z & ~Y: continue
                    J = J0|J1
                    for R in subsets(Y & ~Z):
                        actual = sum((prob for (D,O),prob in law.items()
                                      if J & ~D == 0 and Z & O == 0 and R & ~O == 0),Q(0))
                        formula = rho**size(J)*(1-p)**size(Z)*p**size(R & ~J)
                        upper = rho**size(J)*p**(-size(J & Y))*(1-p)**size(Z)*p**size(R)
                        assert actual == formula and actual <= upper
                        counts['joint_membership_probabilities'] += 1
                        counts['generator_residual_overlap_cases'] += int(bool(J & R))
    rho,p = Q(3,8),Q(1,2)
    assert rho > rho*p  # J = R = one label; naive multiplication undercounts.
    counts['overlap_negative_controls'] += 1


def generating_checks(counts):
    rho,p = Q(3,8),Q(1,2)
    a,b,c = Q(1,8),Q(1,16),Q(1,8)
    for n in range(6):
        for y in range(n+1):
            Y = (1 << y)-1
            for v in (Q(1,4),Q(1,648)):
                direct = Q(0)
                for roles in product(range(4),repeat=n):
                    J0,J1,Z = (sum(1 << e for e,r in enumerate(roles) if r == k) for k in (1,2,3))
                    if Z & ~Y: continue
                    j0,j1,z = size(J0),size(J1),size(Z)
                    d = j1+z
                    patterns = sum(comb(2*y,i) for i in range(min(d,2*y)+1))
                    weight = rho**(j0+j1)*p**(-size((J0|J1)&Y))*(1-p)**z
                    direct += weight*a**j0*(4*b)**j1*c**z*patterns
                u,w = rho*(a+4*b/v),(1-p)*c/v
                upper = (1+u)**(n-y)*(1+u/p+w)**y*(1+v)**(2*y)
                assert direct <= upper
                counts['disjoint_role_generating_bounds'] += 1


def adaptive_checks(counts):
    for n in range(1,6):
        Y = (1 << n)-1
        for design in range(4):
            family = [(0,0,0,0)]
            for R in subsets(Y):
                if not R: continue
                J0 = (R & design) | ((design << 1) & Y & ~R)
                J1 = (R >> 1) & Y & ~J0
                Z = (~(R|J0|J1)) & Y & design
                family.append((J0,J1,Z,R))
            for rho,t in ((Q(1,3),Q(1,4)),(Q(3,8),Q(11,2**17))):
                p = rho+(1-rho)*t
                law = joint_law(n,rho,t)
                mass = sum((rho**size(A|B)*p**(-size(A|B))*(1-p)**size(Z)*
                            p**(size(A)+2*size(B)+size(Z)) for A,B,Z,R in family),Q(0))
                assert mass >= 1
                dist = Counter()
                for (D,O),prob in law.items():
                    e = max([0]+[size(R)-size(A)-2*size(B)-size(Z) for A,B,Z,R in family
                                if (A|B)&~D == 0 and Z&O == 0 and R&~O == 0])
                    dist[e] += prob
                for x in range(n+1):
                    tail = sum((prob for e,prob in dist.items() if e>x),Q(0))
                    assert tail <= min(1,mass*p**x)
                    counts['adaptive_membership_tails'] += 1
                mean = sum((e*prob for e,prob in dist.items()),Q(0))
                assert mean <= (log_bounds(mass)[1]+1)/log_bounds(1/p)[0]
                counts['adaptive_membership_expectations'] += 1
                counts['positive_adaptive_expectations'] += int(mean > 0)


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
    Y = M.greedy(w, (1 << M.n)-1) & ~rule.H
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
    early = {e for e,k in times.items() if k == a}
    active = set(times)-early
    assert all(times[e] >= a+2 for e in active)
    assert len(early) == M.rank[X[a]]
    assert X[a] == X[a+1] == rule.q(h, M.closure[0])
    assert all(times[e] == a for e in early)
    # Freeze activation generators as old occurrences in both streams.
    def freeze(stream):
        result = []
        for identity,label,mark,constant,key,factor in stream:
            if key is not None and key[0] == 'J' and key[1] in early:
                constant += factor*variables[key]
                key, factor = None, 0
            result.append((identity,label,mark,constant,key,factor))
        return result
    first, second = freeze(first), freeze(second)
    for e in early:
        del variables[('J',e)]
    for stream_number,stream in enumerate((first,second)):
        selected = retained(M,stream)
        ids = {item[0] for item in selected}
        assert {('J',e) for e in early} <= ids
        if stream_number == 0:
            assert {('J',e) for e in active} <= ids
        else:
            assert {('Z',e) for Z in witnesses.values() for e in bits(Z)} <= ids
            counts['omitted_active_second_generators'] += len({('J',e) for e in active}-ids)
        movable = [item for item in selected if item[4] is not None]
        assert {item[0] for item in selected if item[4] is None} == contracted_old(M,stream,movable)
        counts['activation_fixed_basis_checks'] += 1
    for item in second:
        if item[4] is not None and item[4][0] == 'J':
            e = item[4][1]
            kind = (1 if valid(times[e]) else -1,item[5])
            assert kind in ((1,1),(-1,1 << step))
            counts['active_generator_occurrences'] += 1
    marks1 = inspect_stream(M, first, variables, counts)
    marks2 = inspect_stream(M, second, variables, counts)
    direct_births = union(G & X[b] & ~X[b-1] for b in range(a+2, 1) if valid(b))
    assert marks1 & G == direct_births
    assert marks1 & marks2 & G & Y == residual
    counts['projected_joint_encodings'] += 1
    j, d, r = len(times), len(tuple(bits(rule.Dh[h]))), len(tuple(bits(residual)))
    j0, j1 = len(early),len(active)
    mu, nu = Q(3,4),Q(1,2)
    excess = max(Q(0),r-(mu-Q(1,4))*j0-mu*j1-nu*z)
    assert sigma+Q(j0,4) <= (rule.kappa+nu)*z+mu*d/rule.kappa+excess
    counts['activation_generator_occurrences'] += j0
    counts['nonempty_filter_paths'] += int(bool(rule.H))
    counts['charged_projected_paths'] += 1
    counts['positive_excess_paths'] += int(excess > 0)
    counts['positive_rank_paths'] += int(z > 0)
    counts['positive_generator_paths'] += int(j > 0)


    return sigma, len(early), len(tuple(bits(rule.Dh[h] & Y & X[a])))


def path_checks(counts):
    rate = Q(1,4)
    for M,w in cases():
        E = (1 << M.n)-1
        optimum = M.greedy(w,E)
        for H in subsets(E):
            probe = Rule(M,{e:w[e] for e in bits(H)},H,0,0,2)
            U = sum(1 << e for e in range(M.n) if probe.candidate(e,w[e]))
            Y = optimum & ~H
            for D in subsets(U):
                safety, baseline = Counter(),{}
                for C in subsets(U):
                    probC = rate**size(C)*(1-rate)**(size(U)-size(C))
                    rule = Rule(M,{e:w[e] for e in bits(H|D|C)},H,D,C,2)
                    if not rule.m: counts['unlisted_outcomes'] += 1
                    for h in range(1,rule.m+1):
                        lower = sum(1 << e for e in bits(U) if w[e]<rule.values[h-1])
                        for T in subsets(lower):
                            probT = rate**size(T)*(1-rate)**(size(lower)-size(T))
                            for parity in (0,1):
                                sigma,j0,discarded = check_group(rule,w,T,parity,h,counts)
                                record = (size(rule.Dh[h]&Y),j0,discarded)
                                assert baseline.setdefault(h,record) == record
                                assert discarded <= j0
                                safety[h] += probC*probT*sigma/2
                for h,(dY,j0,discarded) in baseline.items():
                    assert safety[h] >= Q(dY-discarded,4) >= Q(dY-j0,4)
                    counts['conditional_activation_safety_bounds'] += 1
                    counts['positive_activation_safety_bounds'] += int(dY>discarded)
            counts['filter_configurations'] += 1
        counts['matroid_weight_instances'] += 1


def main():
    counts = Counter()
    probability_checks(counts)
    generating_checks(counts)
    adaptive_checks(counts)
    path_checks(counts)
    for key in ('activation_generator_occurrences','active_generator_occurrences',
                'nonempty_filter_paths','generator_residual_overlap_cases',
                'positive_activation_safety_bounds','positive_excess_paths',
                'positive_adaptive_expectations','omitted_active_second_generators'):
        assert counts[key] > 0,key
    print(json.dumps(dict(counts=counts,stress_threshold=2,
                          filter_masks='all masks on the stated finite cases',
                          safety_guard_and_test_rate='1/4',
                          arithmetic='Exact rationals; outward log intervals for tail integrals',
                          result='PASS (finite evidence; not a universal proof)'),indent=2))


if __name__ == '__main__':
    main()
