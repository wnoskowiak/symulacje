import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def duffing(t, xv):
    x,v = xv
    a,b,c,w,f = 1, 1, 0.2, 0.213*2*np.pi,0.2
    return [v,b*x-a*x*x*x-c*v+f*np.cos(w*t)]

a, b = 0, 40
t = np.linspace(a, b, 4000)

sol1 = solve_ivp(duffing, [a, b], [0,0.15], t_eval=t)
#sol2 = solve_ivp(lorenz, [a, b], [1,1], t_eval=t)

plt.plot(sol1.y[0], sol1.y[1])
plt.scatter(1, 0, s=50, c="b", lw=0,marker="o", label="punkty")
plt.title("f=0.2")
plt.xlabel("$x$")
plt.ylabel("$v$")
plt.savefig("duffing x(v) 1.png")
plt.close()

plt.subplot(211)
plt.title("f=0.2")
plt.plot(sol1.t, sol1.y[0])
plt.xlabel("$t$")
plt.ylabel("$x(t)$")
plt.subplot(212)
plt.plot(sol1.t, sol1.y[1])
plt.ylabel("$v(t)$")
plt.xlabel("$t$")
plt.savefig("duffing x(t) v(t) 1.png")