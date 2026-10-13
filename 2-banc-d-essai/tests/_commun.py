import os, sys, numpy as np
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(ICI)
sys.path.insert(0, RACINE)
DONNEES = os.path.join(RACINE, 'donnees')
PREDICTIONS = os.path.join(RACINE, 'predictions')
def charger(nom): return np.load(os.path.join(DONNEES, nom))
def lent(f): f.lent = True; return f
