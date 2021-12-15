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
    for _ in range(1000*L*L):
        lat=sweep(lat,L,T)
    magdata=np.zeros(5000*L*L)
    for i in range(5000*L*L):
        lat=sweep(lat,L,T)
        magdata[i]=magn(lat,L)
    return np.mean(np.abs(magdata)),np.var(magdata)*L*L/T

@jit(nopython=True)
def analityczne(T):
    if(T<(2/(np.log(1+np.sqrt(2))))):
        return (1-(1/(np.sinh(2/T))**4))**(1/8)
    return 0

ilosc=50
duzy=np.zeros((ilosc,2))
maly=np.zeros((ilosc,2))
Ttab=np.ones(ilosc)
for i in range(ilosc):
    Ttab[i]=float(i)/ilosc*4+1
    duzy[i]=main(Ttab[i],20)
    maly[i]=main(Ttab[i],10)
    print(Ttab[i])
print(duzy,maly)

duzy=np.transpose(duzy)
maly=np.transpose(maly)

plt.title('Średni moduł magnetyzacji')
plt.plot(Ttab,duzy[0],'o',label='L=20')
plt.plot(Ttab,maly[0],'o',label='L=10')
ydata=[analityczne(x) for x in Ttab]
plt.plot(Ttab,ydata,label='Analityczne')
plt.legend()
plt.grid()
plt.savefig('Magnetyzacja.png')

plt.cla()

plt.title('Średnia podatność')
plt.plot(Ttab,duzy[1],'o',label='L=20')
plt.plot(Ttab,maly[1],'o',label='L=10')
plt.legend()
plt.grid()
plt.savefig('Podatność.png')
