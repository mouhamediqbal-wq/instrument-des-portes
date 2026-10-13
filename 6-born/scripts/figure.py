import os, sys
ICI = os.path.dirname(os.path.abspath(__file__)); os.chdir(ICI)
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
exec(open('born.py').read().split('res={}')[0])
K=500
fig,ax=plt.subplots(1,2,figsize=(13,4.6),gridspec_kw={'width_ratios':[1,2.2]})
n,f2=profil('net',K); k=np.arange(n); d=np.array([(j+1)*f2[j+1] for j in range(n)])-k*f2[:n]
ax[0].plot(k/K,d,color='#7F8C98',lw=1.5); ax[0].set_title('Coupure nette : tout le défaut dans la dernière case')
ax[0].set_xlabel('état k / K'); ax[0].set_ylabel('diagonale de qp − pq  (cible : 1)'); ax[0].axhline(1,color='#1D6B73',ls=':',lw=1)
for nom,c,lab in [('lineaire','#B3472E','linéaire (Selberg) : max 3,00'),('arrondi','#1E4E79','arrondi (notre bord) : max 3,05'),
                  ('ebrase','#2A7F62','ébrasé : max 2,11'),('optimal_3','#E0A33A','optimal largeur 3K : max 1,33')]:
    n,f2=profil(nom,K); k=np.arange(n); d=np.array([(j+1)*f2[j+1] for j in range(n)])-k*f2[:n]
    ax[1].plot(k/K,d,color=c,lw=1.8,label=lab)
ax[1].axhline(1,color='#1D6B73',ls=':',lw=1); ax[1].axhline(0,color='#999',lw=0.6)
ax[1].set_title('Bords : le défaut s\'étale et reste borné, quel que soit K'); ax[1].set_xlabel('état k / K'); ax[1].legend(frameon=False,fontsize=9)
for a in ax: a.spines[['top','right']].set_visible(False)
fig.suptitle('Born coupé : qp − pq = i·1 exact au cœur, défaut total toujours −n (théorème de la trace)',fontsize=12)
fig.tight_layout(); fig.savefig('../figures/la commutation de Born et le bord.png',dpi=130)
