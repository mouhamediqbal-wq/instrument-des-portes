# Born 3 : la trace de l'instrument danse en cosinus, et la résonance de l'horloger — prédiction préenregistrée (13/10/2026, 21h39, Paris) — écrite AVANT calcul

Intuition d’ABL_M81 : « le signe, lui, doit danser en cosinus ».

## T1. La forme exacte du défaut cumulé (fenêtre V1, 200–1 000, X = 95,5, bord arrondi)
Portes de l'instrument γ_n (n = numérotation globale, 80 à 649). Défaut S_n = (n − ½) − (θ(γ_n)/π + 1).
P0 : S_n = Φ(γ_n)/π + c, c entier constant (écart < 10⁻³) : le défaut d'une porte est la phase des cavités lue sur la porte.
P1 : défaut cumulé C(N) = Σ_{n≤N} S_n prédit SANS AJUSTEMENT (sauf une constante) par la danse en cosinus :
  P(N) = (1/π) Σ_{p,m} w · p^(−m/2)/m · ρ(γ_N) · cos(m γ_N ln p)/(m ln p) + Φ(γ_N)²/(2π²) + ½ S_N,  ρ(t) = ln(t/2π)/2π.
  Corrélation C/P > 0,98 ; écart quadratique résiduel < 10 % de l'écart quadratique de C.
P2 : le seul terme p = 2 (m = 1) explique déjà plus de 25 % de la variance de C (petits premiers en tête).

## T2. La résonance des cavités avec les portes à p^m = X = t/2π (fenêtre V2, 30 000–30 300 : t/2π ≈ 4 775–4 823)
Balayage D(q) = |(1/N) Σ_n q^(iγ_n)| sur les 404 vraies portes, q de 2 à 10⁸ (pas logarithmique 0,001 en ln q).
P3 : le maximum global de D est atteint pour q à ±3 % de t₀/2π = 4 799 (la frontière de l'horloger), avec D_max entre 0,15 et 0,40.
P4 : D_max ≈ |moyenne de e^(−2πi S_n)| (la résonance lit la danse elle-même) à 0,05 près.
P5 : hors de la zone q ∈ [0,9 ; 1,1]·t₀/2π, la médiane de D est < 0,07 ; pas de pic de résonance à q ≈ (t₀/2π)² (D < 0,12 dans ±5 % autour).
Lecture si P3-P5 réussissent : les portes battent à la fréquence ln(t/2π) ; une cavité p^m = X vibre à la même fréquence, ses erreurs ne se compensent plus. La règle d'horloger X = t/2π est la première résonance cavités-portes.
