"""L'instrument des portes : jouer les zéros de Riemann avec les nombres premiers, et l'inverse.
Voir 1-specification/SPECIFICATION.md (les numéros de section sont cités dans chaque module)."""
from .courbure import theta, ecart_local
from .premiers import crible, von_mangoldt
from .riemann_siegel import Z, portes_riemann_siegel
from .instrument import phase_cavites, portes_instrument, apparier
from .spectrometre import reponse, lire_premiers
from .planck import cases_de_planck, ajuster_h
__version__ = "0.1"
