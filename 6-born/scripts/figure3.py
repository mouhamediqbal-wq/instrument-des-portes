import os, sys
ICI = os.path.dirname(os.path.abspath(__file__)); os.chdir(ICI)
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
d=np.load('born3.npz'); Q=30150/(2*np.pi)
fig,ax=plt.subplots(1,2,figsize=(13,4.8))
ax[0].plot(d['g'],d['C'],color='#1E4E79',lw=2,label='défaut cumulé mesuré')
ax[0].plot(d['g'],d['P'],color='#E0A33A',lw=1.3,label='danse en cosinus prédite (premiers seuls) : r = 0,982')
ax[0].set_title('T1 — la trace de l\'instrument danse en cosinus'); ax[0].set_xlabel('hauteur t'); ax[0].legend(frameon=False,fontsize=9,loc='lower left')
x=np.exp(d['lq'])/Q; m=(x>0.2)&(x<30)
ax[1].semilogx(x[m],d['Dq'][m],color='#55636E',lw=0.8)
for r,lab in [(0.5,'½'),(1,'X'),(2,'2X'),(3,'3X'),(6,'6X'),(10,'10X'),(14,'14X')]:
    i=np.argmin(abs(x-r)); ax[1].annotate(lab,(r,d['Dq'][i]),textcoords='offset points',xytext=(0,6),ha='center',fontsize=9,color='#1E4E79' if r==1 else '#B3472E')
ax[1].axvline(1,color='#1E4E79',ls=':',lw=1); ax[1].axvline(2,color='#B3472E',ls=':',lw=1)
ax[1].set_title('T2 — résonance des portes : un peigne autour de X = t/2π'); ax[1].set_xlabel('q / (t/2π)   (fenêtre 30 000–30 300)'); ax[1].set_ylabel('|moyenne de q^{iγ}| sur les portes')
for a in ax: a.spines[['top','right']].set_visible(False)
fig.tight_layout(); fig.savefig('../figures/la trace danse en cosinus et le peigne.png',dpi=130)
