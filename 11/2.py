import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def duffing(t, xv):
    x,v = xv
    a,b,c,w,f = 1, 1, 0.2, 0.213*2*np.pi,0.2
    return [v,b*x-a*x*x*x-c*v+f*np.cos(w*t)]

a, b = 0, 40
t = np.linspace(a, b, 10000)

sol1 = solve_ivp(duffing, [a, b], [0,0.15], t_eval=t)

plt.plot(sol1.y[0],sol1.y[1])
plt.show()
plt.plot(sol1.t,sol1.y[0])
plt.show()
plt.plot(sol1.t,sol1.y[1])
plt.show()

res = [0.2,0.2925]