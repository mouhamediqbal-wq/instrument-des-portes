# Le suppresseur de loup (composés à trois facteurs) — prédiction préenregistrée (13/10/2026, 13h12, Paris) — écrite AVANT calcul
Méthode : on reprend les carrefours optimisés (6, 10, 15 premiers) comme point de départ et on ré-optimise avec une contrainte de plus : tous les chemins à TROIS pas dont la longueur est celle d'un composé (ln(pqr), ln(p²q)) sont éteints (même poids w = 10 que les paires pq). Les cubes p³ ne sont pas contraints (loi : rapport −2 imposé par l'algèbre) ; on les corrige comme dans « correction des cubes » (empreinte 492023df…). Gradient calculé à la main (dérivée de Fréchet de l'exponentielle), vérifié par différences finies avant usage. Ensuite : nouveau spectre du graphe (même balayage du déterminant), même assemblage, même lissage, même correction des cubes.
Remarque écrite avant : la recette idéale (formule exacte, mêmes premiers, même lissage) n'est elle-même PAS ordonnée (0,0235 / 0,0316 / 0,0254) ; le critère d'ordre 6 > 10 > 15 ne peut donc pas être atteint avec ce lissage, même par un graphe parfait.
Prédictions de Claude :
S1 (optimisation) : poids premiers à 5 % près, paires pq < 2 % des premiers, et composés à trois pas réduits à moins de 20 % de leur niveau actuel, pour 6, 10 et 15 premiers.
S2 (justesse) : écart corrigé ≤ 1,2 × écart idéal pour chacun des trois jeux (soit ≤ 0,028 / 0,038 / 0,030).
S3 : l'amélioration la plus forte est à 15 premiers (de 0,055 vers ≈ 0,03).
S4 : le critère d'ordre échoue entre 6 et 10 (comme la recette idéale).
