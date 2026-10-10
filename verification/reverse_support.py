#!/usr/bin/env python3
"""Shared exact reverse-process models, finite cases, and rational log bounds."""
import sys
sys.dont_write_bytecode = True
from fractions import Fraction as Q
from functools import lru_cache
from itertools import product

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
