# Born 2 : le bord linéaire et la conservation du défaut dans l'instrument — prédiction préenregistrée (13/10/2026, 21h29, Paris) — écrite AVANT calcul

Demande d’ABL_M81 : tester (A) la surprise « l'arrondi n'est pas le meilleur pour l'écart maximal » et (B) la conservation du défaut dans l'instrument.

## A. Le classement de Born se transpose-t-il à l'instrument ?
Montage : instrument fondamental (paquet `portes`), règle d'horloger X = t/2π au centre, bord en octaves (d = distance au bord en octaves au-delà de X). Bords comparés : ARRONDI (demi-cosinus de X à 2X, recommandé) et LINÉAIRE (W = 1 − d de X à 2X, même portée). Fenêtres : V1 (200–1 000, 570 portes), V2 (30 000–30 300, 404), V3 (300 000–300 150, 257). Mesures : part de portes justes (< 0,1 écart), erreur moyenne et erreur maximale (en écarts locaux).
A1 : les deux bords donnent le bon nombre de portes dans les trois fenêtres.
A2 : le classement de Born NE se transpose PAS : dans au moins 2 des 3 fenêtres, l'ARRONDI a une erreur maximale ≤ celle du LINÉAIRE, et une erreur moyenne ≤ celle du LINÉAIRE. Raison attendue : dans l'instrument, l'erreur vient du bruit de troncature d'une somme oscillante, que la douceur du bord (dérivée continue) réduit ; chez Born, elle vient d'une contrainte de somme (trace), qui ne récompense pas la douceur.

## B. L'instrument conserve-t-il un « défaut total » ?
Défaut d'une porte : S_n = (n − ½) − N_lisse(γ_n), N_lisse(t) = θ(t)/π + 1 (la danse de la porte n autour de sa case de Planck).
Analogue de la trace : Σ S_n reste borné (théorème de Littlewood : ∫ S(t) dt = O(log T)), au lieu de croître comme une marche au hasard (≈ 0,26 √N).
B1 (vraies portes, les 1 004 premières) : max sur N ≤ 1 004 de |Σ_{n≤N} S_n| < 3 ; témoins (mêmes S_n mélangés au hasard, 2 000 tirages) : médiane de ce maximum > 6 ; la vraie valeur sous le 1er centile des témoins.
B2 (portes de l'instrument, fenêtre V1, numérotées comme les vraies) : même propriété : max |Σ S_n^inst| < 3, sous le 1er centile des témoins mélangés.
B3 (erreurs de l'instrument) : e_n = (γ_n^inst − γ_n^vraie) / écart local, signées, fenêtre V1 : max |Σ_{n≤N} e_n| < 0,3 ; témoins à signes tirés au hasard (2 000) : la vraie valeur sous le 5e centile.
Si B1-B3 réussissent : l'instrument obéit à une loi de conservation du même type que celle de Born (le défaut total reste borné : il ne peut que se déplacer). Si B3 échoue : l'instrument suit la danse globalement mais ses propres erreurs s'accumulent comme du bruit.
