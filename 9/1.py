import numpy as np
from numba import jit
import matplotlib.pyplot as plt

#T=1
L=5

@jit(nopython=True)
def sweep(lat,L,T):
    x=int(np.random.random()*L)
    y=int(np.random.random()*L)
    Delta=0
    Delta+=lat[(x+1)%L][y]
    Delta+=lat[(x-1)%L][y]
    Delta+=lat[x][(y+1)%L]
    Delta+=lat[x][(y-1)%L]
    Delta*=2
    r=np.random.random()
    lat[x][y] = 1 if (r<1/(1+np.exp(-Delta/T))) else -1
    return lat

@jit(nopython=True)
def magn(lat,L):
    suma=0
    suma=np.sum(lat)
    return suma/L/L

@jit(nopython=True)
def main(T,L):
    lat=np.ones((L,L))
    for _ in range(1000):
        lat=sweep(lat,L,T)
    magdata=np.zeros(5000)
    for i in range(5000):
        lat=sweep(lat,L,T)
        magdata[i]=magn(lat,L)
    #print(T,np.mean(np.abs(magdata)))
    return T,np.mean(np.abs(magdata))

lis=[5,4,3,2,1]
for T in lis:
    print(main(T,L))