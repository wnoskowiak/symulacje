import numpy as np
import matplotlib.pyplot as plt

def rysuj(x,y):
    ml=np.array([[0.5, 0, 0, 0.5, 0.25, np.sqrt(3.)/4],[0.5, 0, 0, 0.5, 0.0, 0],[0.5, 0, 0, 0.5, 0.5, 0]])
    praw=[1./3,1./3,1./3]
    cos=np.random.choice([0,1,2],p=praw)
    m=ml[cos]
    return [m[0]*x+m[1]*y+m[4],m[2]*x+m[3]*y+m[5]]

n=10000
a=np.empty(n)
b=np.empty(n)
a[0],b[0]=rysuj(0,0)
#print(rysuj(0,0))
for i in range(n-1):
    a[i+1],b[i+1]=rysuj(a[i],b[i])
    #print(a[i],b[i])


K=10
N=np.empty(K)
rangi=[i+1 for i in range(K)]
for r in rangi:
    H,_,_=np.histogram2d(a,b,bins=2**(r))
    N[r-1]=np.sum(H>0)

plt.scatter(rangi,np.log(N), s=12, c="b", lw=0,marker="o", label="punkty")

n=40000
a=np.empty(n)
b=np.empty(n)
a[0],b[0]=rysuj(0,0)
#print(rysuj(0,0))
for i in range(n-1):
    a[i+1],b[i+1]=rysuj(a[i],b[i])
    #print(a[i],b[i])

K=10
N=np.empty(K)
rangi=np.array([i+1 for i in range(K)])
for r in rangi:
    H,_,_=np.histogram2d(a,b,bins=2**(r))
    N[r-1]=np.sum(H>0)

plt.scatter(rangi,np.log(N), s=12, c="r", lw=0,marker="o", label="punkty")
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.savefig("Trójkąt Sierpińskiego N(r) mało")
plt.close()