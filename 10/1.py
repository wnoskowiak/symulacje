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

T=2
L=500

lat=np.random.choice([-1,1],size=(L,L))
for i in range(5001):
    lat=sweep(lat,L,T)
    if i ==10:
        plt.imshow(lat, interpolation="nearest",cmap="magma")
        plt.title(f"Agorytm Metropolis {i} króków")
        plt.savefig(f"MC {i}.png")
    if i ==100:
        plt.imshow(lat, interpolation="nearest",cmap="magma")
        plt.title(f"Agorytm Metropolis {i} króków")
        plt.savefig(f"MC {i}.png")
    if i ==1000:
        plt.imshow(lat, interpolation="nearest",cmap="magma")
        plt.title(f"Agorytm Metropolis {i} króków")
        plt.savefig(f"MC {i}.png")
    if i ==5000:
        plt.imshow(lat, interpolation="nearest",cmap="magma")
        plt.title(f"Agorytm Metropolis {i} króków")
        plt.savefig(f"MC {i}.png")
