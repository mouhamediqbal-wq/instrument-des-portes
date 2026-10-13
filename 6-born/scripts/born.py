import os, sys
ICI = os.path.dirname(os.path.abspath(__file__)); os.chdir(ICI)
import numpy as np
def profil(nom, K):
    if nom=='net': n=K+1; f2=np.ones(n+1); f2[n]=0; return n,f2
    if nom in('lineaire','arrondi'): n=2*K
    if nom=='ebrase': n=4*K
    if nom.startswith('optimal'):
        w=int(nom.split('_')[1])*K; n=K+w
    k=np.arange(n+1,dtype=float); f2=np.ones(n+1)
    b=k>K
    if nom=='lineaire': f2[b]=1-(k[b]-K)/K
    if nom=='arrondi': f2[b]=0.5*(1+np.cos(np.pi*(k[b]-K)/K))
    if nom=='ebrase': f2[b]=0.5*(1+np.cos(np.pi*(k[b]-K)/(3*K)))
    if nom.startswith('optimal'): f2[b]=(K-(k[b]-K)*K/w)/k[b]
    f2[n]=0; f2=np.clip(f2,0,None); return n,f2
def commutateur(n,f2):
    k=np.arange(1,n); a=np.zeros((n,n)); a[k-1,k]=np.sqrt(k*f2[k])
    q=(a+a.T)/np.sqrt(2); p=(a-a.T)/(1j*np.sqrt(2))
    return q@p-p@q
res={}
for K in (50,500,5000):
    for nom in ('net','lineaire','arrondi','ebrase','optimal_1','optimal_3'):
        n,f2=profil(nom,K)
        if n<=1200:   # verification matricielle complete
            C=commutateur(n,f2); off=np.abs(C-np.diag(np.diag(C))).max(); d=np.diag(C).imag
            # comparer a la formule diagonale
            kk=np.arange(n); g=kk*f2[:n]; dform=np.append(g[1:],0)+0  # (k+1)f(k+1)^2
            dform=np.array([(j+1)*f2[j+1] for j in range(n)])-kk*f2[:n]
            assert np.abs(d-dform).max()<1e-9, (nom,K)
        else:
            off=float('nan'); kk=np.arange(n); d=np.array([(j+1)*f2[j+1] for j in range(n)])-kk*f2[:n]
        e=d-1
        res[(nom,K)]=dict(n=n,somme=e.sum(),maxe=np.abs(e).max(),exact=np.abs(e[:K]).max(),off=off,
                          largeur=int((np.abs(e)>0.5).sum()))
        print(f"{nom:10s} K={K:5d} n={n:6d} somme e={e.sum():+.6f} (-n={-n}) max|e|={np.abs(e).max():8.4f} "
              f"K premiers max|e|={np.abs(e[:K]).max():.1e} hors-diag={off:.1e} |e|>0.5 sur {int((np.abs(e)>0.5).sum())} etats")
np.save('born_resultats.npy',res,allow_pickle=True)
