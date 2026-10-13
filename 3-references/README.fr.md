# Confrontation aux tables publiques

*Version française. English version: `README.md`.*

L'instrument a été vérifié sur des zéros calculés dans ce projet (Riemann-Siegel, contrôlés par mpmath). Un modèle de référence doit l'être aussi sur des tables indépendantes.

## Tables d'Odlyzko (zéros de ζ)
Site : https://www-users.cse.umn.edu/~odlyzko/zeta_tables/
Fichier conseillé pour commencer : les 100 000 premiers zéros (hauteur ≤ ≈ 74 920). La règle d'horloger y demande X ≈ 12 000 : calcul de quelques minutes.

```
python comparer_odlyzko.py zeros1.txt 50000 50300
```

## LMFDB (fonctions L de Dirichlet)
Site : https://www.lmfdb.org/ (rubrique L-functions, caractères de Dirichlet). Les zéros de χ₃, χ₄, χ₅ y sont publiés : comparer avec `2-banc-d-essai/donnees/portes_L_*_T1000.npy`.

## Règle
Chaque confrontation commence par une prédiction écrite et empreintée (voir `5-communaute/CONTRIBUER.md`).
