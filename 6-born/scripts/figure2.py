import os, sys
ICI = os.path.dirname(os.path.abspath(__file__)); os.chdir(ICI)
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
d=np.load('born2.npz'); rng=np.random.default_rng(7)
fig,ax=plt.subplots(1,2,figsize=(13,4.6))
for i in range(12):
    ax[0].plot(np.cumsum(rng.permutation(d['S1'])),color='#B9C2CA',lw=0.8)
ax[0].plot(np.cumsum(d['S1']),color='#1E4E79',lw=2.2,label='vraies portes : max 0,58')
ax[0].plot([],[],color='#B9C2CA',label='mêmes danses mélangées : max typique 6,6')
ax[0].set_title('Défaut cumulé des 1 004 premières portes  Σ S_n'); ax[0].set_xlabel('porte n'); ax[0].legend(frameon=False,fontsize=9)
for i in range(12):
    ax[1].plot(np.cumsum(d['e']*rng.choice([-1,1],len(d['e']))),color='#B9C2CA',lw=0.8)
ax[1].plot(np.cumsum(d['e']),color='#2A7F62',lw=2.2,label='erreurs de l\'instrument : max 0,18')
ax[1].plot([],[],color='#B9C2CA',label='signes tirés au hasard : max typique 0,86')
ax[1].set_title('Erreurs cumulées de l\'instrument (fenêtre 200–1 000)'); ax[1].set_xlabel('porte de la fenêtre'); ax[1].legend(frameon=False,fontsize=9)
for a in ax: a.spines[['top','right']].set_visible(False); a.axhline(0,color='#999',lw=0.6)
fig.suptitle('Comme chez Born, le défaut total est conservé : il se déplace, il ne s\'accumule pas',fontsize=12)
fig.tight_layout(); fig.savefig('../figures/la conservation du defaut.png',dpi=130)
