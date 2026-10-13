# Provenance des données

*Version française. English version: `PROVENANCE.md`.*

| Fichier | Contenu | Origine |
|---|---|---|
| portes_zeta_1004.npy | les 1 004 premiers zéros de ζ (14,13 à 1 424,46) | calculés par Riemann-Siegel, contrôlés par mpmath (12/10/2026) ; à confronter aux tables d'Odlyzko (3-references) |
| vraies_portes_W4/V1/V2/V3/V4/H1/H2.npy | zéros de ζ dans les fenêtres de test (≈ 10⁴ à 2·10⁶) | Riemann-Siegel (C0, C1), pas 0,001, contrôles mpmath à 10⁻⁶ ; V1 = sous-ensemble de portes_zeta_1004 |
| portes_L_chi3/chi4/chi5_T1000.npy | zéros de L(s, χ) jusqu'à 1 000 | Euler-Maclaurin vectorisé (portes/dirichlet.py), contrôlé contre mpmath à 10⁻⁸ ; comptes 823 / 868 / 904 conformes à Riemann-von Mangoldt |

Licence : CC BY 4.0.
