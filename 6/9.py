import numpy as np
import matplotlib.pyplot as plt

def rysuj(x,y):
    ml=np.array([[0.5, -0.5, 0.5, 0.5, 0.0, 0.0],[0.5, 0.5, -0.5, 0.5, 0.5, 0.5]])
    praw=[0.5,0.5]
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
plt.savefig("Krzywa C Levy'ego")
plt.close()