#!/usr/bin/env python3
"""Exact finite checks of joint affine encoding on actual source paths.

Small thresholds exercise generators that the final threshold would hide.
These checks do not prove the uniform counting theorem.
"""
import json
import sys
from collections import Counter
from fractions import Fraction as Q
from math import comb

sys.dont_write_bytecode = True
from reverse_support import cases
from check_online_rule import Rule, bits, subsets, union
from finite_checks import Matroid


def inspect_stream(M, stream, variables, counts):
    # Each occurrence is (id, label, mark, constant, variable, coefficient).
    selected, basis, marks, previous_score = 0, [], {}, 0
    for item in stream:
        name, e, mark, constant, var, coefficient = item
        score = constant if var is None else coefficient*variables[var]
        assert (score > 0) == bool(mark)
        assert abs(score) > previous_score
        previous_score = abs(score)
        before = M.closure[selected]
        if not (before >> e & 1):
            basis.append(item)
            selected |= 1 << e
        for f in bits(M.closure[selected] & ~before):
            marks[f] = mark
    assert M.rank[selected] == M.rank[-1]
    # The retained old occurrences can differ from old-only greedy only at
    # the rank-drop positions in the source marked-pivot argument.
    old_basis, old_span = [], 0
    movables = union(1 << item[1] for item in stream if item[4] is not None)
    optional = set()
    for item in stream:
        if item[4] is not None:
            continue
        _, e, *_ = item
        if M.rank[old_span | (1 << e)] > M.rank[old_span]:
            if M.rank[old_span | movables | (1 << e)] == M.rank[old_span | movables]:
                optional.add(item[0])
            old_basis.append(item[0])
            old_span |= 1 << e
    retained_old = {v[0] for v in basis if v[4] is None}
    assert retained_old <= set(old_basis)
    assert set(old_basis)-retained_old <= optional
    assert len(optional) <= sum(v[4] is not None for v in stream)
    for f in bits(((1 << M.n)-1) & ~M.closure[0]):
        support = [v for v in basis if not
                   (M.closure[selected & ~(1 << v[1])] >> f & 1)]
        assert support
        constants = sum(v[3] for v in support if v[4] is None)
        affine = constants+sum(v[5]*variables[v[4]] for v in support if v[4] is not None)
        assert affine != 0 and (affine > 0) == bool(marks[f])
        counts['affine_pivot_signs'] += 1
        # Wrongly omitting the shift must fail on at least one tested path.
        wrong = constants+sum((1 if v[4][0] == 'J' and v[5] > 1 else v[5])
                              *variables[v[4]] for v in support if v[4] is not None)
        if (wrong > 0) != bool(marks[f]):
            counts['missing_shift_negative_controls'] += 1
    return sum(1 << e for e, mark in marks.items() if mark)


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
        for e in bits(P & ~O):
            if not (base >> e & 1):
                Z |= 1 << e
                base = M.closure[base | (1 << e)]
        witnesses[b] = Z
        z += len(tuple(bits(Z)))
        residual |= P & ~base
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
    assert marks1 & marks2 & G == residual
    counts['joint_residual_encodings'] += 1


def tail_checks(counts):
    rho, cap = Q(7, 16), Q(33, 64)
    tilt = cap*(1-rho)/(rho*(1-cap))
    moment = 1-rho+rho*tilt
    for n in range(1, 49):
        tail = sum((Q(comb(n, j))*rho**j*(1-rho)**(n-j)
                    for j in range(n+1) if j > cap*n), Q(0))
        assert tail**64 <= moment**(64*n)/tilt**(33*n)
        counts['exact_binomial_chernoff_checks'] += 1
    # Both binomial-sum bounds are valid with floors, including q=0.
    for n in list(range(1, 33))+[639, 640, 1241, 1242, 1243, 1280, 2482, 2483]:
        for k in (4, 8, 640):
            q = int(cap*n/k)
            alpha = cap/k
            S = sum(comb(n, j) for j in range(q+1))
            S2 = sum(comb(2*n, j) for j in range(2*q+1))
            # These stronger floor-exponent inequalities imply the desired
            # real-exponent versions since alpha<1 and q<=alpha*n.
            assert alpha**q*S <= (1+alpha)**n
            assert alpha**(2*q)*S2 <= (1+alpha)**(2*n)
            counts['floor_binomial_sum_checks'] += 1


def phase_checks(counts):
    theta, L = Q(261, 256), 256
    B = theta**L
    factor = (1-1/B)/(L*(theta-1))
    for k in (-257, -256, -1, 0, 1, 255, 256, 257):
        for delta in (-Q(1, 2**30), Q(0), Q(1, 2**30)):
            x = theta**k*(1+delta)
            floor_index = k-1 if delta < 0 else k
            values = [theta**(j+L*((floor_index-j)//L)) for j in range(L)]
            assert all(0 < u <= x < B*u for u in values)
            assert sum(values)/L >= factor*x
            counts['new_phase_boundary_checks'] += 1


def main():
    counts = Counter()
    for M, w in cases():
        U = sum(1 << e for e in range(M.n) if w[e] > 0 and M.rank[1 << e])
        for D in subsets(U):
            for C in subsets(U):
                rule = Rule(M, {e: w[e] for e in bits(D | C)}, 0, D, C, 2)
                for h in range(1, rule.m+1):
                    # Only lower groups' test bits occur in this residual.
                    lower = sum(1 << e for e in bits(U) if w[e] < rule.values[h-1])
                    for T in subsets(lower):
                        for parity in (0, 1):
                            check_group(rule, w, T, parity, h, counts)
        counts['matroid_weight_instances'] += 1
    # A fixed triangle support containing one negative old occurrence and
    # one positive moved generator detects loss of the score multiplier.
    triangle = Matroid(3, set(range(7)))
    stream = [('old0', 0, 0, -(1 << 10), None, 0),
              ('gen', 1, 1, 0, ('J', 1), 1 << 8),
              ('old1', 1, 1, 1 << 14, None, 0),
              ('old2', 2, 1, 1 << 15, None, 0)]
    before = counts['missing_shift_negative_controls']
    inspect_stream(triangle, stream, {('J', 1): 1 << 4}, counts)
    assert counts['missing_shift_negative_controls'] > before
    tail_checks(counts)
    phase_checks(counts)
    assert counts['missing_shift_negative_controls'] > 0
    assert counts['early_invalid_density_occurrences'] > 0
    assert counts['shifted_density_occurrences'] > 0
    print(json.dumps({'counts': dict(counts), 'stress_threshold': 2,
                      'arithmetic': 'exact integers and rational fractions',
                      'result': 'PASS (finite joint-encoding checks, not universal proof)'}, indent=2))


if __name__ == '__main__':
    main()
