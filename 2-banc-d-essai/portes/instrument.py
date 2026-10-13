"""§ 2 L'instrument : des premiers vers les portes (courbure + deux fentes égales + cavités)."""
import numpy as np
from .courbure import theta, ecart_local
from .premiers import crible
from .riemann_siegel import changements_de_signe

def _poids(bord, u, ln2):
    """§ 2.4 Pondération du bord ; u = ln n / ln X ; ln2 = ln 2 / ln X (largeur d'une octave en u)."""
    if u <= 1: return 1.0
    d = (u - 1)/ln2          # distance au bord, en octaves
    if bord == 'net':        return 0.0
    if bord == 'arrondi':    return 0.5*(1+np.cos(np.pi*d)) if d < 1 else 0.0
    if bord == 'ebrasement': return 0.5*(1+np.cos(np.pi*d/2)) if d < 2 else 0.0
    if bord == 'reflecteur': return 0.5 if d <= 1 else (0.25*(1+np.cos(np.pi*(d-1))) if d < 2 else 0.0)
    raise ValueError(bord)

def phase_cavites(t, X, bord='arrondi', echos=True):
    """§ 2.3 Φ(t) : somme des cavités premières (tous les échos m si echos=True, sinon m = 1)."""
    t = np.asarray(t, dtype=float); LX = np.log(X); ln2 = np.log(2)/LX
    portee = {'net': 1, 'arrondi': 2, 'ebrasement': 4, 'reflecteur': 4}[bord]
    phi = np.zeros_like(t)
    for p in crible(int(portee*X)):
        lp = np.log(p); m = 1
        while True:
            amp = p**(-m/2)/m
            if amp < 1e-9 or m*lp > np.log(portee*X) + 1e-9 or (not echos and m > 1):
                break
            w = _poids(bord, m*lp/LX, ln2)
            if w > 0:
                phi += w*amp*np.sin(-m*t*lp)
            m += 1
    return phi

def portes_instrument(a, b, X=None, bord='arrondi', pas=0.002, echos=True):
    """§ 2.5 Portes jouées par l'instrument dans [a, b] ; X = t/2π au centre par défaut (règle d'horloger)."""
    t = np.arange(a, b, pas)
    if X is None: X = (a+b)/2/(2*np.pi)
    return changements_de_signe(t, np.cos(theta(t) + phase_cavites(t, X, bord, echos)))

def apparier(notes, vraies):
    """Distance (en écarts locaux) de chaque vraie porte à la note la plus proche."""
    notes = np.sort(notes); j = np.clip(np.searchsorted(notes, vraies), 1, len(notes)-1)
    d = np.minimum(abs(notes[j]-vraies), abs(notes[j-1]-vraies))
    return d/ecart_local(vraies)
