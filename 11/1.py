import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def duffing(t, xv):
    x,v = xv
    a,b,c,w,f = 1, 1, 0.2, 0.213*2*np.pi,0.333
    return [v,b*x-a*x*x*x-c*v+f*np.cos(w*t)]

a, b = 0, 600
t = np.linspace(a, b, 60000)

sol1 = solve_ivp(duffing, [a, b], [1,0], t_eval=t)
#sol2 = solve_ivp(lorenz, [a, b], [1,1], t_eval=t)

xsol,vsol=sol1.y
plt.plot(xsol[t>200], vsol[t>200])
plt.scatter(1, 0, s=50, c="b", lw=0,marker="o", label="punkty")
plt.title("f=0.2")
plt.xlabel("$x$")
plt.ylabel("$v$")
plt.show()