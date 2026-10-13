"""§ 2 L'instrument : démontage (T0, T1, T3), cavités, fenêtres à l'aveugle."""
import numpy as np
from _commun import charger, lent
from portes import theta, Z, apparier, portes_instrument
from portes.premiers import crible
from portes.riemann_siegel import changements_de_signe

G = charger('portes_zeta_1004.npy')
t = np.arange(10, 1430, 0.002)

def _part(notes): return np.mean(apparier(notes, G) < 0.1)

def test_T0_riemann_siegel_complet():
    notes = changements_de_signe(t, Z(t))
    assert (notes <= 1424.6).sum() == 1004 and _part(notes) == 1.0

def test_T1_sans_courbure():
    from portes.courbure import theta as th
    t0 = 720.0; d = 0.5*np.log(t0/(2*np.pi)); lin = th(t0) + d*(t - t0)
    N = np.floor(np.sqrt(t/(2*np.pi))).astype(int); s = np.zeros_like(t)
    for n in range(1, N.max()+1): s += np.where(n <= N, 2/np.sqrt(n)*np.cos(lin - t*np.log(n)), 0)
    assert _part(changements_de_signe(t, s)) < 0.30

def test_cavites_168_premiers():
    phi = np.zeros_like(t)
    for p in crible(1000): phi += np.angle(1/(1 - p**-0.5*np.exp(-1j*t*np.log(p))))
    d = apparier(changements_de_signe(t, np.cos(theta(t) + phi)), G)
    assert np.mean(d < 0.1) == 1.0 and d.mean() < 0.02

def _fenetre(nom, a, b, attendu):
    v = charger(f'vraies_portes_{nom}.npy'); notes = portes_instrument(a, b, bord='arrondi')
    assert len(notes) == len(v)
    assert np.mean(apparier(notes, v) < 0.1) >= attendu

def test_fenetre_V1(): _fenetre('V1', 200, 1000, 1.0)
def test_fenetre_V2(): _fenetre('V2', 30000, 30300, 1.0)
@lent
def test_fenetre_V3(): _fenetre('V3', 300000, 300150, 1.0)
@lent
def test_fenetre_V4(): _fenetre('V4', 2000000, 2000080, 0.985)
