# L'instrument des portes

*Un instrument qui joue les zéros de Riemann à partir des seuls nombres premiers, et un spectromètre qui retrouve les nombres premiers à partir des seuls zéros.*

Projet ouvert, né du projet π d'ABL_M81, mené avec Claude (assistant IA d'Anthropic), octobre 2026.
Version originale française. English version: README.md. Chaque document existe en français et en anglais ; seules les prédictions scellées (leurs empreintes interdisent toute retouche) et les commentaires du code restent en français.

---

## En une phrase

Les zéros de la fonction ζ de Riemann ne sont pas traités ici comme des nombres à calculer, mais comme des **portes** : une plaque percée à ces portes ne laisse passer que les nombres premiers, et des cavités accordées aux nombres premiers posent ces portes. Le dépôt fournit l'instrument, le spectromètre, et un banc d'essai qui rejoue chaque résultat.

## Ce que fait l'instrument

À partir des **nombres premiers seuls**, il place les portes (les zéros de ζ sur la droite critique) en assemblant trois fondements :

1. **la courbure** : l'axe de mesure s'enroule selon l'angle de Riemann-Siegel θ(t) ;
2. **deux fentes égales** : l'onde et son reflet (s et 1 − s), réunis dans un cosinus ;
3. **des cavités** : chaque premier p est une cavité à écho infini, de facteur (1 − p^(−1/2 − it))^(−1).

Une porte est un changement de signe de cos(θ(t) + Σ_p arg (1 − p^(−1/2 − it))^(−1)), la somme portant sur les premiers p ≤ t/2π (règle d'horloger), avec un bord adouci.

Résultats vérifiés (prédictions écrites et scellées avant chaque calcul) :

| Mesure | Résultat |
|---|---|
| portes jouées de t = 14 à t = 2 000 000 | aucune manquée, aucune en trop |
| portes à moins de 0,1 écart de la vraie position | 1 389 / 1 391 = 99,86 % (quatre fenêtres à l'aveugle) |
| erreur moyenne | 0,020 à 0,033 écart local, constante sur quatre ordres de grandeur |
| exposant de la règle d'horloger | κ = 1,007 / 1,030 / 0,952 / 0,961 (cavités jusqu'à t/2π) |

## Ce que fait le spectromètre

Une plaque percée aux zéros, éclairée : la réponse R(x) = −(4π/T)·√x·Σ cos²(πγ/2T)·cos(γ ln x) s'allume aux puissances de premiers (hauteur ln p) et reste noire ailleurs (formule de Landau, 1911).

- **Diaphragme** : plus de portes ouvertes, plus de premiers lisibles (jusqu'à environ T/2π).
- **Accord** : un bouton qui interroge un nombre ; 100 % de bons classements jusqu'à 120.
- **Filtres de couleur** : avec les zéros des fonctions L de Dirichlet (χ₃, χ₄, χ₅), le spectromètre sépare les premiers par classe (3k ± 1, 4k ± 1, résidus mod 5) : 99,3 à 100 % jusqu'à 150.
- **Réciproque** : à partir des 1 004 premiers zéros seuls, les 55 premiers jusqu'à 262 et leurs 54 écarts sont retrouvés sans erreur.

Une version interactive est dans `5-communaute/spectrometre-de-riemann.html`.

## Ce qui est connu, ce qui est neuf

Les ingrédients sont connus : formule explicite (Riemann, von Mangoldt), formule de Landau, approximation de Selberg de S(t), formule de Riemann-Siegel, formule hybride de Gonek-Hughes-Keating, dynamique de Berry-Keating (H = xp), statistique GUE (Montgomery, Dyson, Odlyzko).

Ce que ce projet apporte, sans exagérer :
- une **architecture** en trois fondements, et la preuve par démontage que chacun est porteur (sans courbure 26 %, premiers seuls 17 %, sans produit d'Euler une porte quitte la droite : Davenport-Heilbronn) ;
- la **loi des cubes** : un graphe quantique à deux passages par corde, accordé sur p et p², chante p³ avec un rapport −2 exactement (k canaux : erreur en p^(k+1), rapport −k) ;
- la **règle d'horloger** mesurée (κ = 1) et la même constante 2π retrouvée par trois routes : aller (cavités jusqu'à t/2π), retour (lecture jusqu'à T/2π), géométrie (une porte par case de Planck, h = 2π ; ajustement h′ = 6,28318) ;
- un **spectromètre** réglable avec filtres de couleur, et l'explication visuelle du biais de Tchebychev (les carrés passent tous dans la classe 4k + 1) ;
- une **méthode** : chaque calcul précédé d'une prédiction écrite et empreintée (SHA-256), les échecs consignés tels quels.

Rien ici ne démontre l'hypothèse de Riemann.

## Organisation

| Dossier | Contenu |
|---|---|
| `1-specification/` | la fiche technique de l'instrument et du spectromètre |
| `2-banc-d-essai/` | le paquet Python `portes`, les données, les prédictions scellées, les tests |
| `3-references/` | confrontation aux tables publiques (Odlyzko, LMFDB) |
| `4-theorie/` | liens avec la littérature, questions ouvertes |
| `5-communaute/` | spectromètre interactif, guide pour contribuer, plan de montage en réseau hyperfréquence |

## Lancer le banc d'essai

Python 3.10 ou plus, avec `numpy` et `scipy` ; `mpmath` seulement pour les contrôles.

```
cd 2-banc-d-essai
python lancer_les_tests.py          # 14 tests rapides (environ 15 secondes)
python lancer_les_tests.py --lents  # + 3 tests lents : fenêtres à 3·10⁵ et 2·10⁶, recalcul des portes de Dirichlet (environ 1 minute de plus)
```

Les tests sont aussi lisibles par `pytest`.

## Licences

- Code : licence MIT (`LICENSE`).
- Textes, figures et données : Creative Commons Attribution 4.0 International (`LICENSE-CC-BY-4.0.md`).

Pour citer : voir `CITATION.cff`.

---

## English summary

**The door instrument.** Riemann zeros are treated as *doors*: a plate pierced at the zeros lets only prime powers through (Landau's formula), and prime cavities place the doors. Built on three foundations (Riemann-Siegel curvature θ(t), two equal slits s ↔ 1 − s, one infinite-echo cavity per prime up to t/2π, with a soft edge), the instrument uses primes only and plays every zero from t = 14 to t = 2·10⁶ with none missed or added, 99.86 % within 0.1 local spacing (blind, pre-registered tests). The spectrometer reads primes back from zeros, with an aperture, a tuning knob and Dirichlet colour filters (mod 3, 4, 5). The constant 2π governs both directions and the phase-space count (one zero per Planck cell of area 2π). Ingredients are classical; the architecture, the cube law of two-channel quantum graphs, the measured clock rule and the pre-registered test bench are this project's contribution. Nothing here proves the Riemann Hypothesis.
