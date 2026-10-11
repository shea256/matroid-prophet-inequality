#!/usr/bin/env python3
"""Numerical discovery for support-aware residual counts; not a proof/ceiling."""
import json
import math
import random


def evaluate(x, mode):
    lk, lt, rho, h, lb, lu, lw, lv = x
    if not (math.log(4)<lk<14 and -24<lt<-2 and .01<rho<.99
            and .1<h<.99 and .5<lb<12 and all(-30<a<0 for a in (lu,lw,lv))):
        return -1, {}
    k,t,B,u,w,v = map(math.exp,(lk,lt,lb,lu,lw,lv))
    p = rho+(1-rho)*t
    lam = -math.log(p)
    states = 3 if mode in ('compressed','support') else 4
    mu = math.log(rho*(states+v*math.exp(lam/4))/(u*v))/lam
    nu = math.log((1-p)/(w*v))/lam
    a = rho*math.exp(-lam*(mu-.25))
    b = rho*math.exp(-lam*mu)/v
    if mode == 'baseline':
        y_factor = 1+u/p+w
    elif mode == 'overlap':
        y_factor = 1+a+2*b*(1+1/p)+w
    elif mode == 'compressed':
        y_factor = 1+a+b*(1+2/p)+w
    else:
        y_factor = 1+(a+b*(1+1/p)+w)/(1+v)**2+b/p
    gamma = rho/4-(math.log(y_factor)-math.log1p(u)+2*math.log1p(v))/lam
    error = mu*rho/k+math.log1p(u)/lam
    K = k+nu
    if gamma<=0 or (1-t)*(gamma*k+1/lam)/K>.25:
        return -1, {}
    loss = error+K*t+(K*t+K*rho/k)/(B-1)
    slack = (1-h)*(gamma-loss/h)
    coefficient = (1-t)*(1-1/B)**2*t*slack/(256*math.expm1(lb/256)*K)
    return coefficient,dict(kappa=k,t=t,rho=rho,h=h,B=B,u=u,w=w,v=v,
                           mu=mu,nu=nu,gamma=gamma,error=error,slack=slack)


def search(mode, starts=24):
    rng = random.Random(11134)
    best = (-1,None)
    for i in range(starts):
        x = [math.log(176),math.log(11/2**17),3/8,.75,math.log(140),
             math.log(1/1056),math.log(1/4096),math.log(1/648)] if i==0 else [
                 math.log(rng.uniform(100,300)),rng.uniform(-11,-8),
                 rng.uniform(.3,.55),rng.uniform(.65,.9),rng.uniform(3,6),
                 math.log(rng.uniform(.0007,.002)),math.log(.0002),math.log(.001)]
        steps = [.3,.3,.04,.04,.3,.4,.4,.4]
        while max(steps)>1e-7:
            improved = False
            for j in range(8):
                for sign in (-1,1):
                    trial = x[:]
                    trial[j] += sign*steps[j]
                    if evaluate(trial,mode)[0] > evaluate(x,mode)[0]:
                        x = trial
                        improved = True
            if not improved:
                steps = [s*.6 for s in steps]
        c,params = evaluate(x,mode)
        if c > best[0]:
            best = c,params
    return dict(mode=mode,coefficient=best[0],ratio_2_minus_31=best[0]*2**31,
                parameters=best[1])


if __name__ == '__main__':
    print(json.dumps(dict(seed=11134,starts_per_mode=24,phases=256,
                         scope='Floating-point discovery, not proof or optimum',
                         attacks=[search(m) for m in ('baseline','overlap','compressed','support')]),indent=2))
