"""La valse de π : mesures de 3 ou 4 temps, part des 4 = π − 3, niveaux 7 / 15 / 292."""
import numpy as np

def test_valse():
    n = np.arange(1, 10**6 + 1); s = np.sign(np.sin(n))
    ch = np.nonzero(s[1:] != s[:-1])[0]; L = np.diff(ch)[1:-1]
    assert set(np.unique(L)) == {3, 4}
    assert abs(np.mean(L == 4) - (np.pi - 3)) < 1e-3
    i4 = np.nonzero(L == 4)[0]; entre = np.diff(i4) - 1
    assert set(np.unique(entre[1:-1])) == {6, 7}   # périodes de 7 ou 8 mesures
