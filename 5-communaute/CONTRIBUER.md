# Contribuer

*Version française. English version: `CONTRIBUTING.md`.*

Ce projet garde une règle simple : **on écrit la prédiction avant de calculer, et on publie le résultat tel quel, échec compris.**

## Proposer une expérience
1. Écrivez dans `2-banc-d-essai/predictions/` un fichier « <nom> - prediction preenregistree.md » : la question, la méthode exacte, les seuils de réussite chiffrés.
2. Scellez-le : `sha256sum "<fichier>" > "empreinte <nom>.txt"` et publiez les deux AVANT de lancer le calcul (un commit suffit à dater).
3. Lancez le calcul, puis ajoutez « <nom> - resultats.md » avec chaque prédiction marquée réussie ou échouée.
4. Si le résultat est reproductible en moins de quelques minutes, ajoutez un test dans `2-banc-d-essai/tests/`.

## Ce qu'on accepte volontiers
- Une réfutation : une fenêtre, une hauteur ou un caractère où l'instrument ou un filtre échoue.
- Une explication théorique d'une règle mesurée (voir `4-theorie/THEORIE.md`, questions ouvertes).
- Une réalisation physique (voir `plan-de-montage.md`).

## Ce qu'on évite
- Ajuster un réglage sur les vrais zéros puis présenter le résultat comme une prédiction.
- Annoncer une démonstration de l'hypothèse de Riemann.
