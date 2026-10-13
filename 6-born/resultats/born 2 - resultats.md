# Born 2 : le bord linéaire et la conservation du défaut — résultats (13/10/2026, 21h30) — prédiction : empreinte 48188671…

## A. Bords arrondi / linéaire dans l'instrument
| Fenêtre | Bord | Portes | Justes | Erreur moyenne | Erreur max |
|---|---|---|---|---|---|
| V1 200–1 000 | arrondi | 570/570 | 100 % | 0,0255 | 0,0899 |
| V1 | linéaire | 570/570 | 100 % | 0,0247 | 0,0876 |
| V2 30 000–30 300 | arrondi | 404/404 | 100 % | 0,0287 | 0,0948 |
| V2 | linéaire | 404/404 | 100 % | 0,0285 | 0,0957 |
| V3 300 000–300 150 | arrondi | 257/257 | 100 % | 0,0300 | 0,0906 |
| V3 | linéaire | 257/257 | 100 % | 0,0298 | 0,0901 |
A1 ✓ : bon nombre de portes partout.
A2 ✗ (échec consigné) : l'arrondi n'a l'erreur maximale la plus faible que dans 1 fenêtre sur 3 (V2), et l'erreur moyenne la plus faible dans aucune. Le linéaire est très légèrement meilleur (1 à 3 %) : la surprise de Born se retrouve dans l'instrument, dans le même sens, mais avec un écart minime. Les deux bords sont équivalents en pratique (100 % de portes justes partout).

## B. Conservation du défaut
B1 ✓ : vraies portes (1 004) : max |Σ S_n| = 0,575 (somme finale +0,213) ; témoins mélangés : médiane 6,62, 1er centile 3,41 ; la vraie valeur est en dessous de tous les 2 000 témoins.
B2 ✓ : portes de l'instrument (V1, 570, numérotées à partir de 80) : max |Σ S_n| = 0,783 ; témoins : médiane 5,12, 1er centile 2,63 ; en dessous de tous les témoins.
B3 ✓ : erreurs de l'instrument (V1) : max |Σ e_n| = 0,179 (somme −0,160) ; témoins à signes au hasard : médiane 0,856, 5e centile 0,461 ; en dessous de tous les témoins.
Lecture : comme chez Born (trace nulle), le défaut des portes ne s'accumule pas : il se déplace et se compense (Littlewood : ∫ S = O(log T)). L'instrument hérite de cette loi : ses propres erreurs se compensent aussi, 5 fois mieux que du bruit. Ce qui reste ouvert : pourquoi l'instrument la respecte (l'analogue exact de la trace reste à écrire).
