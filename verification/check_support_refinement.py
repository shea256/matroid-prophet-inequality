#!/usr/bin/env python3
"""Exact finite evidence for three-state encoding and restricted overlap.

This exercises actual density paths and greedy supports through the previous
checker. It does not prove the universal counting or prophet theorem.
"""
import json
import sys
from collections import Counter
from fractions import Fraction as Q
from itertools import product
from math import comb
sys.dont_write_bytecode = True
import check_activation_split as previous
from check_online_rule import Rule,bits,subsets
from check_retained_basis import retained
from finite_checks import Matroid


def size(mask):
    return mask.bit_count() if hasattr(mask,'bit_count') else bin(mask).count('1')


def mask_laws(counts):
    for n in range(4):
        E = (1<<n)-1
        for rho,t in ((Q(1,3),Q(1,4)),(Q(93,256),Q(23,2**18))):
            p = rho+(1-rho)*t
            law = previous.joint_law(n,rho,t)
            for roles in product(range(6),repeat=n):
                A,P,N,B,Z = [sum(1<<e for e,r in enumerate(roles) if r==s)
                             for s in range(1,6)]
                J = A|P|N|B
                for Y in subsets(E):
                    if Z & ~Y: continue
                    for R in subsets(Y & ~(A|N|Z)):
                        if P & Y & ~R: continue
                        actual = sum((q for (D,O),q in law.items()
                                      if J & ~D == 0 and Z & O == 0 and R & ~O == 0),Q(0))
                        exact = rho**size(J)*(1-p)**size(Z)*p**size(R & ~J)
                        bound = rho**size(J)*(1-p)**size(Z)*p**(size(R)-size((P|B)&Y))
                        old = rho**size(J)*(1-p)**size(Z)*p**(size(R)-size(J&Y))
                        assert actual == exact and actual <= bound <= old
                        counts['joint_probability_checks'] += 1
                        counts['strict_overlap_savings'] += int(bound < old)
    # A retained valid generator can be in R: the overlap factor remains necessary.
    rho,t = Q(93,256),Q(23,2**18)
    p = rho+(1-rho)*t
    assert rho > rho*p
    counts['naive_no_overlap_negative_controls'] += 1


def generating_checks(counts):
    rho,p = Q(3,8),Q(1,2)
    alpha,beta,chi = Q(1,8),Q(1,32),Q(1,64)
    for n in range(5):
        for y in range(n+1):
            Y = (1<<y)-1
            for v in (Q(1,4),Q(1,624)):
                direct = Q(0)
                for roles in product(range(6),repeat=n):
                    A,P,N,B,Z = [sum(1<<e for e,r in enumerate(roles) if r==s)
                                 for s in range(1,6)]
                    if Z & ~Y: continue
                    j0,j1,z = size(A),size(P|N|B),size(Z)
                    d = j1+z
                    patterns = sum(comb(2*y,i) for i in range(min(d,2*y)+1))
                    direct += (rho**(j0+j1)*(1-p)**z*p**(-size((P|B)&Y))
                               *alpha**j0*beta**j1*chi**z*patterns)
                a,b,c = rho*alpha,rho*beta/v,(1-p)*chi/v
                u = a+3*b
                exact_product = (1+u)**(n-y)*(1+a+b*(1+2/p)+c)**y*(1+v)**(2*y)
                upper = (1+u)**(n-y)*(1+u+Q(2,3)*u*(1/p-1)+c)**y*(1+v)**(2*y)
                assert direct <= exact_product <= upper
                counts['weighted_family_bounds'] += 1


def adaptive_checks(counts):
    for n in range(1,5):
        Y = (1<<n)-1
        for design in range(4):
            family = []
            for R in subsets(Y):
                A = (design<<2) & Y & ~R
                P = R & design
                N = (design<<1) & Y & ~(A|R)
                B = R & (design<<1) & ~P
                Z = design & Y & ~(A|P|N|B|R)
                family.append((A,P,N,B,Z,R))
            family.append((0,0,0,0,0,0))
            for rho,t in ((Q(1,3),Q(1,4)),(Q(93,256),Q(23,2**18))):
                p = rho+(1-rho)*t
                law = previous.joint_law(n,rho,t)
                mass = sum((rho**size(A|P|N|B)*(1-p)**size(Z)*
                            p**(size(A)+2*size(P|N|B)+size(Z)-size(P|B))
                            for A,P,N,B,Z,R in family),Q(0))
                assert mass >= 1
                dist = Counter()
                for (D,O),prob in law.items():
                    excess = max([0]+[size(R)-size(A)-2*size(P|N|B)-size(Z)
                                      for A,P,N,B,Z,R in family
                                      if (A|P|N|B)&~D == 0 and Z&O == 0 and R&~O == 0])
                    dist[excess] += prob
                for x in range(n+1):
                    tail = sum((prob for e,prob in dist.items() if e>x),Q(0))
                    assert tail <= min(1,mass*p**x)
                    counts['adaptive_tail_checks'] += 1
                mean = sum((e*prob for e,prob in dist.items()),Q(0))
                assert mean <= (previous.log_bounds(mass)[1]+1)/previous.log_bounds(1/p)[0]
                counts['adaptive_expectation_checks'] += 1
                counts['positive_adaptive_expectations'] += int(mean>0)


def compressed_paths(counts):
    original = previous.inspect_stream
    pending = []

    def inspect(M,stream,variables,inherited):
        marks = original(M,stream,variables,inherited)
        if not pending:
            pending.append((M,stream,variables.copy(),marks))
            return marks
        old_M,first,first_variables,first_marks = pending.pop()
        assert M is old_M and variables == first_variables
        second_basis = retained(M,stream)
        first_basis = retained(M,first)
        J = {item[4] for item in first if item[4] is not None and item[4][0]=='J'}
        T = {item[4] for item in second_basis if item[4] in J}
        omitted = J-T
        assert omitted.isdisjoint(item[4] for item in second_basis)
        signed = variables.copy()
        for item in first_basis:
            if item[4] in omitted:
                signed[item[4]] = item[5]*variables[item[4]]
                counts['omitted_signed_variables'] += 1
                counts['negative_omitted_signed_variables'] += int(item[5]<0)
        # Recalculate every support sign with the compressed variables.
        for basis,expected in ((first_basis,first_marks),(second_basis,marks)):
            labels = sum(1<<item[1] for item in basis)
            for f in bits(((1<<M.n)-1) & ~M.closure[0]):
                support = [item for item in basis if not
                           (M.closure[labels & ~(1<<item[1])]>>f & 1)]
                value = sum(item[3] if item[4] is None else
                            ((1 if item[4] in omitted else item[5])*signed[item[4]])
                            for item in support)
                assert value != 0 and (value>0)==bool(expected>>f&1)
                counts['compressed_support_signs'] += 1
        residual = marks & first_marks
        for item in first_basis:
            identity,e,mark,constant,key,coefficient = item
            if identity[0]!='J': continue
            if key is None: # activation generator
                assert not (residual>>e & 1)
                counts['activation_exclusions'] += 1
            elif key in T:
                assert bool(residual>>e&1) == bool(mark)
                counts['retained_type_checks'] += 1
            elif residual>>e&1:
                # Omitting the generator does NOT imply its label avoids R.
                counts['omitted_residual_negative_controls'] += 1
        for item in second_basis:
            if item[4] is not None and item[4][0]=='Z':
                assert not (residual>>item[1]&1)
                counts['witness_exclusions'] += 1
        counts['compressed_path_pairs'] += 1
        return marks

    previous.inspect_stream = inspect
    inherited = Counter()
    try:
        previous.path_checks(inherited)
        # A valid-parity generator omitted from the second basis can STILL be
        # residual. Binary vectors (a,g,a+g,a+g), weights (1,2,2,2), density
        # labels {0,1,3}, guard {0}, Y={1,2}. At b=-1, witness 2 followed by
        # old a spans generator 1 with a positive last pivot.
        M = Matroid(4,{s for s in range(16) if size(s)<=2 and s!=12})
        weights,D,C = (1,2,2,2),11,1
        rule = Rule(M,{e:weights[e] for e in bits(D|C)},0,D,C,2)
        previous.check_group(rule,weights,0,1,2,inherited)
    finally:
        previous.inspect_stream = original
    assert not pending
    for name in ('omitted_signed_variables','negative_omitted_signed_variables',
                 'activation_exclusions','retained_type_checks','witness_exclusions',
                 'omitted_residual_negative_controls'):
        assert counts[name]>0,name
    return inherited


def main():
    counts = Counter()
    mask_laws(counts)
    generating_checks(counts)
    adaptive_checks(counts)
    inherited = compressed_paths(counts)
    print(json.dumps(dict(counts=counts,inherited_path_counts=inherited,
                          stress_threshold=2,arithmetic='Exact integers and rational fractions',
                          result='PASS (finite evidence, not a universal proof)'),indent=2))


if __name__ == '__main__':
    main()
