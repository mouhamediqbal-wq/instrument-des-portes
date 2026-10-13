# Épreuve en hauteur, à l'aveugle — prédiction préenregistrée (13/10/2026, 14h03, Paris) — écrite AVANT tout calcul
Instrument (règle figée) : note = changement de signe de cos(θ(t) + Σ_{p ≤ X} arg (1 − p^{−1/2 − it})^{−1}), θ(t) = (t/2)ln(t/2π) − t/2 − π/8 + 1/(48t) + 7/(5760t³). Entrées : premiers et θ seulement.
Fenêtres : H1 = [100 000 ; 100 200] ; H2 = [1 000 000 ; 1 000 100]. Pas de grille 0,001.
Ordre : 1) l'instrument joue ses notes (X = 1 000 et X = 10 000) ; elles sont enregistrées et empreintées AVANT 2) le calcul des vrais zéros par Riemann-Siegel (Z avec corrections C0, C1 ; N = √(t/2π) termes), contrôlé par mpmath sur quelques zéros et par le compte de Riemann-von Mangoldt.
Mesure : appariés = vrais zéros à moins de 0,1 écart local d'une note ; écart moyen en écarts locaux ; nombre de notes contre nombre de zéros.
Prédictions de Claude :
H-a : X = 1 000 : appariés ≥ 95 % en H1 et ≥ 90 % en H2.
H-b : X = 10 000 fait mieux que X = 1 000 dans les deux fenêtres (écart moyen plus petit).
H-c : écart moyen (X = 10 000) < 0,03 en H1 et < 0,04 en H2.
H-d : nombre de notes = nombre de zéros à ±2 près dans chaque fenêtre.
