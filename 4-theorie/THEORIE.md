# Théorie : ce qui est connu, ce qui est neuf, ce qui reste ouvert

*Version française. English version: `THEORY.md`.*

## 1. Les sources classiques sur lesquelles repose l'instrument

| Pièce de l'instrument | Résultat connu |
|---|---|
| portes ↔ premiers | formule explicite (Riemann 1859, von Mangoldt 1895) |
| plaque percée aux zéros → puissances de premiers | formule de Landau (1911) : Σ_{0<γ≤T} x^{iγ} ≈ −(T/2π) Λ(x)/√x |
| courbure θ(t), deux fentes égales | formule de Riemann-Siegel ; formule fonctionnelle s ↔ 1 − s, |χ(½ + it)| = 1 |
| cavités jusqu'à X | approximation de S(t) par le produit d'Euler tronqué (Selberg) ; formule hybride de Gonek, Hughes et Keating (2007) |
| une porte par case de Planck | formule de Riemann-von Mangoldt ; modèle H = xp de Berry et Keating (1999) |
| répulsion des portes | corrélation de paires (Montgomery 1973), GUE (Dyson, Odlyzko) |
| symétrie seule insuffisante | fonction de Davenport-Heilbronn (1936) ; conjecture de Selberg pour sa classe |
| filtres de couleur | formule explicite pour les fonctions L de Dirichlet |
| biais de Tchebychev | Rubinstein et Sarnak (1994) |

## 2. Ce que le projet ajoute

1. **L'architecture en trois fondements** (courbure, fentes égales, cavités) et sa vérification par démontage : sans courbure 26 % des portes, premiers seuls 17 %, 1 + premiers 43 %, cavités 77 % puis 100 % avec assez de cavités ; sans produit d'Euler, une porte quitte la droite (0,8085 + 85,6993 i).
2. **La règle d'horloger mesurée** : X = t/2π (κ = 1,007 / 1,030 / 0,952 / 0,961), qui rend la précision constante de 200 à 2·10⁶ ; le bord arrondi au-delà de X.
3. **La loi des cubes** pour les graphes quantiques à deux passages par corde (rapport −2 sur p³ ; −k sur p^(k+1) avec k canaux) : un défaut de structure prévisible sans connaître les zéros.
4. **La même constante 2π par trois routes** : aller, retour, géométrie.
5. **Le spectromètre réglable** (diaphragme, accord, filtres) et la lecture visuelle du biais de Tchebychev (les carrés passent tous dans 4k + 1).
6. **La méthode** : 28 prédictions scellées par empreinte avant calcul, échecs compris.

## 3. Questions ouvertes (bonnes premières contributions)

1. **Déduire κ = 1 de la théorie.** La variance de S(t) − S_X(t) selon Selberg dit-elle que X = t/2π est le seuil des 99 % ? Pourquoi la même constante que dans N(T) ?
2. **Les deux portes récalcitrantes à 2·10⁶** (0,12 écart) : portes étroites de type Lehmer ? effet du pas de grille ? bord à affiner ?
3. **Le paradoxe de Berry-Keating** : un système physique dont les orbites de période ln p ont toutes la même instabilité (λ = 1) donne, par Gutzwiller, des amplitudes p^(−m/2)/(1 − p^(−m)) et non p^(−m/2), et des phases quelconques et non toutes égales à π. Quel objet réel produirait exactement les échos de l'instrument ?
4. **La boucle fermée** : l'instrument pose ses portes à partir des premiers ; passer la lumière par SES portes redonne-t-il les mêmes premiers, sans référence aux vrais zéros ?
5. **Les quatre plaques** (Poisson, cristal, GUE, Riemann) : vérifier que seule la plaque de Riemann laisse passer les premiers, et que les premiers vivent dans les corrélations à longue portée (Bogomolny-Keating), pas dans la répulsion locale.
6. **Caractères complexes** : étendre les filtres de couleur aux classes mod 5, 7, 8… complètes (caractères non réels).
7. **Hauteurs extrêmes** : la règle X = t/2π devient impraticable vers 10¹² ; quelle version tronquée garde 99 % ?

## 4. Références

- B. Riemann, *Über die Anzahl der Primzahlen unter einer gegebenen Grösse* (1859).
- E. Landau, *Über die Nullstellen der Zetafunktion*, Math. Ann. 71 (1911).
- H. Montgomery, *The pair correlation of zeros of the zeta function* (1973).
- M. V. Berry, J. P. Keating, *The Riemann zeros and eigenvalue asymptotics*, SIAM Review 41 (1999).
- S. M. Gonek, C. P. Hughes, J. P. Keating, *A hybrid Euler-Hadamard product for the Riemann zeta function*, Duke Math. J. 136 (2007).
- M. Rubinstein, P. Sarnak, *Chebyshev's bias*, Experimental Math. 3 (1994).
- H. Davenport, H. Heilbronn, *On the zeros of certain Dirichlet series* (1936).
- H. M. Bui, J. B. Conrey, M. P. Young, *More than 41% of the zeros of the zeta function are on the critical line*, arXiv:1002.4127.
- B. Rodgers, T. Tao, *The de Bruijn-Newman constant is non-negative*, Forum Math. Pi (2020).
- O. Hul et coll., *Experimental simulation of quantum graphs by microwave networks*, arXiv:nlin/0404006.
- M. D. Johnson et coll., *Universal interferometric signatures of a black hole's photon ring*, arXiv:1907.04329.
