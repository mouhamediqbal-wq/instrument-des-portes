import os, sys
ICI = os.path.dirname(os.path.abspath(__file__)); os.chdir(ICI)
# Prediction theorique (sans donnees) : coefficients de Fourier de e^{-2 pi i S} via Jacobi-Anger, premier par premier
import numpy as np
def premiers(n):
    return [k for k in range(2,n) if all(k%d for d in range(2,int(k**0.5)+1))]
def factorint(n):
    f={};d=2
    while d*d<=n:
        while n%d==0: f[d]=f.get(d,0)+1; n//=d
        d+=1
    if n>1: f[n]=f.get(n,0)+1
    return f
P=premiers(200); M=8
phi=np.linspace(0,2*np.pi,4096,endpoint=False)
c={}
for p in P:
    f=np.ones_like(phi,dtype=complex)
    for m in range(1,M+1):
        z=2/(m*p**(m/2)); f*=np.exp(1j*z*np.sin(m*phi))
    c[p]=np.fft.fft(f)/len(phi)   # c[p][j] = coefficient de e^{i j phi}
def R(num,den):
    # r = num/den ; composante e^{-i t ln r} : j_p = -(exposant de p dans r)
    e={}
    for q,k in factorint(num).items(): e[q]=e.get(q,0)+k
    for q,k in factorint(den).items(): e[q]=e.get(q,0)-k
    val=1+0j
    for q,k in e.items():
        val*=c[q][(-k)%4096]/c[q][0]
    return val
L=[(1,1),(2,1),(1,2),(3,1),(1,3),(2,3),(3,2),(4,1),(1,4),(5,1),(1,5),(6,1),(1,6),(7,1),(1,7),(10,1),(1,10),(14,1),(15,1),(9,1),(8,1),(12,1),(5,2),(5,3)]
for a,b in L: print(f"{a}/{b}", f"{abs(R(a,b)):.3f}")
