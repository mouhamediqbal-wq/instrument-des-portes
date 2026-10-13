import os, sys
ICI = os.path.dirname(os.path.abspath(__file__)); os.chdir(ICI)
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
rows=np.load('born4.npy',allow_pickle=True)
lab=[r[0].replace('/1','') for r in rows]; pr=np.array([r[1] for r in rows],float); me=np.array([r[2] for r in rows],float)
o=np.argsort([eval(r[0]) for r in rows]); lab=[lab[i]+'X' if '/' not in lab[i] else lab[i]+' X' for i in o]; pr=pr[o]; me=me[o]
x=np.arange(len(lab)); fig,ax=plt.subplots(figsize=(12,4.6))
ax.bar(x-0.2,pr,0.4,color='#E0A33A',label='prédit par la trigonométrie (Jacobi-Anger, premiers seuls)')
ax.bar(x+0.2,me,0.4,color='#1E4E79',label='mesuré sur 2 125 vraies portes (7 fenêtres, 200 à 2·10⁶)')
ax.axhline(0,color='#555',lw=0.8); ax.set_xticks(x); ax.set_xticklabels(lab,fontsize=9)
ax.set_ylabel('hauteur de la dent / hauteur en X'); ax.legend(frameon=False,fontsize=9,loc='lower right')
ax.set_title('Le peigne des portes : 15 dents sur 15 au bon signe, écart moyen 0,07 — les dents en 4X, 8X, 9X, 12X, 18X sont absentes comme prévu')
ax.spines[['top','right']].set_visible(False); fig.tight_layout(); fig.savefig('../figures/le peigne ordonne par la trigonometrie.png',dpi=130)
