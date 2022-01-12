import numpy as np
from numba import jit
import matplotlib.pyplot as plt
from scipy import special

@jit(nopython=True)
def sweep(lat,L,T):
    for _ in range(L*L):
        x=int(np.random.random()*L)
        y=int(np.random.random()*L)
        Delta=0
        Delta+=lat[(x+1)%L][y]
        Delta+=lat[(x-1)%L][y]
        Delta+=lat[x][(y+1)%L]
        Delta+=lat[x][(y-1)%L]
        Delta*=2*lat[x][y]
        if Delta<=0:
            lat[x][y]*=-1
        else:
            r=np.random.random()
            if np.exp(Delta/T)<r:
                lat[x][y]*=-1
    return lat

@jit(nopython=True)
def Chi(lat,L,r):
    suma=0
    for w in range(L):
        sum=0
        for r0 in range(L):
            sum+=lat[w][r0]*lat[w][(r0+r)%L]
        suma+=sum/L
    return suma/L

@jit(nopython=True)
def rozmiar(lat,L):
    C=0 
    rmax=0
    for r in range(L):
        help=Chi(lat,L,r)
        if help<np.exp(-1):
            rmax=r
            break
        C-=np.log(help)
    return rmax*(rmax+1)/2/C

T=2
L=500
rozmiary=[]
Tdata=[]
lat=np.random.choice([-1,1],size=(L,L))
for i in range(5001):
    lat=sweep(lat,L,T)
    if(i==10):
        Tdata.append(i)
        rozmiary.append(rozmiar(lat,L))
    if(i==20):
        Tdata.append(i)
        rozmiary.append(rozmiar(lat,L))
    if(i==50):
        Tdata.append(i)
        rozmiary.append(rozmiar(lat,L))
    if(i==100):
        Tdata.append(i)
        rozmiary.append(rozmiar(lat,L))
    if(i==200):
        Tdata.append(i)
        rozmiary.append(rozmiar(lat,L))
    if(i==500):
        Tdata.append(i)
        rozmiary.append(rozmiar(lat,L))
    if(i==1000):
        Tdata.append(i)
        rozmiary.append(rozmiar(lat,L))
    if(i==2000):
        Tdata.append(i)
        rozmiary.append(rozmiar(lat,L))
    if(i==5000):
        Tdata.append(i)
        rozmiary.append(rozmiar(lat,L))
    print(i)

plt.yscale("log")
plt.xscale("log")
ydata=np.sqrt(Tdata)*rozmiary[0]/np.sqrt(10)
plt.plot(Tdata,rozmiary,'o')
plt.plot(Tdata,ydata)
plt.savefig(f"Wykres rozmiarów.png")

