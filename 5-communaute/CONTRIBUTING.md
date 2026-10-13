# Contributing

*English version. Version française : `CONTRIBUER.md`.*

This project keeps one simple rule: **write the prediction before computing, and publish the result as it is, failures included.**

## Proposing an experiment
1. Write a file "<name> - prediction preenregistree.md" in `2-banc-d-essai/predictions/`: the question, the exact method, and numerical success thresholds.
2. Seal it: `sha256sum "<file>" > "empreinte <name>.txt"`, and publish both BEFORE running the computation (a commit is enough to date it).
3. Run the computation, then add "<name> - resultats.md" with each prediction marked as passed or failed.
4. If the result can be reproduced in under a few minutes, add a test in `2-banc-d-essai/tests/`.

## Welcome contributions
- A refutation: a window, a height or a character where the instrument or a filter fails.
- A theoretical explanation of a measured rule (see `4-theorie/THEORY.md`, open questions).
- A physical realisation (see `build-plan.md`).

## What we avoid
- Tuning a setting on the true zeros and then presenting the result as a prediction.
- Announcing a proof of the Riemann Hypothesis.
