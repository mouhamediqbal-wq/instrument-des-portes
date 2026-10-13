# 6 · Born, the edge and the comb

*English version. Version française : `README.fr.md`.*

A supplementary part, distinct from the instrument itself (folders 1 to 5). It starts from Born's canonical commutation relation and asks what it says about the doors. Same method as the rest of the repository: every prediction was written and sealed with a SHA-256 fingerprint **before** the computation (`predictions/`), and failures are reported as they are (`resultats/`, in French).

## 1. Born's relation and the edge (prediction `born`, 5/5 passed)
Born and Jordan (1925): qp − pq = iħ·1, with ħ = h/2π. It cannot hold for finite matrices: the trace of a commutator is 0, the trace of iħ·1 is iħ·n. Truncating the harmonic-oscillator matrices at size n gives qp − pq = i·diag(1, …, 1, −(n − 1)): exact everywhere except the last cell, which carries the whole defect.
With a soft edge, the defect spreads and stays **bounded, independent of the size**: linear edge 3.00, rounded edge 3.05, splayed edge 2.11, optimal edge 1 + K/w for an edge of width w. The total defect is always exactly −n (trace theorem): it can be moved, never removed.

## 2. Conservation of the defect in the doors (prediction `born 2`: B1–B3 passed, A2 failed)
Defect of door n: S_n = (n − ½) − (θ(γ_n)/π + 1), its offset from its Planck cell. The cumulative sum Σ S_n over the first 1,004 zeros never exceeds **0.58** (shuffled controls: 6.6). The doors of the instrument, built from the primes alone, show the same property (0.78 against 5.1), and the instrument's own errors compensate each other (0.18 against 0.86 for random signs). This is the analogue of Born's trace; for the true zeros it reflects Littlewood's theorem (∫ S = O(log T)).
Reported failure (A2): we predicted that the rounded edge would beat a linear edge in the instrument; the linear edge is in fact very slightly better (1–3 %), as in Born's case.

## 3. The trace dances in cosine (prediction `born 3`: P0, P2, P5 passed; P1 partly, P3 failed)
The defect of a door of the instrument is exactly the cavity phase read at the door: S_n = Φ(γ_n)/π (to 2·10⁻⁶). Its cumulative sum follows a cosine dance predicted from the primes alone (correlation 0.982; the amplitude is not yet within 10 %), with p = 2 alone explaining 44 % of the variance.
Probing the doors with q^{iγ} reveals resonances around X = t/2π. Prediction P3 (the strongest at X) failed: the strongest is at 2X, and the resonances form a **comb**.

## 4. The Möbius comb (prediction `born 4`, 4/4 passed)
Expanding the dance of the doors prime by prime (Jacobi–Anger expansion, Bessel functions) predicts the whole comb: relative to the tooth at X, the tooth at q = (a/b)·X has height

  R(a/b) = μ(a) · Π_{p|a} √p/(p − 1) · b^(−1/2)

(μ = Möbius function; no tooth when a has a square factor). On 2,125 true zeros (7 windows from 200 to 2·10⁶): **15 signs out of 15**, mean deviation **0.07**, no tooth at 4X, 8X, 9X, 12X, 18X, tallest teeth 2X then 6X.

## Status in the literature (checked 13 October 2026)
- Known: the measured sum is Σ χ(ρ)⁻¹ r^{iγ}; Σ χ(ρ) = −T/2π (height at X ≈ −1/log(t/2π)); the teeth X/b of height b^(−1/2); the change of regime exactly at X = T/2π and X = T/π = 2X (Gonek, Fujii; arXiv 2601.18025).
- **Not found**: the teeth a·X with Möbius sign μ(a) and height Π √p/(p − 1). Not found does not mean new: the full texts of Gonek (1993) and Fujii (2012) were not consulted. Our derivation is heuristic (the Euler product does not converge on the critical line); only the measurements support it. Corrections and references are welcome (open an Issue).

## Note on the sealed predictions
In the four prediction texts, the first name of the person who asked the question was replaced by the pseudonym ABL_M81 **after** sealing; nothing else was changed. The fingerprints in `predictions/` are those of the published texts; the original fingerprints (computed before each computation, and quoted in `resultats/`) were:

| Prediction | Original fingerprint (before computation) | Published text |
|---|---|---|
| born | caf5a41b5358169f3cbd93b6a9ca9e579f38686798ab3a883ae28215716aaab3 | abf6f1d66a8bd829e588a03425a02f068703c089f6ef3ceb810a179624ac6892 |
| born 2 | 481886716cb380ca4bc20d0c8bc1be8381efcdea62bc0dd613ea47f656108f60 | 940340d4304ec87646c7d5f785cd753c8cfd0e2702d99b1e731a7bd63a965e47 |
| born 3 | 7e567aa544b63b69246ef9575e5c5d3585dc1f23e8e8f5b6bd8a4729539b0f21 | c744f5fb97c12ab5f9ff5a81629598881ebb0c05c25b754efa5080c8f06c2936 |
| born 4 | 1d7a2af6ee21c55fb4458ea71fc159c0684459cd78b6cac8a94e580c46f4da5f | a0ad231e9462f834e59f2e94a60136dc344320fe40a741291e84bfcc9c728770 |

## Reproducing
```
cd 6-born/scripts
python born.py   # 1. Born and the edge (seconds)
python born2.py  # 2. edges in the instrument, conservation (about 1 minute)
python born3.py  # 3. cosine dance and resonance scan (about 1 minute)
python born4.py  # 4. Möbius comb (seconds)
python figure.py; python figure2.py; python figure3.py; python figure4.py   # figures/
```
Fast checks are part of the test bench: `2-banc-d-essai/tests/test_born.py`.

## Open questions
- Why does the instrument conserve its defect? Write the exact analogue of Born's trace for the instrument.
- Prove (or find in the literature) the law of the teeth a·X with the Möbius sign.
