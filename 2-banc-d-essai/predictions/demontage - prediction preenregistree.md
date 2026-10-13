# Démontage de l'instrument fondamental — prédiction préenregistrée (13/10/2026, 13h55, Paris) — écrite AVANT tout calcul
Instrument de référence : Riemann-Siegel, Z(t) = 2 Σ_{n ≤ N(t)} n^{−1/2} cos(θ(t) − t ln n) + correction (C0, C1), N(t) = ⌊√(t/2π)⌋, θ(t) = (t/2)ln(t/2π) − t/2 − π/8 + 1/(48t) + 7/(5760t³).
Données : les 1 004 premiers zéros (14,13 à 1 424,46). Fenêtre 10 ≤ t ≤ 1 430.
Mesure commune (T0, T1, T3) : notes de l'instrument = changements de signe ; pour chaque vrai zéro γ, distance au plus proche changement de signe, divisée par l'écart moyen local 2π/ln(γ/2π) ; « appariés » = zéros à moins de 0,1 écart ; + nombre total de notes.
T0 (rien retiré) : 1 004 notes exactement ; 100 % appariés ; erreur moyenne < 10⁻⁴, maximale < 10⁻².
T1 (courbure retirée : θ remplacé par sa tangente en t = 720, axe droit) : |nombre de notes − 1 004| > 50 ET appariés < 30 %.
T2 (fentes inégales : formule fonctionnelle approchée Σ n^{−s} + χ(s) Σ n^{s−1} pour σ = 0,40 / 0,45 / 0,50 / 0,55 / 0,60) : profondeur du noir = min |f| sur ± ½ écart autour de chaque vrai zéro, divisée par la médiane de |f| sur la fenêtre. Prédiction : médiane des profondeurs < 0,01 en σ = 0,50 ; > 0,1 en σ = 0,40 et 0,60 ; profondeur(0,45) ≈ ½ profondeur(0,40) à 30 % près (zéros simples : |f| croît linéairement avec |σ − ½|).
T3 (cordes composées retirées) : T3a premiers seuls (sans n = 1) ; T3b n = 1 + premiers. Prédiction : appariés T3a < 30 % ; T3b entre 30 % et 70 % ; T3b > T3a.
T4 (témoin Davenport-Heilbronn : même symétrie, pas de produit d'Euler ; caractère mod 5, χ(2) = i, κ = (√(10 − 2√5) − 2)/(√5 − 1)) : en partant de la valeur publiée 0,808517 + 85,699348 i, la recherche de racine converge vers un zéro avec |f| < 10⁻¹⁰ et Re(s) ≠ ½ (≈ 0,8085) ; son reflet 1 − s̄ (Re ≈ 0,1915) est aussi un zéro.
Règle : on consigne tel quel ; rien n'est ajusté sur les zéros.
