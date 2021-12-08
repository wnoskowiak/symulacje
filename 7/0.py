from collections import deque
import os
import numpy as np
import matplotlib.pyplot as plt

my_path = os.path.abspath(__file__)
results_dir = os.path.join(my_path, 'Animowane\\')

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
    lattice=np.ones((n,n))*(-1)
    lattices=[]
    tossing=np.random.random((n,n))<p
    start=(n//2,n//2)
    cluster=deque()
    cluster.append(start)
    lattice[start]=1
    while(len(cluster)>0):
        i=cluster.pop()
        for neighbor in neighbours(i,n):
            if(lattice[neighbor]==-1):
                if(tossing[neighbor]):
                    lattice[neighbor]=1
                    cluster.append(neighbor)
                else:
                    lattice[neighbor]=0
        lattices.append(lattice.copy())
    return lattices

prop=0.59
size=100
lattices=Leath(prop,size)
print(len(lattices))
iter=0
for lattic in lattices:
    if(iter%100==0):
        a = plt.title(f"Perkolacja p = {prop} size = {size}x{size} {iter}")
        name = f"{a.get_text()}.png"
        plt.imshow(lattic, interpolation="nearest",cmap="magma")
        plt.grid()
        plt.savefig(results_dir,name)
    iter+=1
    #plt.show()