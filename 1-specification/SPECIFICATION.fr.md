# Spécification de l'instrument des portes — version 0.1 (13 octobre 2026)

*Version française. English version: `SPECIFICATION.md`.*

Ce document définit l'instrument et le spectromètre de façon à ce qu'on puisse les réécrire sans lire le code. Les numéros de section servent de référence dans le code (`portes/`) et dans les tests.

## 1. Vocabulaire

| Terme | Sens précis |
|---|---|
| **porte** | un zéro non trivial ½ + iγ de ζ (ou d'une fonction L), repéré par sa hauteur γ > 0 ; sur la droite critique, un changement de signe de la fonction réelle Z(t) |
| **corde, cavité** | le facteur d'Euler d'un premier p, vu comme une cavité de longueur ln p et de réflectivité p^(−1/2) ; « cavité » = tous les échos m = 1, 2, 3… ; « corde simple » = l'écho m = 1 seul |
| **écart local** | l'écart moyen entre portes à la hauteur t : 2π / ln(t/2π) |
| **porte juste** | porte de l'instrument à moins de 0,1 écart local d'une vraie porte |
| **courbure** | l'angle θ(t) de Riemann-Siegel (§ 2.1) |
| **case de Planck** | une case de surface h = 2π dans l'espace des phases du flot H = xp (§ 4) |

## 2. L'instrument (des premiers vers les portes)

### 2.1 La courbure
θ(t) = (t/2)·ln(t/2π) − t/2 − π/8 + 1/(48t) + 7/(5760t³).
Écart à la forme exacte arg Γ(¼ + it/2) − (t/2) ln π : 7·10⁻¹⁰ à t = 14, < 10⁻¹⁸ au-delà de 10³ (en précision infinie ; en nombres flottants double, l'arrondi domine : 6·10⁻¹¹ à 10⁶).

### 2.2 Les deux fentes égales
La sortie est un cosinus : Z_inst(t) = cos(θ(t) + Φ(t)). Réelle par construction, elle ne s'annule qu'en changeant de signe : chaque zéro est une porte.

### 2.3 Les cavités
Φ(t) = Σ_p Σ_m W(m·ln p / ln X) · Im(p^(−m(1/2 + it))) / m, soit, sans pondération, Σ_p arg (1 − p^(−1/2 − it))^(−1).

### 2.4 Les réglages figés
- **Règle d'horloger** : X = t/2π (au centre de la fenêtre jouée). Mesurée : κ = ln X / ln(t/2π) = 1,007 ; 1,030 ; 0,952 ; 0,961 à t ≈ 1,2·10³ ; 10⁴ ; 10⁵ ; 10⁶ (plus petit X donnant 99 %).
- **Bord** (pondération W, u = ln n / ln X) :
  - coupure nette : W = 1 si u ≤ 1, sinon 0 ;
  - **bord arrondi (recommandé)** : W = 1 jusqu'à u = 1, puis demi-cosinus jusqu'à 0 en ln n = ln(2X) ;
  - variantes testées : ébrasement (jusqu'à 4X), réflecteur (palier ½ de X à 2X puis demi-cosinus jusqu'à 4X).
  - À éviter : W = 1 − u (Selberg, même X) : moins bon, et une note parasite à 2·10⁶.

### 2.5 Sortie
Les portes de l'instrument = changements de signe de Z_inst sur une grille de pas 0,002 (interpolation linéaire).

### 2.6 Domaine de validité vérifié

| Fenêtre | X | Portes / vraies portes | Justes (bord arrondi) | Erreur moyenne |
|---|---|---|---|---|
| 200 – 1 000 | 95 | 570 / 570 | 100 % | 0,026 |
| 30 000 – 30 300 | 4 799 | 404 / 404 | 100 % | 0,029 |
| 300 000 – 300 150 | 47 758 | 257 / 257 | 100 % | 0,030 |
| 2 000 000 – 2 000 080 | 318 316 | 160 / 160 | 98,8 % | 0,033 |

Sans aucune note parasite, y compris sous la première porte (trou central de −14,13 à 14,13).

## 3. Le spectromètre (des portes vers les premiers)

### 3.1 La plaque
Portes γ₁ < γ₂ < … ≤ T, ouverture w(γ) = cos²(πγ/2T).

### 3.2 La réponse
R(x) = −(4π/T)·√x·Σ_γ w(γ)·cos(γ ln x).
Par la formule de Landau, R(x) → Λ(x) (ln p si x = p^k, 0 sinon) quand la résolution suffit.

### 3.3 Réglages
- **Diaphragme** : nombre de portes ouvertes ; lecture fiable jusqu'à environ T/2π (1 004 portes, T ≈ 1 424 : premiers exacts jusqu'à 262 ; 54/54 entiers bien classés jusqu'à 55).
- **Accord** : seuil R(x) > 0,35 → « clic ». 100 % de bons classements jusqu'à 120 ; 99,5 % jusqu'à 200 (seule erreur : 128 = 2⁷).
- **Filtres de couleur** : plaque de L(s, χ) pour un caractère réel primitif χ ; « + » = (R_ζ + R_χ)/2 laisse passer les p^k avec χ(p^k) = +1, « − » = (R_ζ − R_χ)/2 ceux avec χ(p^k) = −1. Vérifié pour χ₃, χ₄, χ₅ jusqu'à T = 1 000 : 99,3 à 100 % sur les entiers 2 à 150.

### 3.4 Lecture des premiers à partir des portes seules
ψ̂(x) = x − Σ_γ w(γ)·2 Re(x^ρ/ρ) − ln 2π − ½ ln(1 − x^(−2)) ; Λ̂(n) = ψ̂(n + ½) − ψ̂(n − ½) ; n est premier si Λ̂(n) > 0,35 et Λ̂(n) > 0,75·ln n.

## 4. La constante d'échange 2π

- Aller : cavités jusqu'à t/2π (§ 2.4).
- Retour : lecture jusqu'à T/2π (§ 3.3).
- Géométrie : N(E) = aire de {x ≥ ℓx, p ≥ ℓp, xp ≤ E}, ℓx·ℓp = h, divisée par h, moins 1/8 = (E/2π)(ln(E/2π) − 1) + 7/8 pour h = 2π (Berry-Keating). Sur les 1 004 premières portes, l'écart (n − ½) − N(γ_n) a une moyenne +0,0002, un écart-type 0,26 et un maximum 0,73 ; la valeur de h qui ajuste le mieux est 6,28318 (2π = 6,28319). Cette valeur est garantie par la formule de Riemann-von Mangoldt : la mesure la confirme.

## 5. Défauts de structure connus (pour les réalisations en graphe ou en câbles)

- **Loi des cubes** : une corde vue d'un sommet a deux sens de passage ; son facteur est un polynôme de degré 2 en y = x/√p. Accorder p (1/√p) et p² (1/(2p)) impose 1 + y + y² = (1 − y³)/(1 − y), d'où un coefficient de p³ égal à −2/(3p^(3/2)) au lieu de +1/(3p^(3/2)) (rapport −2). Avec k canaux : juste jusqu'à p^k, puis rapport −k en p^(k+1).
- **Composés à trois pas** (pqr, p²q) : non contraints par une optimisation à deux pas ; ils font croître l'erreur avec le nombre de cordes. Les éteindre (suppresseur) rend l'ajout de cordes bénéfique.

## 6. Ce que l'instrument n'est pas

- Ce n'est pas un opérateur auto-adjoint au sens de Hilbert-Pólya.
- Il ne démontre rien sur l'hypothèse de Riemann.
- Pour calculer des zéros, la formule de Riemann-Siegel est plus économique (√(t/2π) termes contre t/2π premiers). L'intérêt de l'instrument est ailleurs : il n'utilise que les premiers, il donne l'anatomie de chaque porte, et il forme avec le spectromètre une circulation fermée.
