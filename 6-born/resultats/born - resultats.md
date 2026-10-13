# La commutation de Born et le bord — résultats (13/10/2026, 21h26) — prédiction : empreinte caf5a41b…
P1 ✓ : Σ e = −n exactement pour les 18 cas (6 profils × K = 50, 500, 5 000). Termes hors diagonale < 6·10⁻¹⁴ (vérification matricielle complète jusqu'à n = 1 000).
P2 ✓ : NET : K premiers états exacts (< 2·10⁻¹³) ; un seul défaut de taille K + 1 (51 / 501 / 5 001), qui grandit avec K.
P3 ✓ : max |e| : LINÉAIRE 2,980 / 2,998 / 3,000 ; ARRONDI 3,048 / 3,050 / 3,050 ; OPTIMAL 2,000. K premiers états exacts.
P4 ✓ : ÉBRASÉ 2,112 ; OPTIMAL largeur 3K 1,333.
P5 ✓ : tous les bords respectent max |e| ≥ 1 + K/w (moyenne forcée du défaut sur le bord : −(K + w)/w) ; l'OPTIMAL l'atteint.
Observation : l'ARRONDI a un maximum un peu plus haut que le LINÉAIRE (3,05 contre 3,00) mais une zone perturbée plus étroite (|e| > 0,5 sur 0,91 K états contre K).
Lecture : l'analogie avec nos portes tient pour la forme — sans bord, l'erreur grandit avec la taille ; avec un bord, elle devient bornée et constante (comme la précision constante de l'instrument de 200 à 2·10⁶). Born ajoute une loi de conservation : le défaut total −n ne disparaît jamais, on choisit seulement où et comment il s'étale. Plus le bord est large, plus il est doux (1 + K/w). Aucune démonstration que nos portes obéissent à la même loi : c'est une piste.
