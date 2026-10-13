"""6-born : la trace de Born, la conservation du défaut des portes, le peigne de Möbius (voir 6-born/README.md)."""
import glob, hashlib, os
import numpy as np
from _commun import charger, RACINE
from portes import theta

BORN = os.path.join(RACINE, '..', '6-born', 'predictions')

def test_empreintes_born():
    fichiers = glob.glob(os.path.join(BORN, 'empreinte*.txt'))
    assert len(fichiers) == 4
    for e in fichiers:
        h, nom = open(e, encoding='utf-8').read().strip().split('  ', 1)
        assert hashlib.sha256(open(os.path.join(BORN, nom), 'rb').read()).hexdigest() == h, nom

def test_trace_de_born_et_bord():
    # oscillateur coupé à n = 2K avec le bord arrondi : qp − pq exact au cœur, défaut total −n, défaut max ≈ 3,05
    K = 200; n = 2*K; k = np.arange(n+1, dtype=float); f2 = np.ones(n+1)
    b = k > K; f2[b] = 0.5*(1 + np.cos(np.pi*(k[b] - K)/K)); f2[n] = 0
    a = np.zeros((n, n)); j = np.arange(1, n); a[j-1, j] = np.sqrt(j*f2[j])
    q = (a + a.T)/np.sqrt(2); p = (a - a.T)/(1j*np.sqrt(2))
    e = np.diag(q@p - p@q).imag - 1
    assert abs(e.sum() + n) < 1e-8 and np.abs(e[:K]).max() < 1e-9 and 3.0 < np.abs(e).max() < 3.1

def test_conservation_du_defaut():
    G = charger('portes_zeta_1004.npy'); n = np.arange(1, len(G)+1)
    S = (n - 0.5) - (theta(G)/np.pi + 1)
    rng = np.random.default_rng(1)
    temoins = [np.abs(np.cumsum(rng.permutation(S))).max() for _ in range(200)]
    assert np.abs(np.cumsum(S)).max() < 1 and np.median(temoins) > 4

def _R(a, b):
    r = 1.0
    for p in (2, 3, 5, 7):
        if a % p == 0: r *= -np.sqrt(p)/(p - 1)
    return r/np.sqrt(b)

def test_peigne_de_mobius():
    g = np.concatenate([charger(f'vraies_portes_{w}.npy') for w in ('W4', 'V1', 'V2', 'H1', 'V3', 'H2', 'V4')])
    E = np.exp(2j*theta(g)); A1 = E.mean()
    L = [(2,1),(1,2),(3,1),(1,3),(2,3),(3,2),(5,1),(1,5),(6,1),(1,6),(7,1),(10,1),(14,1),(15,1),(1,4)]
    m = np.array([(np.mean(E*np.exp(1j*g*np.log(a/b)))/A1).real for a, b in L])
    pr = np.array([_R(a, b) for a, b in L])
    assert np.all(np.sign(m) == np.sign(pr)) and np.sqrt(np.mean((m - pr)**2)) < 0.15
    for a in (4, 8, 9, 12): assert abs(np.mean(E*np.exp(1j*g*np.log(a)))/A1) < 0.3
