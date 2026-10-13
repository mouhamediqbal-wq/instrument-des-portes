"""§ 3 Le spectromètre : des portes vers les premiers."""
import numpy as np

def reponse(x, gammas, T=None):
    """§ 3.2 R(x) = −(4π/T)·√x·Σ cos²(πγ/2T)·cos(γ ln x)."""
    g = np.asarray(gammas, dtype=float)
    if T is None: T = g.max() + 0.5
    w = np.cos(np.pi*g/(2*T))**2; x = np.atleast_1d(np.asarray(x, dtype=float))
    return -(4*np.pi/T)*np.sqrt(x)*(w[None, :]*np.cos(np.outer(np.log(x), g))).sum(1)

def lire_premiers(gammas, nmax, T=None):
    """§ 3.4 Λ̂(n) et la liste des n déclarés premiers, à partir des portes seules."""
    g = np.asarray(gammas, dtype=float)
    if T is None: T = g.max() + 0.5
    w = np.cos(np.pi*g/(2*T))**2; rho = 0.5 + 1j*g
    def psi(x):
        x = np.atleast_1d(x)[:, None]
        s = 2*np.real(w[None, :]*np.exp(rho[None, :]*np.log(x))/rho[None, :]).sum(1)
        x = x[:, 0]; return x - s - np.log(2*np.pi) - 0.5*np.log(1 - x**-2.0)
    N = np.arange(2, nmax+1); L = psi(N+0.5) - psi(N-0.5)
    return N, L, N[(L > 0.35) & (L > 0.75*np.log(N))]
