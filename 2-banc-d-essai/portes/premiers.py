"""Nombres premiers et fonction de von Mangoldt."""
import numpy as np

def crible(n):
    """Tableau des nombres premiers ≤ n."""
    s = np.ones(int(n)+1, bool); s[:2] = False
    for i in range(2, int(n**0.5)+1):
        if s[i]:
            s[i*i::i] = False
    return np.nonzero(s)[0]

def puissance_de_premier(n):
    """(p, k) si n = p^k, sinon None."""
    n = int(n)
    for p in range(2, n+1):
        if n % p == 0:
            m, k = n, 0
            while m % p == 0:
                m //= p; k += 1
            return (p, k) if m == 1 else None
    return None

def von_mangoldt(n):
    """Λ(n) = ln p si n = p^k, 0 sinon."""
    pk = puissance_de_premier(n)
    return float(np.log(pk[0])) if pk else 0.0
