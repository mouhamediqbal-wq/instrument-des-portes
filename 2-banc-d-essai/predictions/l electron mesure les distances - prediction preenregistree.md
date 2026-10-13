# L'électron mesure les distances (Ritz à l'envers) — prédiction préenregistrée (13/10/2026, 14h37, Paris) — écrite AVANT calcul
Entrée : UNIQUEMENT les 1 004 premiers zéros γ (14,13 à 1 424,46). Aucun nombre premier n'est fourni.
Formule explicite (von Mangoldt) : ψ(x) = x − Σ_ρ x^ρ/ρ − ln 2π − ½ ln(1 − x^{−2}), somme sur les zéros pondérée par w(γ) = cos²(πγ/2T), T = 1 425 (bord adouci fixé d'avance).
Pour chaque entier n ≥ 2 : Λ̂(n) = ψ(n + ½) − ψ(n − ½). Décision : n est une puissance de premier si Λ̂(n) > 0,35 ; c'est un PREMIER si de plus Λ̂(n) > 0,75 · ln n (pour p^k, Λ = ln p = ln n / k).
Sorties : la liste des premiers trouvés, les espaces entre eux, la première erreur (premier manqué, faux premier, espace faux).
Prédictions de Claude :
E1 : tous les premiers et tous les espaces sont exacts au moins jusqu'à 100.
E2 : la première erreur apparaît avant 400.
E3 : les puissances de premiers (4, 8, 9, 16, 25, 27, 32, 49…) sont reconnues comme puissances et non comme premiers jusqu'à 100.
