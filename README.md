# The Door Instrument

*An instrument that plays the Riemann zeros from the primes alone, and a spectrometer that recovers the primes from the zeros alone.*

Open project born from ABL_M81's π project, carried out with Claude (Anthropic's AI assistant), October 2026.
French version: `README.fr.md`. Every document exists in English and in French (a `.fr.md` file, or the French file name, alongside). Two things stay in French: the sealed predictions in `2-banc-d-essai/predictions/` (their SHA-256 fingerprints forbid any edit) and the comments in the code.

---

## In one sentence

The zeros of the Riemann zeta function are treated here not as numbers to compute but as **doors**: a plate pierced at those doors lets only the primes through, and cavities tuned to the primes place the doors. The repository provides the instrument, the spectrometer, and a test bench that replays every result.

## What the instrument does

Using **the primes alone**, it places the doors (the zeros of ζ on the critical line) by combining three foundations:

1. **curvature**: the measuring axis winds according to the Riemann-Siegel angle θ(t);
2. **two equal slits**: the wave and its mirror image (s and 1 − s), combined in a cosine;
3. **cavities**: each prime p is an infinite-echo cavity with factor (1 − p^(−1/2 − it))^(−1).

A door is a sign change of cos(θ(t) + Σ_p arg (1 − p^(−1/2 − it))^(−1)), the sum running over primes p ≤ t/2π (the clockmaker's rule), with a smoothed edge.

Verified results (every prediction was written and sealed before its computation):

| Measure | Result |
|---|---|
| doors played from t = 14 to t = 2,000,000 | none missed, none added |
| doors within 0.1 local spacing of the true position | 1,389 / 1,391 = 99.86 % (four blind windows) |
| mean error | 0.020 to 0.033 local spacing, constant over four orders of magnitude |
| clockmaker's exponent | κ = 1.007 / 1.030 / 0.952 / 0.961 (cavities up to t/2π) |

## What the spectrometer does

Light a plate pierced at the zeros: the response R(x) = −(4π/T)·√x·Σ cos²(πγ/2T)·cos(γ ln x) lights up at prime powers (height ln p) and stays dark elsewhere (Landau's formula, 1911).

- **Aperture**: the more doors open, the more primes can be read (up to about T/2π).
- **Tuning knob**: queries one number at a time; 100 % correct classification up to 120.
- **Colour filters**: with the zeros of Dirichlet L-functions (χ₃, χ₄, χ₅), the spectrometer separates the primes by class (3k ± 1, 4k ± 1, residues mod 5): 99.3 to 100 % up to 150.
- **Reverse direction**: from the first 1,004 zeros alone, the 55 primes up to 262 and their 54 gaps are recovered without error.

An interactive version is in `5-communaute/spectrometre-de-riemann.html`.

## What is known, what is new

The ingredients are classical: the explicit formula (Riemann, von Mangoldt), Landau's formula, Selberg's approximation of S(t), the Riemann-Siegel formula, the hybrid formula of Gonek, Hughes and Keating, the Berry-Keating dynamics (H = xp), and GUE statistics (Montgomery, Dyson, Odlyzko).

What this project contributes, without overstating it:
- an **architecture** built on three foundations, and proof by disassembly that each one is load-bearing (without curvature 26 % of doors; primes alone 17 %; without an Euler product a door leaves the critical line, as for the Davenport-Heilbronn function);
- the **cube law**: a quantum graph with two passages per string, tuned on p and p², plays p³ with a ratio of exactly −2 (with k channels: error at p^(k+1), ratio −k);
- the measured **clockmaker's rule** (κ = 1) and the same constant 2π found along three routes: forward (cavities up to t/2π), backward (reading up to T/2π), and geometric (one door per Planck cell, h = 2π; fitted h′ = 6.28318);
- a tunable **spectrometer** with colour filters, and a visual explanation of Chebyshev's bias (prime squares all pass through the 4k + 1 filter);
- a **method**: every computation is preceded by a written prediction sealed with a SHA-256 fingerprint, and failures are recorded as they are.

Nothing here proves the Riemann Hypothesis.

## Repository layout

| Folder | Contents |
|---|---|
| `1-specification/` | the technical specification of the instrument and the spectrometer |
| `2-banc-d-essai/` | the Python package `portes`, data, sealed predictions, tests |
| `3-references/` | comparison with public tables (Odlyzko, LMFDB) |
| `4-theorie/` | links to the literature, open questions (`THEORY.md`) |
| `5-communaute/` | interactive spectrometer, contribution guide (`CONTRIBUTING.md`), microwave-network build plan (`build-plan.md`) |

## Running the test bench

Python 3.10 or later, with `numpy` and `scipy`; `mpmath` is only needed for cross-checks.

```
cd 2-banc-d-essai
python lancer_les_tests.py          # 14 fast tests (about 15 seconds)
python lancer_les_tests.py --lents  # + 3 slow tests: windows at 3·10⁵ and 2·10⁶, recomputation of the Dirichlet zeros (about 1 extra minute)
```

The tests can also be run with `pytest`.

## Licences

- Code: MIT licence (`LICENSE`).
- Texts, figures and data: Creative Commons Attribution 4.0 International (`LICENSE-CC-BY-4.0.md`).

How to cite: see `CITATION.cff`.
