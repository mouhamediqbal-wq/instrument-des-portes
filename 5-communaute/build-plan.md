# Build plan: the instrument in cables (draft for discussion with a laboratory)

*English version. Version française : `plan-de-montage.md`.*

Status: **calculation draft, not built, not verified in a laboratory.** It relies on the microwave networks that simulate quantum graphs (Hul et al., arXiv:nlin/0404006).

## Principle
A "flower": one central vertex and one loop of coaxial cable per prime p, with length proportional to ln p. The resonance spectrum of the network, measured with a vector network analyser, plays the role of the graph's notes; the doors are obtained by the assembly described in the specification (envelope + smoothed fluctuation), or directly by measuring the transmission phase.

## Dimensions (PTFE-dielectric cable, ε ≈ 2.06, velocity ≈ 0.70 c; scale ℓ₀ = 0.5 m)

| p | loop length ℓ₀ ln p |
|---|---|
| 2 | 0.347 m |
| 3 | 0.549 m |
| 5 | 0.805 m |
| 7 | 0.973 m |
| 11 | 1.199 m |
| 13 | 1.283 m |
| 17 | 1.417 m |
| 19 | 1.472 m |
| 23 | 1.568 m |
| 29 | 1.684 m |

Total length: 5.16 m (6 primes), 11.30 m (10 primes).
Frequency ↔ height correspondence: f = k·v/(2π ℓ₀) ≈ k × 66.5 MHz; k = 14.13 → 0.94 GHz; k = 100 → 6.65 GHz; k = 160 → 10.6 GHz: within the range of a standard analyser.

## The vertex
- **Simple version**: Kirchhoff (Neumann) junction, native in cables. This is the project's "Kirchhoff crossroads": it makes the composites audible (echoes at ln 6, ln 10…) and has GOE statistics if time-reversal symmetry is not broken.
- **Faithful version**: the project's optimised junction matrix (unitary 2n × 2n, flux on each loop). It is not native in cables; it can be realised by a network of couplers and phase shifters (Reck or Clements decomposition: n(2n − 1) elements, i.e. 66 for 6 primes), which is more natural in programmable integrated photonics than at microwave frequencies.
- **Breaking time-reversal symmetry** (GUE statistics of the zeros): a circulator or a ferrite element at the vertex.

## Expected defects, known in advance (specification § 5)
- **Cube law**: two passages per loop → the echo of p³ comes out with a ratio of −2; to be corrected by computation (it is known exactly) or by a three-channel loop.
- **Three-step composites**: to be switched off in the design of the vertex (wolf suppressor).
- **Cable losses**: they attenuate all echoes; they will have to be measured and compensated (the target is an amplitude of 1/√p per echo).

## What the measurement would bring
A physical object whose resonances follow the Riemann doors to the precision of the assembly (≈ 0.03 spacing for 10 to 15 primes in simulation), and a bench for testing the Berry-Keating paradox (amplitudes p^(−m/2), phases).
