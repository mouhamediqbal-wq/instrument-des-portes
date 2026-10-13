# Born 4 : la trigonométrie remet de l'ordre dans le peigne — prédiction préenregistrée (13/10/2026, 21h46, Paris) — écrite AVANT calcul

Question d’ABL_M81 : « la trigonométrie peut-elle remettre de l'ordre ? »
Théorie (Jacobi-Anger, calculée sans données) : la danse S des portes est une somme de sinus, un par premier et par écho ; e^(−2πiS) = Π_p e^(2i·arg(1 − p^(−1/2−it))^(−1)) = Π_p (1 − x̄_p)/(1 − x_p), x_p = p^(−1/2) e^(−it ln p). Ses coefficients de Fourier sont exacts, premier par premier : c₀ = 1 − 1/p ; c_j = p^(−j/2)(1 − 1/p) (j ≥ 1) ; c₋₁ = −1/√p ; c₋ⱼ = 0 (j ≥ 2).
Conséquence : la résonance des portes en q = r·X (X = t/2π) vaut, rapportée à celle en X,
  R(r) = Π_{p | a} (−√p/(p − 1)) × b^(−1/2)   pour r = a/b, a sans facteur carré, premier avec b ; R = 0 si a a un facteur carré.
Les dents du peigne sont donc en X × (entier sans carré) / (entier quelconque), avec des hauteurs et des signes fixés.

Mesure : A(r) = (1/N) Σ_n e^(2iθ(γ_n)) r^(iγ_n) sur les 7 fenêtres de vraies portes réunies (W4, V1, V2, H1, V3, H2, V4 : 2 125 portes, de 200 à 2·10⁶) ; rapport mesuré ρ(r) = Re[A(r)/A(1)].

Valeurs prédites de R(r) :
| r | R prédit |
|---|---|
| 1/1 | +1.000 |
| 2/1 | -1.413 |
| 1/2 | +0.707 |
| 3/1 | -0.866 |
| 1/3 | +0.577 |
| 2/3 | -0.816 |
| 3/2 | -0.612 |
| 5/1 | -0.559 |
| 1/5 | +0.447 |
| 6/1 | +1.224 |
| 1/6 | +0.408 |
| 7/1 | -0.441 |
| 10/1 | +0.790 |
| 14/1 | +0.623 |
| 15/1 | +0.484 |
| 1/4 | +0.500 |
| 4/1 | +0.001 |
| 8/1 | +0.001 |
| 9/1 | +0.000 |
| 12/1 | -0.001 |
| 18/1 | -0.000 |
Contrôles (R = 0, valeurs de r non rationnelles simples) : 1,37 ; 2,71 ; 4,4.

P1 (positions et signes) : pour les 15 rapports prédits non nuls, le signe de ρ(r) est celui de R(r) dans au moins 13 cas sur 15.
P2 (hauteurs) : écart quadratique moyen entre ρ(r) et R(r) sur ces 15 rapports < 0,35.
P3 (dents interdites) : pour 4, 8, 9, 12, 18 et les 3 contrôles, |A(r)/A(1)| < 0,45 (bruit attendu ≈ 0,022/|A(1)|).
P4 (ordre) : la plus haute dent est 2X (|ρ| maximal parmi les 21 rapports testés autres que 1), la deuxième 6X ou X.
