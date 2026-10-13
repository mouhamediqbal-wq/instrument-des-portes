# Plan de montage : l'instrument en câbles (ébauche à discuter avec un laboratoire)

*Version française. English version: `build-plan.md`.*

Statut : **ébauche de calcul, non construite, non vérifiée en laboratoire.** Elle s'appuie sur les réseaux hyperfréquences qui simulent les graphes quantiques (Hul et coll., arXiv:nlin/0404006).

## Principe
Une « fleur » : un sommet central et une boucle de câble coaxial par premier p, de longueur proportionnelle à ln p. Le spectre des résonances du réseau, mesuré à l'analyseur de réseau vectoriel, joue le rôle des notes du graphe ; les portes s'obtiennent par l'assemblage décrit dans la spécification (enveloppe + fluctuation lissée), ou directement en mesurant la phase de transmission.

## Dimensions (câble à diélectrique PTFE, ε ≈ 2,06, vitesse ≈ 0,70 c ; échelle ℓ₀ = 0,5 m)

| p | longueur de boucle ℓ₀ ln p |
|---|---|
| 2 | 0,347 m |
| 3 | 0,549 m |
| 5 | 0,805 m |
| 7 | 0,973 m |
| 11 | 1,199 m |
| 13 | 1,283 m |
| 17 | 1,417 m |
| 19 | 1,472 m |
| 23 | 1,568 m |
| 29 | 1,684 m |

Longueur totale : 5,16 m (6 premiers), 11,30 m (10 premiers).
Correspondance fréquence ↔ hauteur : f = k·v/(2π ℓ₀) ≈ k × 66,5 MHz ; k = 14,13 → 0,94 GHz ; k = 100 → 6,65 GHz ; k = 160 → 10,6 GHz : dans la gamme d'un analyseur courant.

## Le sommet
- **Version simple** : jonction de Kirchhoff (Neumann), native en câbles. C'est le « carrefour de Kirchhoff » du projet : il fait entendre les composés (échos en ln 6, ln 10…) et a la statistique GOE si on ne brise pas la symétrie du temps.
- **Version fidèle** : la matrice de jonction optimisée du projet (unitaire 2n × 2n, flux sur chaque boucle). Elle n'est pas native en câbles ; elle se réalise par un réseau de coupleurs et de déphaseurs (décomposition de Reck ou de Clements : n(2n − 1) éléments, soit 66 pour 6 premiers), plus naturel en photonique intégrée programmable qu'en hyperfréquence.
- **Briser la symétrie du temps** (statistique GUE des zéros) : un circulateur ou un élément à ferrite sur le sommet.

## Défauts attendus, connus d'avance (spécification § 5)
- **Loi des cubes** : deux passages par boucle → l'écho de p³ sort avec un rapport −2 ; à corriger par calcul (il est connu exactement) ou par une boucle à trois canaux.
- **Composés à trois pas** : à éteindre dans la conception du sommet (suppresseur de loup).
- **Pertes** des câbles : elles atténuent tous les échos ; il faudra les mesurer et les compenser (l'amplitude 1/√p par écho est la cible).

## Ce que la mesure apporterait
Un objet physique dont les résonances suivent les portes de Riemann à la précision de l'assemblage (≈ 0,03 écart pour 10 à 15 premiers en simulation), et un banc pour tester le paradoxe de Berry-Keating (amplitudes p^(−m/2), phases).
