# La commutation de Born et le bord — prédiction préenregistrée (13/10/2026, 21h25, Paris) — écrite AVANT calcul

Question (ABL_M81) : quand on coupe les matrices infinies de Born, l'erreur se loge-t-elle au bord comme celle de nos cavités, et un bord arrondi l'apprivoise-t-il comme pour l'instrument ?

Montage : oscillateur harmonique, ħ = 1. Opérateur a tronqué : a(k−1, k) = √k · f(k), k = 1…n−1 (états 0…n−1), f = profil de bord ; q = (a + a†)/√2, p = (a − a†)/(i√2). Alors qp − pq = i·[a, a†] est diagonale : C(k) = (k+1) f(k+1)² − k f(k)² (avec f(n) = 0). Cible : C(k) = 1 partout (Born : [q, p] = i·1). Erreur e(k) = C(k) − 1.
Profils (K = nombre d'états gardés intacts, f = 1 pour k ≤ K) :
- NET : n = K + 1 (coupure franche) ;
- LINÉAIRE (type Selberg) : f² = 1 − (k − K)/K jusqu'à 2K ;
- ARRONDI (notre bord) : f² = ½(1 + cos(π(k − K)/K)) jusqu'à 2K ;
- ÉBRASÉ : même demi-cosinus étiré de K à 4K ;
- OPTIMAL de largeur w : k f(k)² = K − (k − K)·K/w (valeur constante −K/w sur le bord).

Prédictions (K = 50, 500, 5 000) :
P1 (théorème de la trace) : pour tout profil, Σ e(k) = −n exactement (à 10⁻⁹ près relatif). Le défaut total ne disparaît jamais : il ne peut qu'être déplacé.
P2 (NET) : e = 0 sur les K premiers états ; un seul défaut, e = −(K + 1), qui grandit avec K.
P3 (bords de largeur K) : max |e| indépendant de K (à 1 % près) : LINÉAIRE 3,00 ± 0,02 ; ARRONDI 3,05 ± 0,05 ; OPTIMAL 2,00 ± 0,01. Les K premiers états restent exacts (|e| < 10⁻⁹).
P4 (ÉBRASÉ, largeur 3K) : max |e| = 2,11 ± 0,05 ; OPTIMAL de largeur 3K : 1,333 ± 0,01.
P5 (borne) : aucun bord de largeur w ne fait mieux que max |e| = 1 + K/w ; l'OPTIMAL l'atteint.
Lecture attendue : l'analogie tient pour la forme (bord nécessaire, erreur bornée et constante au lieu de croître), mais Born impose une loi que nos portes ne montrent pas : le défaut total est conservé (−n), seul son étalement est réglable.
