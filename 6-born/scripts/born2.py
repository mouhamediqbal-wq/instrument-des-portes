import os, sys
ICI = os.path.dirname(os.path.abspath(__file__)); os.chdir(ICI)
import numpy as np, time
B=os.path.join(ICI,'..','..','2-banc-d-essai')
sys.path.insert(0,B)
import portes.instrument as I
from portes import theta
from portes.courbure import ecart_local
orig=I._poids
def poids(bord,u,ln2):
    if bord=='lineaire':
        if u<=1: return 1.0
        d=(u-1)/ln2; return 1-d if d<1 else 0.0
    return orig(bord,u,ln2)
I._poids=poids
_pc=I.phase_cavites
def phase(t,X,bord='arrondi',echos=True):
    if bord=='lineaire':
        # meme portee que l'arrondi (2X)
        t=np.asarray(t,float); LX=np.log(X); ln2=np.log(2)/LX; phi=np.zeros_like(t)
        for p in I.crible(int(2*X)):
            lp=np.log(p); m=1
            while True:
                amp=p**(-m/2)/m
                if amp<1e-9 or m*lp>np.log(2*X)+1e-9: break
                w=poids('lineaire',m*lp/LX,ln2)
                if w>0: phi+=w*amp*np.sin(-m*t*lp)
                m+=1
        return phi
    return _pc(t,X,bord,echos)
I.phase_cavites=phase
D=B+'/donnees/'
rng=np.random.default_rng(20261013)
print('A — bords')
fen={'V1':(200,1000),'V2':(30000,30300),'V3':(300000,300150)}
A={}; notesV1={}
for nom,(a,b) in fen.items():
    v=np.load(D+f'vraies_portes_{nom}.npy')
    for bord in ('arrondi','lineaire'):
        t0=time.time(); notes=I.portes_instrument(a,b,bord=bord)
        ok=len(notes)==len(v)
        if ok: e=(notes-v)/ecart_local(v)
        else: e=I.apparier(notes,v)
        A[(nom,bord)]=(len(notes),len(v),np.mean(np.abs(e)<0.1),np.abs(e).mean(),np.abs(e).max())
        if nom=='V1': notesV1[bord]=notes
        print(f"{nom} {bord:9s} portes {len(notes)}/{len(v)} justes {100*np.mean(np.abs(e)<0.1):6.2f}% moy {np.abs(e).mean():.4f} max {np.abs(e).max():.4f} ({time.time()-t0:.0f}s)")
print('B — conservation')
G=np.load(D+'portes_zeta_1004.npy')
def S(g,n0): n=np.arange(n0,n0+len(g)); return (n-0.5)-(theta(g)/np.pi+1)
def maxcum(x): return np.abs(np.cumsum(x)).max()
def temoins(x,mode):
    r=[]
    for _ in range(2000):
        y=rng.permutation(x) if mode=='melange' else x*rng.choice([-1,1],len(x))
        r.append(maxcum(y))
    return np.array(r)
S1=S(G,1); m1=maxcum(S1); T1=temoins(S1,'melange')
print(f"B1 vraies 1004 : max|cum S| = {m1:.3f} ; somme finale {S1.sum():+.3f} ; ecart-type S {S1.std():.3f} ; temoins mediane {np.median(T1):.2f}, 1er centile {np.percentile(T1,1):.2f} ; rang {np.mean(T1<=m1)*100:.2f}%")
v=np.load(D+'vraies_portes_V1.npy'); n0=int(np.searchsorted(G,v[0]))+1
assert np.allclose(G[n0-1:n0-1+len(v)],v,atol=1e-6)
gi=notesV1['arrondi']; S2=S(gi,n0); m2=maxcum(S2); T2=temoins(S2,'melange')
print(f"B2 instrument V1 (n0={n0}) : max|cum S| = {m2:.3f} ; somme {S2.sum():+.3f} ; temoins mediane {np.median(T2):.2f}, 1er centile {np.percentile(T2,1):.2f} ; rang {np.mean(T2<=m2)*100:.2f}%")
e=(gi-v)/ecart_local(v); m3=maxcum(e); T3=temoins(e,'signes')
print(f"B3 erreurs V1 : max|cum e| = {m3:.4f} ; somme {e.sum():+.4f} ; |e| moyen {np.abs(e).mean():.4f} ; temoins mediane {np.median(T3):.3f}, 5e centile {np.percentile(T3,5):.3f} ; rang {np.mean(T3<=m3)*100:.2f}%")
np.savez('born2.npz',S1=S1,S2=S2,e=e,T1=T1,T2=T2,T3=T3)
