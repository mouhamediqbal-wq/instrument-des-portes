# Le loup à trois pas — prédiction préenregistrée (13/10/2026, 12h56, Paris) — écrite AVANT calcul
Constat (exploratoire, résultats « forme de l'erreur ») : le reste r = d(graphe) − d(idéal) est commun aux trois graphes (corrélations 0,74-0,86).
Hypothèse : il vient des chemins à TROIS pas du graphe, non contraints par l'optimisation (cubes p³ et composés à trois facteurs).
Méthode (sans regarder les zéros pour construire la prédiction) : pour chaque graphe (6, 10, 15 premiers), à partir de son seul carrefour S et de ses flux φ :
- coefficients g(n) de ln det(I − U) pour les chemins de 1, 2 et 3 pas, regroupés par longueur ln n ; coefficients idéaux t(n) = 1/(m·p^{m/2}) si n = p^m, 0 sinon ;
- fluctuation prédite du défaut : ΔS₃(E) = −(1/π) Im Σ_{n à 3 pas} (g(n) − t(n)) e^{iE ln n} ; idem ΔS₁₂ pour les écarts résiduels des chemins à 1 et 2 pas ;
- reste prédit = notes(enveloppe + lissage[S_idéal + ΔS]) − notes(enveloppe + lissage[S_idéal]), même lissage qu'A1-bis.
Prédictions de Claude :
L1 : corrélation (reste prédit par ΔS₃, reste mesuré r) > 0,6 pour chacun des trois graphes.
L2 : ΔS₃ explique plus que ΔS₁₂ (corrélation plus forte) pour chacun des trois graphes.
L3 : l'écart moyen du reste prédit par ΔS₃ croît de 6 à 10 à 15 premiers, comme le reste mesuré (0,049 → 0,074 → 0,093).
Si L1 échoue : le loup vient d'ailleurs (chemins plus longs, ou finesse du graphe), et la ré-optimisation à trois pas n'est pas lancée sur cette base.
