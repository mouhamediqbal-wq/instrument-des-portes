# 6 · Born, le bord et le peigne

*Version française. English version: `README.md`.*

Une partie supplémentaire, distincte de l'instrument lui-même (dossiers 1 à 5). Elle part de la relation de commutation canonique de Born et cherche ce qu'elle dit des portes. Même méthode que le reste du dépôt : chaque prédiction a été écrite et scellée par une empreinte SHA-256 **avant** le calcul (`predictions/`), et les échecs sont consignés tels quels (`resultats/`).

## 1. La relation de Born et le bord (prédiction `born`, 5/5 réussies)
Born et Jordan (1925) : qp − pq = iħ·1, avec ħ = h/2π. Impossible avec des matrices finies : la trace d'un commutateur est nulle, celle de iħ·1 vaut iħ·n. En coupant les matrices de l'oscillateur à la taille n, on obtient qp − pq = i·diag(1, …, 1, −(n − 1)) : exact partout sauf la dernière case, qui porte tout le défaut.
Avec un bord progressif, le défaut s'étale et reste **borné, quelle que soit la taille** : bord linéaire 3,00, arrondi 3,05, ébrasé 2,11, optimal 1 + K/w pour un bord de largeur w. Le défaut total vaut toujours exactement −n (théorème de la trace) : on le déplace, on ne l'efface jamais.

## 2. Conservation du défaut dans les portes (prédiction `born 2` : B1-B3 réussies, A2 échouée)
Défaut de la porte n : S_n = (n − ½) − (θ(γ_n)/π + 1), son écart à sa case de Planck. La somme cumulée Σ S_n sur les 1 004 premiers zéros ne dépasse jamais **0,58** (témoins mélangés : 6,6). Les portes de l'instrument, construites avec les seuls premiers, ont la même propriété (0,78 contre 5,1), et les erreurs propres de l'instrument se compensent (0,18 contre 0,86 pour des signes au hasard). C'est l'analogue de la trace de Born ; pour les vrais zéros, c'est le théorème de Littlewood (∫ S = O(log T)).
Échec consigné (A2) : nous avions prédit que le bord arrondi battrait un bord linéaire dans l'instrument ; le linéaire est en fait très légèrement meilleur (1 à 3 %), comme chez Born.

## 3. La trace danse en cosinus (prédiction `born 3` : P0, P2, P5 réussies ; P1 en partie, P3 échouée)
Le défaut d'une porte de l'instrument est exactement la phase des cavités lue sur la porte : S_n = Φ(γ_n)/π (à 2·10⁻⁶). Sa somme cumulée suit une danse en cosinus prédite par les seuls premiers (corrélation 0,982 ; amplitude pas encore à 10 % près) ; p = 2 explique seul 44 % de la variance.
En sondant les portes avec q^{iγ}, des résonances apparaissent autour de X = t/2π. La prédiction P3 (la plus forte en X) a échoué : la plus forte est en 2X, et les résonances forment un **peigne**.

## 4. Le peigne de Möbius (prédiction `born 4`, 4/4 réussies)
En développant la danse des portes premier par premier (développement de Jacobi-Anger, fonctions de Bessel), on prédit tout le peigne : rapportée à la dent en X, la dent en q = (a/b)·X a pour hauteur

  R(a/b) = μ(a) · Π_{p|a} √p/(p − 1) · b^(−1/2)

(μ = fonction de Möbius ; pas de dent si a contient un carré). Sur 2 125 vrais zéros (7 fenêtres de 200 à 2·10⁶) : **15 signes sur 15**, écart moyen **0,07**, aucune dent en 4X, 8X, 9X, 12X, 18X, les plus hautes en 2X puis 6X.

## État de la littérature (vérifié le 13 octobre 2026)
- Connu : la somme mesurée est Σ χ(ρ)⁻¹ r^{iγ} ; Σ χ(ρ) = −T/2π (hauteur en X ≈ −1/log(t/2π)) ; les dents X/b de hauteur b^(−1/2) ; le changement de régime exactement en X = T/2π et X = T/π = 2X (Gonek, Fujii ; arXiv 2601.18025).
- **Non trouvé** : les dents a·X avec le signe de Möbius μ(a) et la hauteur Π √p/(p − 1). Non trouvé ne veut pas dire inédit : les textes complets de Gonek (1993) et Fujii (2012) n'ont pas été consultés. Notre dérivation est heuristique (le produit d'Euler ne converge pas sur la droite critique) ; seule la mesure l'appuie. Corrections et références bienvenues (ouvrir une Issue).

## Note sur les prédictions scellées
Dans les quatre textes de prédiction, le prénom de la personne qui posait la question a été remplacé par le pseudonyme ABL_M81 **après** scellement ; rien d'autre n'a été modifié. Les empreintes de `predictions/` sont celles des textes publiés ; les empreintes d'origine (calculées avant chaque calcul, et citées dans `resultats/`) étaient :

| Prédiction | Empreinte d'origine (avant calcul) | Texte publié |
|---|---|---|
| born | caf5a41b5358169f3cbd93b6a9ca9e579f38686798ab3a883ae28215716aaab3 | abf6f1d66a8bd829e588a03425a02f068703c089f6ef3ceb810a179624ac6892 |
| born 2 | 481886716cb380ca4bc20d0c8bc1be8381efcdea62bc0dd613ea47f656108f60 | 940340d4304ec87646c7d5f785cd753c8cfd0e2702d99b1e731a7bd63a965e47 |
| born 3 | 7e567aa544b63b69246ef9575e5c5d3585dc1f23e8e8f5b6bd8a4729539b0f21 | c744f5fb97c12ab5f9ff5a81629598881ebb0c05c25b754efa5080c8f06c2936 |
| born 4 | 1d7a2af6ee21c55fb4458ea71fc159c0684459cd78b6cac8a94e580c46f4da5f | a0ad231e9462f834e59f2e94a60136dc344320fe40a741291e84bfcc9c728770 |

## Reproduire
```
cd 6-born/scripts
python born.py   # 1. Born et le bord (quelques secondes)
python born2.py  # 2. bords dans l'instrument, conservation (environ 1 minute)
python born3.py  # 3. danse en cosinus et balayage des résonances (environ 1 minute)
python born4.py  # 4. peigne de Möbius (quelques secondes)
python figure.py; python figure2.py; python figure3.py; python figure4.py   # figures/
```
Les vérifications rapides font partie du banc d'essai : `2-banc-d-essai/tests/test_born.py`.

## Questions ouvertes
- Pourquoi l'instrument conserve-t-il son défaut ? Écrire l'analogue exact de la trace de Born pour l'instrument.
- Démontrer (ou trouver dans la littérature) la loi des dents a·X au signe de Möbius.
