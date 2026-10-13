# Forme de l'erreur d'A1-bis — prédiction préenregistrée (13/10/2026, 12h48, Paris) — écrite AVANT tout calcul
Question (doublet achromatique) : l'erreur dₙ = Eₙ − γₙ des 40 premières notes d'A1-bis (6, 10, 15 premiers) est-elle une « aberration » régulière, corrigeable, ou du bruit ? Et d'où vient-elle : de la recette (troncature aux premiers choisis + lissage, comme un verre dispersif) ou du graphe lui-même (le loup) ?
Mesures (aucun nouveau spectre ; spectres kP6, kP10, kP15 déjà calculés ; règle d'assemblage A1-bis inchangée) :
- dₙ pour chaque jeu ; biais moyen ; autocorrélation de dₙ à un pas ; corrélations entre jeux.
- Référence « idéale » : même règle, mais avec la fluctuation EXACTE de la formule explicite tronquée aux mêmes premiers, S_P(E) = −(1/π) Σ_{p≤P} Σ_{m≤3} sin(m·E·ln p)/(m·p^{m/2}), lissée par la même gaussienne. Donne dₙ(idéal).
Prédictions de Claude :
F1 (aberration, pas bruit) : autocorrélation à un pas de dₙ > 0,3 pour les trois jeux.
F2 (pas de biais dominant) : |moyenne de dₙ| < 0,5 × moyenne de |dₙ| pour les trois jeux.
F3 (recette contre loup) : corrélation entre dₙ(graphe) et dₙ(idéal) > 0,7 pour 6 premiers, et plus faible pour 15 premiers (le graphe à 15 cordes ajoute son propre parasite).
F4 (doublet) : dₙ(6) et dₙ(15) sont positivement corrélés (> 0,3) — même cause commune (premiers manquants au-delà de 47) — donc pas de doublet par simple compensation de signes ; un doublet ne serait possible qu'en combinant des jeux d'erreurs de signes opposés, à chercher ailleurs.
Règle : on consigne tel quel ; aucun poids de combinaison n'est ajusté sur les zéros.
