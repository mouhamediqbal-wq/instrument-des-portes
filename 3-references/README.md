# Comparison with public tables

*English version. Version française : `README.fr.md`.*

The instrument has been verified on zeros computed within this project (Riemann-Siegel, checked with mpmath). A reference model must also be verified on independent tables.

## Odlyzko's tables (zeros of ζ)
Site: https://www-users.cse.umn.edu/~odlyzko/zeta_tables/
Suggested file to start with: the first 100,000 zeros (height ≤ ≈ 74,920). The clockmaker's rule there calls for X ≈ 12,000: a computation of a few minutes.

```
python comparer_odlyzko.py zeros1.txt 50000 50300
```

## LMFDB (Dirichlet L-functions)
Site: https://www.lmfdb.org/ (L-functions section, Dirichlet characters). The zeros of χ₃, χ₄, χ₅ are published there: compare them with `2-banc-d-essai/donnees/portes_L_*_T1000.npy`.

## Rule
Every comparison starts with a written, fingerprinted prediction (see `5-communaute/CONTRIBUTING.md`).
