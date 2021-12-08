import numpy as np
import matplotlib.pyplot as plt

def rysuj(x,y):
    ml=np.array([[0.824074, 0.281482, -0.212346, 0.864198, -1.882290,-0.110607],[0.088272, 0.520988, -0.463889, -0.377778, 0.785360,8.095795]])
    praw=[0.787473,0.212527]
    cos=np.random.choice([0,1],p=praw)
    m=ml[cos]
    return [m[0]*x+m[1]*y+m[4],m[2]*x+m[3]*y+m[5]]

n=100000
a=np.empty(n)
b=np.empty(n)
a[0],b[0]=rysuj(0,0)
#print(rysuj(0,0))
for i in range(n-1):
    a[i+1],b[i+1]=rysuj(a[i],b[i])
    #print(a[i],b[i])


plt.scatter(a, b, s=3, c="b", lw=0,marker="o", label="punkty")
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.savefig("Smok Fraktalny")
plt.close()