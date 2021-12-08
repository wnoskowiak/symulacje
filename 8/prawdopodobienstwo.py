import numpy as np
import matplotlib.pyplot as plt

def rand (x,y):
    a,b=np.random.rand()>=1/2,np.random.rand()>=1/2
    if (a):
        x,y = (x+1, y) if (b) else (x-1, y)
    else:
        x,y = (x, y+1) if (b) else (x, y-1)
    return x,y


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
    for _ in range(1000):
        x,y=nowaczastka(L2,L2,l+3)
        #print("olaboga")
        while True:
            #print("n")
            if odl(x,y,L2,L2)>(l+10)*(l+10):
                break
            if (sprawdz(lattice,x,y)>=1):
                att=np.random.rand()
                if (att>0.5):
                    lattice[x][y]=1
                    if odl(x, y, L2, L2) > l ** 2:
                        l=np.sqrt(odl(x,y,L2,L2))
                    break
                else:
                    nx,ny = rand (x,y)
                    while True:
                        if lattice[nx][ny]==1:
                            nx,ny = rand (x,y)
                        else:
                            break
                    x,y = nx,ny
            else:
                a,b=np.random.rand()>=1/2,np.random.rand()>=1/2
                xp,yp=x,y
                if (a):
                    x,y = (x+1, y) if (b) else (x-1, y)
                else:
                    x,y = (x, y+1) if (b) else (x, y-1)
                if(lattice[x][y]==1):
                    x,y=xp,yp
        if(i%10==0):
            lattices.append(lattice.copy())
        i+=1
    return lattices
    
print("a")
lattices=DLA(200)
for iter,lattic in enumerate(lattices):
    print(iter)
    plt.imshow(lattic, interpolation="nearest",cmap="magma")
    plt.savefig(f"DLA {str(iter).zfill(4)}.png")