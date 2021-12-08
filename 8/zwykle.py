import numpy as np
import matplotlib.pyplot as plt


def nowaczastka(x,y,R):
    theta=np.random.rand()*2*np.pi
    return int(x+R*np.sin(theta)),int(y+R*(np.cos(theta)))

def sprawdz(lattice,x,y):
    try:
        return (lattice[x-1][y]+lattice[x+1][y]+lattice[x][y-1]+lattice[x][y+1])>=1
    except:
        return 0

def odl(x,y,s1,s2):
    return ((x-s1)**2+(y-s2)**2)

def DLA(L):
    lattices=[]
    lattice=np.zeros((L,L))
    L2=L//2
    lattice[L2][L2]=1
    l=0
    i=0
    for _ in range(500):
        x,y=nowaczastka(L2,L2,l+75)
        while True:
            if (sprawdz(lattice,x,y)>=1):
                lattice[x][y]=1
                if odl(x, y, L2, L2) > l ** 2:
                    l=np.sqrt(odl(x,y,L2,L2))
                break
            if odl(x,y,L2,L2)>(l+150)*(l+150):
                break
            a,b=np.random.rand()>=1/2,np.random.rand()>=1/2
            xp,yp=x,y
            if (a):
                x,y = (x+1, y) if (b) else (x-1, y)
            else:
                x,y = (x, y+1) if (b) else (x, y-1)
            if(lattice[x][y]==1):
                x,y=xp,yp
        if(i%100==0):
            lattices.append(lattice.copy())
        i+=1
    return lattices
    
lattices=DLA(200)
for iter,lattic in enumerate(lattices):
    plt.imshow(lattic, interpolation="nearest",cmap="magma")
    plt.savefig(f"DLA {str(iter).zfill(4)}.png")