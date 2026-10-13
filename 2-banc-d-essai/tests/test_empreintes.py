"""Chaque prédiction scellée correspond toujours à son empreinte SHA-256 (rien n'a été retouché après coup)."""
import glob, hashlib, os
from _commun import PREDICTIONS

def test_toutes_les_empreintes():
    fichiers = glob.glob(os.path.join(PREDICTIONS, 'empreinte*.txt'))
    assert len(fichiers) >= 28
    for e in fichiers:
        h, nom = open(e, encoding='utf-8').read().strip().split('  ', 1)
        donnees = open(os.path.join(PREDICTIONS, nom), 'rb').read()
        assert hashlib.sha256(donnees).hexdigest() == h, nom
