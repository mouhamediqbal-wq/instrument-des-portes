# Specification of the Door Instrument — version 0.1 (13 October 2026)

*English version. Version française : `SPECIFICATION.fr.md`.*

This document defines the instrument and the spectrometer precisely enough to rewrite them without reading the code. Section numbers are used as references in the code (`portes/`) and in the tests.

## 1. Vocabulary

| Term | Precise meaning |
|---|---|
| **door** | a non-trivial zero ½ + iγ of ζ (or of an L-function), identified by its height γ > 0; on the critical line, a sign change of the real function Z(t) |
| **string, cavity** | the Euler factor of a prime p, seen as a cavity of length ln p and reflectivity p^(−1/2); "cavity" = all echoes m = 1, 2, 3…; "single string" = the echo m = 1 alone |
| **local spacing** | the mean spacing between doors at height t: 2π / ln(t/2π) |
| **correct door** | a door of the instrument within 0.1 local spacing of a true door |
| **curvature** | the Riemann-Siegel angle θ(t) (§ 2.1) |
| **Planck cell** | a cell of area h = 2π in the phase space of the flow H = xp (§ 4) |

## 2. The instrument (from the primes to the doors)

### 2.1 Curvature
θ(t) = (t/2)·ln(t/2π) − t/2 − π/8 + 1/(48t) + 7/(5760t³).
Deviation from the exact form arg Γ(¼ + it/2) − (t/2) ln π: 7·10⁻¹⁰ at t = 14, < 10⁻¹⁸ beyond 10³ (in exact arithmetic; in double-precision floating point, rounding dominates: 6·10⁻¹¹ at 10⁶).

### 2.2 The two equal slits
The output is a cosine: Z_inst(t) = cos(θ(t) + Φ(t)). Real by construction, it can only vanish by changing sign: every zero is a door.

### 2.3 The cavities
Φ(t) = Σ_p Σ_m W(m·ln p / ln X) · Im(p^(−m(1/2 + it))) / m, that is, without weighting, Σ_p arg (1 − p^(−1/2 − it))^(−1).

### 2.4 Fixed settings
- **Clockmaker's rule**: X = t/2π (at the centre of the window being played). Measured: κ = ln X / ln(t/2π) = 1.007; 1.030; 0.952; 0.961 at t ≈ 1.2·10³; 10⁴; 10⁵; 10⁶ (smallest X giving 99 %).
- **Edge** (weighting W, u = ln n / ln X):
  - sharp cut-off: W = 1 if u ≤ 1, otherwise 0;
  - **rounded edge (recommended)**: W = 1 up to u = 1, then a half-cosine down to 0 at ln n = ln(2X);
  - variants tested: splay (up to 4X), reflector (plateau ½ from X to 2X, then half-cosine up to 4X).
  - To avoid: W = 1 − u (Selberg, same X): worse, and a spurious note at 2·10⁶.

### 2.5 Output
The doors of the instrument = sign changes of Z_inst on a grid of step 0.002 (linear interpolation).

### 2.6 Verified range

| Window | X | Doors / true doors | Correct (rounded edge) | Mean error |
|---|---|---|---|---|
| 200 – 1,000 | 95 | 570 / 570 | 100 % | 0.026 |
| 30,000 – 30,300 | 4,799 | 404 / 404 | 100 % | 0.029 |
| 300,000 – 300,150 | 47,758 | 257 / 257 | 100 % | 0.030 |
| 2,000,000 – 2,000,080 | 318,316 | 160 / 160 | 98.8 % | 0.033 |

No spurious note, including below the first door (central gap from −14.13 to 14.13).

## 3. The spectrometer (from the doors to the primes)

### 3.1 The plate
Doors γ₁ < γ₂ < … ≤ T, aperture w(γ) = cos²(πγ/2T).

### 3.2 The response
R(x) = −(4π/T)·√x·Σ_γ w(γ)·cos(γ ln x).
By Landau's formula, R(x) → Λ(x) (ln p if x = p^k, 0 otherwise) when the resolution is sufficient.

### 3.3 Settings
- **Diaphragm**: number of open doors; reliable reading up to about T/2π (1,004 doors, T ≈ 1,424: exact primes up to 262; 54/54 integers correctly classified up to 55).
- **Tuning knob**: threshold R(x) > 0.35 → "click". 100 % correct classification up to 120; 99.5 % up to 200 (only error: 128 = 2⁷).
- **Colour filters**: plate of L(s, χ) for a real primitive character χ; "+" = (R_ζ + R_χ)/2 lets through the p^k with χ(p^k) = +1, "−" = (R_ζ − R_χ)/2 those with χ(p^k) = −1. Verified for χ₃, χ₄, χ₅ up to T = 1,000: 99.3 to 100 % on the integers 2 to 150.

### 3.4 Reading the primes from the doors alone
ψ̂(x) = x − Σ_γ w(γ)·2 Re(x^ρ/ρ) − ln 2π − ½ ln(1 − x^(−2)); Λ̂(n) = ψ̂(n + ½) − ψ̂(n − ½); n is prime if Λ̂(n) > 0.35 and Λ̂(n) > 0.75·ln n.

## 4. The exchange constant 2π

- Forward: cavities up to t/2π (§ 2.4).
- Backward: reading up to T/2π (§ 3.3).
- Geometry: N(E) = area of {x ≥ ℓx, p ≥ ℓp, xp ≤ E}, with ℓx·ℓp = h, divided by h, minus 1/8 = (E/2π)(ln(E/2π) − 1) + 7/8 for h = 2π (Berry-Keating). Over the first 1,004 doors, the deviation (n − ½) − N(γ_n) has mean +0.0002, standard deviation 0.26 and maximum 0.73; the best-fitting value of h is 6.28318 (2π = 6.28319). This value is guaranteed by the Riemann-von Mangoldt formula: the measurement confirms it.

## 5. Known structural defects (for realisations as graphs or cables)

- **Cube law**: a string seen from a vertex has two directions of passage; its factor is a degree-2 polynomial in y = x/√p. Tuning p (1/√p) and p² (1/(2p)) forces 1 + y + y² = (1 − y³)/(1 − y), hence a coefficient of p³ equal to −2/(3p^(3/2)) instead of +1/(3p^(3/2)) (ratio −2). With k channels: correct up to p^k, then ratio −k at p^(k+1).
- **Three-step composites** (pqr, p²q): not constrained by a two-step optimisation; they make the error grow with the number of strings. Switching them off (suppressor) makes adding strings beneficial.

## 6. What the instrument is not

- It is not a self-adjoint operator in the Hilbert-Pólya sense.
- It proves nothing about the Riemann Hypothesis.
- For computing zeros, the Riemann-Siegel formula is cheaper (√(t/2π) terms against t/2π primes). The instrument's interest lies elsewhere: it uses only the primes, it gives the anatomy of each door, and together with the spectrometer it forms a closed circulation.
