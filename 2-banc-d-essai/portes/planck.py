"""§ 4 La constante d'échange : une porte par case de Planck (h = 2π)."""
import numpy as np
from scipy.optimize import minimize_scalar

def cases_de_planck(E, h=2*np.pi):
    """(E/h)(ln(E/h) − 1) + 7/8 : aire sous xp = E (ℓx·ℓp = h) divisée par h, moins 1/8."""
    E = np.asarray(E, dtype=float)
    return (E/h)*(np.log(E/h) - 1) + 7/8

def ajuster_h(gammas):
    g = np.sort(np.asarray(gammas, dtype=float)); n = np.arange(1, len(g)+1)
    r = minimize_scalar(lambda h: np.sum(((n-0.5) - cases_de_planck(g, h))**2), bounds=(5, 8), method='bounded')
    return r.x
