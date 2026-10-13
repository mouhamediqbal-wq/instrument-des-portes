import os, sys
ICI = os.path.dirname(os.path.abspath(__file__)); os.chdir(ICI)
import numpy as np
B=os.path.join(ICI,'..','..','2-banc-d-essai'); sys.path.insert(0,B)
from portes import theta
exec(open('theorie4.py').read().split("L=[")[0])
D=B+'/donnees/'
g=np.concatenate([np.load(D+f'vraies_portes_{w}.npy') for w in ['W4','V1','V2','H1','V3','H2','V4']])
N=len(g); E=np.exp(2j*theta(g))
def A(r): return np.mean(E*np.exp(1j*g*np.log(r)))
A1=A(1.0)
print(f"N = {N} ; A(1) = {A1:.4f} (|A1| = {abs(A1):.4f}) ; bruit attendu sur le rapport ~ {1/np.sqrt(N)/abs(A1):.3f}")
L=[(2,1),(1,2),(3,1),(1,3),(2,3),(3,2),(5,1),(1,5),(6,1),(1,6),(7,1),(10,1),(14,1),(15,1),(1,4)]
Z=[(4,1),(8,1),(9,1),(12,1),(18,1)]
rows=[];dev=[];sg=0
for a,b in L:
    pr=R(a,b).real; m=A(a/b)/A1; rows.append((f"{a}/{b}",pr,m.real,abs(m))); dev.append(m.real-pr); sg+=np.sign(m.real)==np.sign(pr)
    print(f"{a:>2}/{b:<2} predit {pr:+.3f}  mesure Re {m.real:+.3f} |.| {abs(m):.3f}")
print(f"P1 signes corrects : {sg}/15 ; P2 ecart quadratique : {np.sqrt(np.mean(np.square(dev))):.3f}")
mx=[]
for a,b in Z:
    m=A(a/b)/A1; mx.append(abs(m)); print(f"interdit {a}/{b} : |rapport| {abs(m):.3f}")
for r in (1.37,2.71,4.4):
    m=A(r)/A1; mx.append(abs(m)); print(f"controle {r} : |rapport| {abs(m):.3f}")
print(f"P3 max interdits/controles : {max(mx):.3f}")
allr=[(f'{a}/{b}',abs(A(a/b)/A1)) for a,b in L+Z]
allr.sort(key=lambda x:-x[1]); print("P4 classement :", allr[:4])
np.save('born4.npy',np.array(rows,dtype=object),allow_pickle=True)
