import numpy as np
import matplotlib.pyplot as plt

def rysuj(x,y):
    ml=np.array([[0.001, 0.0, 0.0, 0.16, 0.0, 0.0],[-0.15, 0.28, 0.26, 0.24, 0.0, 0.44],[ 0.2,-0.26, 0.23, 0.22, 0.0, 1.6],[ 0.85, 0.04,-0.04, 0.85, 0.0, 1.6]])
    praw=[0.03,0.11,0.13,0.73]
    cos=np.random.choice([0,1,2,3],p=praw)
    m=ml[cos]
    return [m[0]*x+m[1]*y+m[4],m[2]*x+m[3]*y+m[5]]

n=100
a=np.empty(n)
b=np.empty(n)
a[0],b[0]=rysuj(0,0)
#print(rysuj(0,0))
for i in range(n-1):
    a[i+1],b[i+1]=rysuj(a[i],b[i])
    #print(a[i],b[i])


K=14
N=np.empty(K)
rangi=[i+1 for i in range(K)]
for r in rangi:
    H,_,_=np.histogram2d(a,b,bins=2**(r))
    N[r-1]=np.sum(H>0)

plt.scatter(rangi,np.log(N), s=3, c="b", lw=0,marker="o", label="punkty")
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.savefig("Paprotka Barnsley N(r) malo")
plt.close()