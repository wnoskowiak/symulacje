import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def duffing(t, xv):
    x,v = xv
    a,b,c,w,f = 1, 1, 0.07, 0.213*2*np.pi, 0.29
    return [v,b*x-a*x*x*x-c*v+f*np.cos(w*t)]

a, b = 0, 40000
t = np.linspace(a, b, 4000000)

sol1 = solve_ivp(duffing, [a, b], [1,0], t_eval=t)
#sol2 = solve_ivp(lorenz, [a, b], [1,1], t_eval=t)

xh=[]
vh=[]
xsol,vsol=sol1.y
n=0
for time in sol1.t:
    if(abs(time-n/0.213)<40000./4000000):
        n+=1
        ia=int(time*4000000/40000)-1
        xh.append(xsol[ia])
        vh.append(vsol[ia])
plt.scatter(xh, vh, s=3, c="b", lw=0,marker="o", label="punkty")

plt.show()