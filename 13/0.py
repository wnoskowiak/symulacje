import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

Du,Dv,F,k = 2e-5,1e-5,0.025,0.055

N=100

u = np.ones(N)
v = np.zeros(N)
xs = np.arange(N)
for i in range(N//4,3*N//4):
    u[i] = np.random.rand()*0.2+0.4
    v[i] = np.random.rand()*0.2+0.2
du=np.zeros(N)
dv=np.zeros(N)
Laplacev=np.zeros(N)
Laplaceu=np.zeros(N)

czasu=np.zeros((100,100))
czasv=np.zeros((100,100))

for t in range(10001 - 2):
    if t in [0, 100, 10000]:
        plt.plot(u)
        plt.plot(v)
        plt.savefig(f"obrazek {t}.png")
        plt.cla()
    ul=np.roll(u,-1)
    up=np.roll(u,1)
    vl=np.roll(v,-1)
    vp=np.roll(v,1)
    #print(ul,up,u)
    Lu=(ul+up-2*u)/0.02/0.02
    #Lu = np.diff(u,n=2, append = u[:2])/0.02/0.02
    #Lv = np.diff(v,n=2, append = v[:2])/0.02/0.02
    #print(Laplaceu)
    Lv=(vl+vp-2*v)/0.02/0.02
    #print(Lv-lv)
    du=Du*Lu-u*v*v+F-F*u
    dv=Dv*Lv+u*v*v-(F+k)*v
    u=u+du
    v=v+dv
    if(t%100==0):
        czasu[t//100]=np.copy(u)
        czasv[t//100]=np.copy(v)



plt.imshow(czasu,interpolation="nearest",cmap="magma")
plt.savefig('uuuu.png')
plt.cla()
plt.imshow(czasv,interpolation="nearest",cmap="magma")
plt.savefig('vvvv.png')