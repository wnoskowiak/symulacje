import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

Du,Dv,k = 2e-5,1e-5,0.062    

N=100

resu = []
resv = []

Fs=[0,0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09,0.1]
for F in Fs:
    u = np.ones((N,N))
    v = np.zeros((N,N))
    for i in range(N//4,3*N//4):
        for j in range(N//4,3*N//4):
            u[i, j] = np.random.rand()*0.2+0.4
            v[i, j] = np.random.rand()*0.2+0.2
    du=np.zeros((N,N))
    dv=np.zeros((N,N))
    Laplacev=np.zeros((N,N))
    Laplaceu=np.zeros((N,N))
    for t in range(5001):
        ul=np.roll(u,-1,axis=0)
        up=np.roll(u,1,axis=0)
        vl=np.roll(v,-1,axis=0)
        vp=np.roll(v,1,axis=0)
        ul2=np.roll(u,-1,axis=1)
        up2=np.roll(u,1,axis=1)
        vl2=np.roll(v,-1,axis=1)
        vp2=np.roll(v,1,axis=1)
        #print(ul,up,u)
        Laplaceu=(ul+up+ul2+up2-4*u)/0.02/0.02
        #print(Laplaceu)
        Laplacev=(vl+vp+vl2+vp2-4*v)/0.02/0.02
        du=Du*Laplaceu-u*v*v+F-F*u
        dv=Dv*Laplacev+u*v*v-(F+k)*v
        u=u+du
        v=v+dv
    resu.append(u)
    resv.append(v)

resu = np.concatenate(np.array(resu))
plt.imshow(resu,interpolation="nearest",cmap="magma")
plt.savefig(f"uuuu {format(F, '.5f')}.png")
plt.cla()
"""
plt.imshow(v,interpolation="nearest",cmap="magma")
plt.savefig(f"vvvv {format(F, '.5f')}.png")
plt.cla()
"""