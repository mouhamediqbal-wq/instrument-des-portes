import os, sys
ICI = os.path.dirname(os.path.abspath(__file__)); os.chdir(ICI)
import numpy as np
B=os.path.join(ICI,'..','..','2-banc-d-essai'); sys.path.insert(0,B)
import portes.instrument as I
from portes import theta
D=B+'/donnees/'
a,b=200,1000; X=(a+b)/2/(2*np.pi)
g=I.portes_instrument(a,b,bord='arrondi'); G=np.load(D+'portes_zeta_1004.npy'); v=np.load(D+'vraies_portes_V1.npy')
n0=int(np.searchsorted(G,v[0]))+1; n=np.arange(n0,n0+len(g))
S=(n-0.5)-(theta(g)/np.pi+1); Phi=I.phase_cavites(g,X,'arrondi')
dev=S-Phi/np.pi; c=np.round(dev.mean())
print(f"P0 : c = {c:.0f}, ecart max |S - Phi/pi - c| = {np.abs(dev-c).max():.2e}")
# termes
LX=np.log(X); ln2=np.log(2)/LX; T=[]
for p in I.crible(int(2*X)):
    lp=np.log(p); m=1
    while True:
        amp=p**(-m/2)/m
        if amp<1e-9 or m*lp>np.log(2*X)+1e-9: break
        w=I._poids('arrondi',m*lp/LX,ln2)
        if w>0: T.append((p,m,w,amp,m*lp))
        m+=1
rho=np.log(g/(2*np.pi))/(2*np.pi)
def cosdanse(sel=None):
    s=np.zeros_like(g)
    for (p,m,w,amp,om) in T:
        if sel and not sel(p,m): continue
        s+=w*amp*rho*np.cos(om*g)/om
    return s/np.pi
C=np.cumsum(S-c)
P=cosdanse()+Phi**2/(2*np.pi**2)+0.5*(S-c)
P=P+np.mean(C-P)
r=np.corrcoef(C,P)[0,1]; res=np.sqrt(np.mean((C-P)**2))/np.std(C)
print(f"P1 : correlation C/P = {r:.4f} ; residu quadratique = {100*res:.1f} % de l'ecart-type de C")
P2=cosdanse(lambda p,m: p==2 and m==1); 
A=np.vstack([P2,np.ones_like(P2)]).T; coef=np.linalg.lstsq(A,C,rcond=None)[0]
r2=np.corrcoef(C,P2)[0,1]**2
print(f"P2 : terme p=2 seul : variance expliquee {100*r2:.1f} % (coefficient ajuste {coef[0]:.3f}, attendu 1)")
# T2
v2=np.load(D+'vraies_portes_V2.npy'); t0=30150
G2=np.load(D+'portes_zeta_1004.npy')
lq=np.arange(np.log(2),np.log(1e8),0.001)
Dq=np.array([abs(np.mean(np.exp(1j*v2*L))) for L in lq])
k=Dq.argmax(); q=np.exp(lq[k])
# S_n pour V2 : numerotation via N lisse arrondi
N0=np.round(theta(v2[0])/np.pi+1+0.5)  # indice approx de la premiere porte
nn=np.arange(len(v2)); Sv=(N0+nn-0.5)-(theta(v2)/np.pi+1); Sv-=np.round(Sv.mean())
car=abs(np.mean(np.exp(-2j*np.pi*Sv)))
print(f"P3 : max D = {Dq[k]:.3f} en q = {q:.0f} (t0/2pi = {t0/(2*np.pi):.0f}, ecart {100*(q/(t0/(2*np.pi))-1):+.2f} %)")
print(f"P4 : |moyenne e^(-2 pi i S_n)| = {car:.3f} (S_n : moyenne {Sv.mean():+.3f}, ecart-type {Sv.std():.3f})")
Q=t0/(2*np.pi); hors=(np.exp(lq)<0.9*Q)|(np.exp(lq)>1.1*Q)
zone2=(np.exp(lq)>0.95*Q**2)&(np.exp(lq)<1.05*Q**2)
print(f"P5 : mediane hors zone = {np.median(Dq[hors]):.3f} ; max autour de (t0/2pi)^2 = {Dq[zone2].max():.3f} ; 5 plus hauts pics hors zone :",
      ', '.join(f"{np.exp(lq[i]):.0f}:{Dq[i]:.3f}" for i in np.argsort(-np.where(hors,Dq,0))[:5]))
np.savez('born3.npz',C=C,P=P,P2=P2,g=g,lq=lq,Dq=Dq,S=S,Phi=Phi)
