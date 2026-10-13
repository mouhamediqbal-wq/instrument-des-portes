"""§ 2.1 La courbure : l'angle de Riemann-Siegel."""
import numpy as np

def theta(t):
    """θ(t) = (t/2) ln(t/2π) − t/2 − π/8 + 1/(48t) + 7/(5760 t³)."""
    t = np.asarray(t, dtype=float)
    return t/2*np.log(t/(2*np.pi)) - t/2 - np.pi/8 + 1/(48*t) + 7/(5760*t**3)

def ecart_local(t):
    """Écart moyen entre portes à la hauteur t : 2π / ln(t/2π)."""
    return 2*np.pi/np.log(np.asarray(t, dtype=float)/(2*np.pi))
