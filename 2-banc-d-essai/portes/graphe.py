"""§ 5 La loi des cubes : une corde à k canaux ne peut être juste au-delà de p^k."""
import numpy as np

def coefficients_log(poly, n):
    """Coefficients c_1..c_n de ln(poly(y)) en série, poly = [1, a1, a2, …]."""
    a = np.zeros(n+1); a[:len(poly)] = poly[:n+1]
    c = np.zeros(n+1)   # récurrence : m c_m = m a_m − Σ_{j<m} j c_j a_{m−j}
    for m in range(1, n+1):
        c[m] = a[m] - sum(j*c[j]*a[m-j] for j in range(1, m))/m
    return c[1:]

def rapport_premier_ecart(k):
    """Corde à k canaux accordée sur les k premiers échos : polynôme 1 + y + … + y^k.
    Renvoie (coefficient obtenu en y^(k+1)) / (coefficient juste 1/(k+1))."""
    c = coefficients_log([1.0]*(k+1), k+1)
    return c[k]*(k+1)
