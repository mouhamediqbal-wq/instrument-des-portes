# L'horloger : le ressort et l'engrenage — prédiction préenregistrée (13/10/2026, 14h08, Paris) — écrite AVANT calcul
Pièce 1 (le ressort θ) : écart |θ_développement(t) − θ_exact(t)| (θ_exact = mpmath.siegeltheta) en t = 14, 100, 10³, 10⁵, 10⁶.
  P1 : écart < 10⁻⁹ en t = 14 et < 10⁻¹² au-delà de 10³ (le ressort n'a pas de jeu).
Pièce 2 (l'engrenage : quartz → horloge atomique) : pour chaque fenêtre, plus petit X (parmi 100, 200, 500, 10³, 2·10³, 5·10³, 10⁴, 2·10⁴, 5·10⁴, 10⁵, 2·10⁵) donnant ≥ 99 % de vrais zéros appariés (< 0,1 écart local) ; κ = ln X / ln(t/2π) au centre de la fenêtre.
  Fenêtres : W3 = [1 000 ; 1 424,5] (zéros connus) ; W4 = [10 000 ; 10 200] ; W5 = [10⁵ ; 10⁵ + 200] ; W6 = [10⁶ ; 10⁶ + 100] (vrais zéros par Riemann-Siegel, déjà calculés pour W5 et W6).
  K1 : κ constant à ± 20 % près sur les quatre fenêtres.
  K2 : 0,7 ≤ κ ≤ 1,3 dans chaque fenêtre.
(Étape 3, écrite après ce résultat : règle figée X = (t/2π)^κ, puis nouvelle épreuve à l'aveugle.)
