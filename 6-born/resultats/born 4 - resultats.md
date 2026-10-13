# Born 4 : la trigonométrie remet de l'ordre dans le peigne — résultats (13/10/2026, 21h47) — prédiction : empreinte 1d7a2af6…
Données : 2 125 vraies portes (W4, V1, V2, H1, V3, H2, V4), A(1) = −0,1356 (réel négatif, comme attendu : e^(2iθ) = −e^(−2πiS)).
| r | prédit | mesuré (Re) |
|---|---|---|
| 2 | −1,413 | −1,481 |
| 1/2 | +0,707 | +0,747 |
| 3 | −0,866 | −0,877 |
| 1/3 | +0,577 | +0,595 |
| 2/3 | −0,816 | −0,830 |
| 3/2 | −0,612 | −0,554 |
| 5 | −0,559 | −0,568 |
| 1/5 | +0,447 | +0,508 |
| 6 | +1,224 | +1,173 |
| 1/6 | +0,408 | +0,424 |
| 7 | −0,441 | −0,257 |
| 10 | +0,790 | +0,884 |
| 14 | +0,623 | +0,682 |
| 15 | +0,484 | +0,584 |
| 1/4 | +0,500 | +0,533 |
P1 ✓ : 15 signes sur 15.
P2 ✓ : écart quadratique moyen 0,070 (seuil 0,35).
P3 ✓ : dents interdites et contrôles : 4X 0,192 ; 8X 0,105 ; 9X 0,076 ; 12X 0,037 ; 18X 0,055 ; 1,37X 0,059 ; 2,71X 0,106 ; 4,4X 0,103 (tous < 0,45).
P4 ✓ : 2X (1,48) puis 6X (1,18), puis 10X et 3X.
Lecture : la loi du peigne est R(a/b) = μ(a) · Π_{p|a} √p/(p − 1) · b^(−1/2) (μ = fonction de Möbius : signe −1 par premier, 0 si facteur carré). Les dents sont aux multiples sans carré de X divisés par n'importe quel entier ; leurs hauteurs et leurs signes viennent premier par premier du développement de Jacobi-Anger (fonctions de Bessel) de la danse des portes. La structure (rapport ζ(½+it)/ζ(½−it), Möbius) est classique ; cette forme précise est probablement connue sous un autre nom (formules de type Landau-Gonek) : non vérifié à ce stade.

## Vérification dans la littérature (13/10/2026, 21h52)
- Notre mesure est une somme de χ(ρ)⁻¹·r^(iγ) sur les zéros (e^(2iθ) = 1/χ(½+iγ)).
- Connu : Σ_{γ≤T} χ(ρ) = −T/2π (Corollaire 5.1 de arXiv 2601.18025, « Generalisations of the Landau–Gonek Theorem », 2026, qui cite Gonek et Fujii) ⇒ hauteur en X ≈ −1/log(t/2π) : V2 prédit 0,118, mesuré 0,108 ; signe négatif ✓.
- Connu : les dents en X/b (b entier), de hauteur b^(−1/2) : cas X entier de Σ χ(ρ)X^ρ (Théorème 5 et Corollaire 5.2 du même article).
- Connu : le régime de ces sommes change précisément en X = T/2π et X = T/π = 2·(T/2π) (Théorème 5) : ce sont nos deux frontières (horloger X, fin du bord arrondi 2X).
- Non trouvé : les dents en a·X (a sans carré) avec le signe de Möbius μ(a) et la hauteur Π √p/(p − 1) ; l'article se limite à X ≥ 1. Peut-être ailleurs (sommes de X^(−ρ) de Gonek, Fujii) : non vérifié.
- Voisin mais distinct : Ford-Zaharescu et Ford-Soundararajan-Zaharescu (distribution de {αγ}, α fixe, arXiv 0805.2745).

## Recherche approfondie (13/10/2026, 21h56)
- Gonek 1985 / 1993 (formule de Landau uniforme) : Σ X^ρ et Σ X^(−ρ) ont pour termes principaux −(T/2π)Λ(X) et −(T/2π)Λ(X)/X : von Mangoldt, pas Möbius ; sans le facteur χ.
- arXiv 2601.18025 (2026) : Σ χ(ρ)X^ρ seulement pour X ≥ 1 (nos dents X/b) ; le cas X < 1 avec χ (nos dents a·X) n'est pas traité ; Gonek signale seulement que X^(−ρ) seul se ramène à X > 1.
- Conrey-Snaith 2007 (conjectures des rapports) : moments discrets de ζ' aux zéros ; Möbius présent seulement via 1/ζ et les mollificateurs, pas sous cette forme (texte complet de la section 7 non lu).
- Fujii 2012 (Steklov 276) : Σ ζ'(ρ)X^ρ ; résumé sans Möbius ni χ (texte complet non lu).
- Remarque : aux zéros, e^(2iθ(γ)) = −ζ'(1−ρ)/ζ'(ρ) (sous RH) ; notre peigne est donc la moyenne pondérée de ce rapport, ce qui explique l'apparition de Möbius (1/ζ' ↔ μ).
Conclusion : la loi des dents en a·X (signe μ(a), hauteur Π √p/(p − 1)) n'a été trouvée dans aucun texte accessible ; non trouvé ne veut pas dire inédit (textes complets de Gonek 1993 et Fujii 2012 non consultés). Notre dérivation (Jacobi-Anger sur le produit d'Euler) est heuristique : le produit ne converge pas sur la droite critique ; seule la mesure la confirme.
