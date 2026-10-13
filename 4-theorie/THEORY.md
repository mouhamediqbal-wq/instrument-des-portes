# Theory: what is known, what is new, what remains open

*English version. Version française : `THEORIE.md`.*

## 1. The classical sources the instrument rests on

| Part of the instrument | Known result |
|---|---|
| doors ↔ primes | explicit formula (Riemann 1859, von Mangoldt 1895) |
| plate pierced at the zeros → prime powers | Landau's formula (1911): Σ_{0<γ≤T} x^{iγ} ≈ −(T/2π) Λ(x)/√x |
| curvature θ(t), two equal slits | Riemann-Siegel formula; functional equation s ↔ 1 − s, \|χ(½ + it)\| = 1 |
| cavities up to X | approximation of S(t) by the truncated Euler product (Selberg); hybrid formula of Gonek, Hughes and Keating (2007) |
| one door per Planck cell | Riemann-von Mangoldt formula; H = xp model of Berry and Keating (1999) |
| repulsion between doors | pair correlation (Montgomery 1973), GUE (Dyson, Odlyzko) |
| symmetry alone is not enough | Davenport-Heilbronn function (1936); Selberg's conjecture for his class |
| colour filters | explicit formula for Dirichlet L-functions |
| Chebyshev's bias | Rubinstein and Sarnak (1994) |

## 2. What the project adds

1. **The three-foundation architecture** (curvature, equal slits, cavities) and its verification by disassembly: without curvature 26 % of doors, primes alone 17 %, 1 + primes 43 %, cavities 77 %, then 100 % with enough cavities; without an Euler product, a door leaves the line (0.8085 + 85.6993 i).
2. **The measured clockmaker's rule**: X = t/2π (κ = 1.007 / 1.030 / 0.952 / 0.961), which keeps the precision constant from 200 to 2·10⁶; the rounded edge beyond X.
3. **The cube law** for quantum graphs with two passages per string (ratio −2 on p³; −k on p^(k+1) with k channels): a structural defect predictable without knowing the zeros.
4. **The same constant 2π along three routes**: forward, backward, geometry.
5. **The tunable spectrometer** (diaphragm, tuning knob, filters) and a visual reading of Chebyshev's bias (the squares all pass through 4k + 1).
6. **The method**: 28 predictions sealed with a fingerprint before computation, failures included.

## 3. Open questions (good first contributions)

1. **Derive κ = 1 from theory.** Does Selberg's variance of S(t) − S_X(t) say that X = t/2π is the 99 % threshold? Why the same constant as in N(T)?
2. **The two stubborn doors at 2·10⁶** (0.12 spacing): narrow Lehmer-type doors? effect of the grid step? an edge to refine?
3. **The Berry-Keating paradox**: a physical system whose orbits of period ln p all have the same instability (λ = 1) gives, through Gutzwiller, amplitudes p^(−m/2)/(1 − p^(−m)) rather than p^(−m/2), and arbitrary phases rather than all equal to π. What real object would produce exactly the instrument's echoes?
4. **The closed loop**: the instrument places its doors from the primes; does shining light through ITS doors give back the same primes, with no reference to the true zeros?
5. **The four plates** (Poisson, crystal, GUE, Riemann): check that only the Riemann plate lets the primes through, and that the primes live in the long-range correlations (Bogomolny-Keating), not in the local repulsion.
6. **Complex characters**: extend the colour filters to complete classes mod 5, 7, 8… (non-real characters).
7. **Extreme heights**: the rule X = t/2π becomes impractical around 10¹²; which truncated version keeps 99 %?
8. **Conservation of the defect** (see `6-born/`): the cumulative defect of the instrument's doors stays bounded, like the trace of Born's commutator. Why? Write the exact analogue of the trace.
9. **The Möbius comb** (see `6-born/`): the resonances of the doors at q = (a/b)·t/2π follow μ(a) · Π_{p|a} √p/(p − 1) · b^(−1/2) on 2,125 zeros. Prove it, or find it in the literature (the teeth X/b are known; the teeth a·X were not found).

## 4. References

- B. Riemann, *Über die Anzahl der Primzahlen unter einer gegebenen Grösse* (1859).
- E. Landau, *Über die Nullstellen der Zetafunktion*, Math. Ann. 71 (1911).
- H. Montgomery, *The pair correlation of zeros of the zeta function* (1973).
- M. V. Berry, J. P. Keating, *The Riemann zeros and eigenvalue asymptotics*, SIAM Review 41 (1999).
- S. M. Gonek, C. P. Hughes, J. P. Keating, *A hybrid Euler-Hadamard product for the Riemann zeta function*, Duke Math. J. 136 (2007).
- M. Rubinstein, P. Sarnak, *Chebyshev's bias*, Experimental Math. 3 (1994).
- H. Davenport, H. Heilbronn, *On the zeros of certain Dirichlet series* (1936).
- H. M. Bui, J. B. Conrey, M. P. Young, *More than 41% of the zeros of the zeta function are on the critical line*, arXiv:1002.4127.
- B. Rodgers, T. Tao, *The de Bruijn-Newman constant is non-negative*, Forum Math. Pi (2020).
- O. Hul et al., *Experimental simulation of quantum graphs by microwave networks*, arXiv:nlin/0404006.
- M. D. Johnson et al., *Universal interferometric signatures of a black hole's photon ring*, arXiv:1907.04329.
