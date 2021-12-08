from collections import deque
import numpy as np
import matplotlib.pyplot as plt

def neighbours(i,n):
    sasiad=[]
    if(i[0]!=n-1):
        sasiad.append((i[0]+1,i[1]))
    if(i[0]!=0):
        sasiad.append((i[0]-1,i[1]))
    if(i[1]!=n-1):
        sasiad.append((i[0],i[1]+1))
    if(i[1]!=0):
        sasiad.append((i[0],i[1]-1))
    return sasiad



def Leath(p,n):
    brzeg=0
    rozmiar=0
    lattice=np.ones((n,n))*(-1)
    tossing=np.random.random((n,n))<p
    start=(n//2,n//2)
    cluster=deque()
    cluster.append(start)
    lattice[start]=1
    while(len(cluster)>0):
        i=cluster.pop()
        if(len(neighbours(i,n))<4):
            brzeg=1
            break
        for neighbor in neighbours(i,n):
            if(lattice[neighbor]==-1):
                if(tossing[neighbor]):
                    lattice[neighbor]=1
                    cluster.append(neighbor)
                else:
                    lattice[neighbor]=0
    if(not brzeg):
        rozmiar=np.sum(lattice == 1)
    return brzeg,rozmiar

size=200
praw=[]
S=[]
P=[]
for p in range(50):
    sumaS=0
    sumaP=0
    prop=p/250+0.49
    print(prop)
    for iter in range(1000):
        Ph,Sh=Leath(prop,size)
        sumaS+=Sh
        sumaP+=Ph
    S.append(sumaS/100)
    P.append(sumaP/100)
    praw.append(prop)
plt.title(f"Perkolacja zmienne prawdopodobienstwo size = {size}x{size} rozmiar")
plt.plot(praw,(S),'o')
plt.grid()
plt.savefig(f"Perkolacja zmienne prawdopodobienstwo size = {size}x{size} rozmiar.png")
plt.cla()
plt.title(f"Perkolacja zmienne prawdopodobienstwo size = {size}x{size} brzeg")
plt.plot(praw,(P),'o')
plt.grid()
plt.savefig(f"Perkolacja zmienne prawdopodobienstwo size = {size}x{size} brzeg.png")
#plt.show()