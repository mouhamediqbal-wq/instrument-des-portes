# Born 3 : la trace de l'instrument danse en cosinus, et la résonance de l'horloger — résultats (13/10/2026, 21h40) — prédiction : empreinte 7e567aa5…

## T1 (fenêtre 200–1 000, 570 portes de l'instrument)
P0 ✓ : S_n = Φ(γ_n)/π exactement (c = 0, écart max 2·10⁻⁶) : le défaut d'une porte est la phase des cavités lue sur la porte.
P1 ✗ (échec partiel consigné) : corrélation entre défaut cumulé mesuré et danse en cosinus prédite (premiers seuls, sans ajustement) = 0,982 (seuil 0,98 ✓) ; mais résidu = 18,8 % de l'écart-type (seuil 10 % ✗). La forme est la bonne ; l'amplitude n'est pas encore exacte à 10 % près (approximation intégrale de la somme discrète).
P2 ✓ : le seul terme p = 2 explique 43,6 % de la variance (coefficient ajusté 0,92 pour 1 attendu).

## T2 (fenêtre 30 000–30 300, 404 vraies portes, q de 2 à 10⁸)
P3 ✗ : le maximum global n'est pas à X = t/2π (4 799) mais à 2X (q = 9 596, D = 0,155).
P4 ✓ formel, non probant : D_max − |moyenne e^(−2πiS_n)| = 0,155 − 0,108 = 0,047 < 0,05, mais au mauvais endroit. (Lecture hors prédiction : à q = X exactement, D = 0,106, et la caractéristique de la danse vaut 0,108.)
P5 ✓ : médiane hors zone 0,034 ; autour de X² : max 0,110 < 0,12.

## Observation hors prédiction (à sceller avant de la tester)
Les résonances forment un peigne aux multiples et fractions simples de X : ½X (0,124), ⅔X (0,113), X (0,106), 2X (0,155), 3X (0,136), 6X (0,143), 10X (0,131), 14X (0,139). Hypothèse : c'est l'image, par la symétrie s ↔ 1 − s (les deux fentes égales), des pics de Landau ; la frontière X de l'horloger est le centre du miroir, et 2X — la fin de notre bord arrondi — sa première dent la plus forte.
