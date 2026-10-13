"""§ 2.1 courbure, § 5 loi des cubes, § 4 constante 2π."""
import numpy as np
from _commun import charger
from portes import theta, cases_de_planck, ajuster_h
from portes.graphe import rapport_premier_ecart

def test_courbure_contre_forme_exacte():
    try:
        import mpmath as mp
    except ImportError:
        print('    (mpmath absent : contrôle de la courbure sauté)'); return
    mp.mp.dps = 30
    for t, tol in ((14.0, 1e-9), (1000.0, 1e-12)):
        assert abs(float(mp.siegeltheta(t)) - float(theta(t))) < tol

def test_loi_des_cubes():
    assert abs(rapport_premier_ecart(2) - (-2)) < 1e-12
    for k in range(1, 7):
        assert abs(rapport_premier_ecart(k) - (-k)) < 1e-9

def test_une_porte_par_case_de_planck():
    g = charger('portes_zeta_1004.npy'); n = np.arange(1, len(g)+1)
    S = (n - 0.5) - cases_de_planck(g)
    assert abs(S.mean()) < 0.05 and 0.15 < S.std() < 0.45 and abs(S).max() < 1.5
    assert abs(ajuster_h(g)/(2*np.pi) - 1) < 1e-4
