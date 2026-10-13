# Data provenance

*English version. Version française : `PROVENANCE.fr.md`.*

| File | Contents | Origin |
|---|---|---|
| portes_zeta_1004.npy | the first 1,004 zeros of ζ (14.13 to 1,424.46) | computed with Riemann-Siegel, checked with mpmath (12/10/2026); to be compared with Odlyzko's tables (3-references) |
| vraies_portes_W4/V1/V2/V3/V4/H1/H2.npy | zeros of ζ in the test windows (≈ 10⁴ to 2·10⁶) | Riemann-Siegel (C0, C1), step 0.001, mpmath checks to 10⁻⁶; V1 = subset of portes_zeta_1004 |
| portes_L_chi3/chi4/chi5_T1000.npy | zeros of L(s, χ) up to 1,000 | vectorised Euler-Maclaurin (portes/dirichlet.py), checked against mpmath to 10⁻⁸; counts 823 / 868 / 904 consistent with Riemann-von Mangoldt |

Licence: CC BY 4.0.
