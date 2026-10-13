"""§ 3 Le spectromètre : diaphragme, accord, lecture des premiers, filtres de couleur."""
import numpy as np
from _commun import charger, lent
from portes import reponse, lire_premiers, von_mangoldt
from portes.premiers import crible, puissance_de_premier
from portes.dirichlet import CH

G = charger('portes_zeta_1004.npy')

def test_diaphragme_1004_portes():
    I = np.arange(2, 56); R = reponse(I, G); L = np.array([von_mangoldt(n) for n in I])
    ok = np.where(L > 0, R >= 0.5*L, abs(R) < 0.25)
    assert ok.all()

def test_accord_jusqu_a_120():
    I = np.arange(2, 121); R = reponse(I, G); L = np.array([von_mangoldt(n) for n in I])
    assert np.all((R > 0.35) == (L > 0))

def test_lecture_des_premiers_jusqu_a_262():
    N, L, trouves = lire_premiers(G, 262)
    assert list(trouves) == list(crible(262))

def test_six_filtres_de_couleur():
    T = 1000.0; gz = G[G <= T]; I = np.arange(2, 151); Rz = reponse(I, gz, T)
    for nom, (chi, q, par) in CH.items():
        Rc = reponse(I, charger(f'portes_L_{nom}_T1000.npy'), T)
        for s in (1, -1):
            F = (Rz + s*Rc)/2; bons = total = 0
            for n, v in zip(I, F):
                pk = puissance_de_premier(n)
                if pk and q % pk[0] == 0: continue
                attendu = pk is not None and chi[pk[0] % q]**pk[1] == s
                bons += ((v > 0.4) == attendu); total += 1
            assert bons/total >= 0.99, (nom, s, bons, total)

@lent
def test_recalcul_des_portes_de_dirichlet():
    from portes.dirichlet import portes_dirichlet
    for nom, attendu in (('chi3', 823), ('chi4', 868), ('chi5', 904)):
        g = portes_dirichlet(nom); assert len(g) == attendu
        assert np.allclose(g, charger(f'portes_L_{nom}_T1000.npy'), atol=1e-6)
