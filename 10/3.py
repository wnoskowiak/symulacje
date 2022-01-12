import numpy as np
from numba import jit
import matplotlib.pyplot as plt
from scipy import special

@jit(nopython=True)
def sweep(lat,L,T):
    for _ in range(L*L):
        x=int(np.random.random()*L)
        y=int(np.random.random()*L)
        c=np.random.random()
        d=np.random.random()
        if c>1/2:
            if d>1/2:
                a=1
                b=0
            else:
                a=-1
                b=0
        else:
            if d>1/2:
                a=0
                b=1
            else:
                a=0
                b=-1
        a=(x+a+L)%L
        b=(y+b+L)%L
        if(lat[a][b]!=lat[x][y]):
            Delta=0
            Delta+=lat[(x+1)%L][y]
            Delta+=lat[(x-1)%L][y]
            Delta+=lat[x][(y+1)%L]
            Delta+=lat[x][(y-1)%L]
            Delta-=lat[a][b]
            Delta*=lat[x][y]
            Delta2=0
            Delta2+=lat[(a+1)%L][b]
            Delta2+=lat[(a-1)%L][b]
            Delta2+=lat[a][(b+1)%L]
            Delta2+=lat[a][(b-1)%L]
            Delta2-=lat[x][y]
            Delta2*=lat[a][b]
            Delta3=Delta+Delta2
            Delta3*=2
            if Delta3<=0:
                lat[x][y]*=-1
                lat[a][b]*=-1
            else:
                r=np.random.random()
                if np.exp(-Delta3/T)>r:
                    lat[x][y]*=-1
                    lat[a][b]*=-1
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
L=200
rozmiary=[]
Tdata=[]
lat=np.random.choice([-1,1],size=(L,L))
for i in range(1000001):
    lat=sweep(lat,L,T)
    if(i==1000):
        Tdata.append(i)
        rozmiary.append(rozmiar(lat,L))
    if(i==2000):
        Tdata.append(i)
        rozmiary.append(rozmiar(lat,L))
    if(i==5000):
        Tdata.append(i)
        rozmiary.append(rozmiar(lat,L))
    if(i==10000):
        Tdata.append(i)
        rozmiary.append(rozmiar(lat,L))
    if(i==20000):
        Tdata.append(i)
        rozmiary.append(rozmiar(lat,L))
    if(i==50000):
        Tdata.append(i)
        rozmiary.append(rozmiar(lat,L))
    if(i==100000):
        Tdata.append(i)
        rozmiary.append(rozmiar(lat,L))
    if(i==200000):
        Tdata.append(i)
        rozmiary.append(rozmiar(lat,L))
    if(i==500000):
        Tdata.append(i)
        rozmiary.append(rozmiar(lat,L))
    if(i==1000000):
        Tdata.append(i)
        rozmiary.append(rozmiar(lat,L))
    if i ==10:
        plt.cla()
        plt.imshow(lat, interpolation="nearest",cmap="magma")
        plt.title(f"Agorytm Metropolis {i} króków")
        plt.savefig(f"MC {i}.png")
    if i ==100:
        plt.cla()
        plt.imshow(lat, interpolation="nearest",cmap="magma")
        plt.title(f"Agorytm Metropolis {i} króków")
        plt.savefig(f"MC {i}.png")
    if i ==1000:
        plt.cla()
        plt.imshow(lat, interpolation="nearest",cmap="magma")
        plt.title(f"Agorytm Metropolis {i} króków")
        plt.savefig(f"MC {i}.png")
    if i ==5000:
        plt.cla()
        plt.imshow(lat, interpolation="nearest",cmap="magma")
        plt.title(f"Agorytm Metropolis {i} króków")
        plt.savefig(f"MC {i}.png")
    if i ==10000:
        plt.cla()
        plt.imshow(lat, interpolation="nearest",cmap="magma")
        plt.title(f"Agorytm Metropolis {i} króków")
        plt.savefig(f"MC {i}.png")
    if i ==20000:
        plt.cla()
        plt.imshow(lat, interpolation="nearest",cmap="magma")
        plt.title(f"Agorytm Metropolis {i} króków")
        plt.savefig(f"MC {i}.png")
    if i ==50000:
        plt.cla()
        plt.imshow(lat, interpolation="nearest",cmap="magma")
        plt.title(f"Agorytm Metropolis {i} króków")
        plt.savefig(f"MC {i}.png")
    if i ==100000:
        plt.cla()
        plt.imshow(lat, interpolation="nearest",cmap="magma")
        plt.title(f"Agorytm Metropolis {i} króków")
        plt.savefig(f"MC {i}.png")
    if i ==200000:
        plt.cla()
        plt.imshow(lat, interpolation="nearest",cmap="magma")
        plt.title(f"Agorytm Metropolis {i} króków")
        plt.savefig(f"MC {i}.png")
    if i ==500000:
        plt.cla()
        plt.imshow(lat, interpolation="nearest",cmap="magma")
        plt.title(f"Agorytm Metropolis {i} króków")
        plt.savefig(f"MC {i}.png")
    if i ==1000000:
        plt.cla()
        plt.imshow(lat, interpolation="nearest",cmap="magma")
        plt.title(f"Agorytm Metropolis {i} króków")
        plt.savefig(f"MC {i}.png")
plt.clf()
plt.cla()
plt.yscale("log")
plt.xscale("log")
ydata=np.cbrt(Tdata)*rozmiary[0]/np.cbrt(1000)
plt.plot(Tdata,rozmiary,'o')
plt.plot(Tdata,ydata)
plt.savefig(f"Wykres rozmiarówASAD.png")

'''lat=np.random.choice([-1,1],size=(L,L))
for i in range(50001):
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
    if i ==10000:
        plt.imshow(lat, interpolation="nearest",cmap="magma")
        plt.title(f"Agorytm Metropolis {i} króków")
        plt.savefig(f"MC {i}.png")
    if i ==20000:
        plt.imshow(lat, interpolation="nearest",cmap="magma")
        plt.title(f"Agorytm Metropolis {i} króków")
        plt.savefig(f"MC {i}.png")
    if i ==50000:
        plt.imshow(lat, interpolation="nearest",cmap="magma")
        plt.title(f"Agorytm Metropolis {i} króków")
        plt.savefig(f"MC {i}.png")'''