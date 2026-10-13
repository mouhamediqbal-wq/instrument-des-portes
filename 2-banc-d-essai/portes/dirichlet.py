"""Fonctions L de Dirichlet (caractères réels primitifs χ₃, χ₄, χ₅) par Euler-Maclaurin vectorisé ; § 3.3 filtres de couleur."""
import numpy as np
from scipy.special import loggamma
B=[1/6,-1/30,1/42,-1/30,5/66,-691/2730,7/6]
from math import factorial
def hurwitz(s,a,N):
    # s complexe (tableau), a reel ; Euler-Maclaurin
    n=np.arange(N)[:,None]
    S=np.zeros_like(s)
    for k in range(N): S+=np.exp(-s*np.log(k+a))
    x=N+a; S+=np.exp((1-s)*np.log(x))/(s-1)+0.5*np.exp(-s*np.log(x))
    poch=s.copy(); term_pow=np.exp((-s-1)*np.log(x))
    for j,b in enumerate(B):
        k=j+1  # terme B_{2k}/(2k)! * s(s+1)...(s+2k-2) x^{-s-2k+1}
        S+=b/factorial(2*k)*poch*term_pow
        poch=poch*(s+2*k-1)*(s+2*k); term_pow=term_pow/(x*x)
    return S
def L(s,chi,q,N):
    return sum(chi[a]*hurwitz(s,a/q,N) for a in range(1,q) if chi[a]!=0)*np.exp(-s*np.log(q))
def Zchi(t,chi,q,par):
    s=0.5+1j*t; N=int(max(t.max(),50)/2)+60
    th=np.imag(loggamma((0.5+par+1j*t)/2))+t/2*np.log(q/np.pi)
    v=np.exp(1j*th)*L(s,chi,q,N); return v
CH={'chi3':([0,1,-1],3,1),'chi4':([0,1,0,-1],4,1),'chi5':([0,1,-1,-1,1],5,0)}

def portes_dirichlet(nom, T=1000.0, pas=0.01, morceaux=40):
    chi, q, par = CH[nom]
    ts = np.arange(0.5, T, pas); z = np.empty_like(ts)
    for c in np.array_split(np.arange(len(ts)), morceaux):
        z[c] = np.real(Zchi(ts[c], chi, q, par))
    i = np.nonzero(np.sign(z[:-1])*np.sign(z[1:]) < 0)[0]
    return ts[i] - z[i]*(ts[i+1]-ts[i])/(z[i+1]-z[i])
