"""Compare l'instrument (règle d'horloger, bord arrondi) aux zéros d'une table d'Odlyzko.
Usage : python comparer_odlyzko.py <fichier_de_zeros> <a> <b>
Le fichier contient un zéro par ligne (hauteurs γ, en ordre croissant)."""
import sys, os, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '2-banc-d-essai'))
from portes import portes_instrument, apparier
f, a, b = sys.argv[1], float(sys.argv[2]), float(sys.argv[3])
g = np.loadtxt(f); g = g[(g > a) & (g < b)]
notes = portes_instrument(a, b, bord='arrondi')
d = apparier(notes, g)
print(f"fenêtre [{a} ; {b}] : {len(notes)} portes jouées / {len(g)} zéros de la table ; justes à 0,1 écart : {100*np.mean(d<0.1):.2f} % ; erreur moyenne {d.mean():.4f}")
