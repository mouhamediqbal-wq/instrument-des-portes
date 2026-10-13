# A1 — Assemblage préenregistré (13/10/2026, 10h40, Paris) — écrit AVANT tout calcul à 30 premiers et avant ré-analyse
Instrument assemblé = enveloppe de Riemann-von Mangoldt + fluctuation du graphe des premiers (carrefour optimisé, poids exacts 1/√p, composés pq éteints, flux).
Règle (fixée sans regarder les zéros) :
- N_s(E) = (E/2π)(ln(E/2π) − 1) + 7/8 ; domaine de validité : E ≥ 2π (au-delà de son minimum ; la note parasite d'hier venait de E < 2π, où N_s remonte vers 7/8).
- S_g(E) = N_g(E) − (Σ ln p)·E/π − c, où c = moyenne de N_g(k) − (Σ ln p)k/π sur tout le spectre calculé du graphe (k de 0 à k_max) : constante prise sur le graphe seul.
- Notes assemblées : Eₙ = plus petit E ≥ 2π tel que N_s(E) + S_g(E) ≥ n − ½.
Jeux : 6 premiers (≤ 13), 15 premiers (≤ 47), 30 premiers (≤ 113) — 50 premiers abandonnés d'avance (optimisation 100×100 trop lente sans dérivée automatique).
Mesure : écart moyen |Eₙ − γₙ| sur les 40 premières notes ; témoin : l'enveloppe seule (S_g = 0), même règle.
Critère A1 (réussite si TOUT est vrai) : écart(6) > écart(15) > écart(30) ET écart(30) < écart(enveloppe).
Prédiction de Claude : réussite, avec écart(6) au-dessus du témoin et écart(15), écart(30) en dessous.
