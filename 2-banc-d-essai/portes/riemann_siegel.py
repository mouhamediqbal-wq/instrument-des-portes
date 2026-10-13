"""Référence indépendante : Z(t) de Riemann-Siegel (termes C0, C1), pour calculer les vraies portes."""
import numpy as np
from .courbure import theta

def _psi(q):
    return np.cos(2*np.pi*(q**2 - q - 1/16))/np.cos(2*np.pi*q)

def Z(t):
    t = np.atleast_1d(np.asarray(t, dtype=float))
    a = np.sqrt(t/(2*np.pi)); N = np.floor(a).astype(int); p = a - N; th = theta(t)
    s = np.zeros_like(t)
    for n in range(1, N.max()+1):
        s += np.where(n <= N, 2/np.sqrt(n)*np.cos(th - t*np.log(n)), 0.0)
    h = 1e-3
    C0 = _psi(p)
    C1 = -((_psi(p+2*h) - 2*_psi(p+h) + 2*_psi(p-h) - _psi(p-2*h))/(2*h**3))/(96*np.pi**2)
    return s + (-1.0)**(N-1)*a**-0.5*(C0 + C1/a)

def changements_de_signe(t, v):
    i = np.nonzero(np.sign(v[:-1])*np.sign(v[1:]) < 0)[0]
    return t[i] - v[i]*(t[i+1]-t[i])/(v[i+1]-v[i])

def portes_riemann_siegel(a, b, pas=0.001, morceaux=40):
    t = np.arange(a, b, pas)
    v = np.concatenate([Z(c) for c in np.array_split(t, morceaux)])
    return changements_de_signe(t, v)
