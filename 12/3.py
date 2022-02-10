import numpy as np
from random import randint
import queue
import matplotlib.pyplot as plt
from numpy.lib import histogram
import scipy.optimize as scp

que = queue.Queue()
n = 31
lat = np.zeros((n, n),int)
iter = 5000
sizes = []

def f(x,a):
    return a/x

for i in range(iter):
    nx, ny = randint(0,n-1), randint(0,n-1)
    lat[nx][ny] += 1
    if lat[nx][ny] == 4:
        que.put((nx, ny))
    av = 0
    while not que.empty():
        (lx, ly) = que.get()
        try:
            if lat[lx][ly] >= 3:
                av += 1
                lat[lx][ly] = 0
                que.put((lx+1, ly))
                que.put((lx-1, ly))
                que.put((lx, ly+1))
                que.put((lx, ly-1))
            else:
                lat[lx][ly] += 1
        except:
            pass
    if av > 0:
        sizes.append(av)

print(sizes)
hist,bins = np.histogram(sizes,bins = np.max(sizes),density=False)
pop,cov=scp.curve_fit(f,bins[0:-1],hist)
space = np.arange(1, np.max(sizes), 0.1)
plt.plot(space,f(space, *pop))
plt.plot(bins[0:-1],hist)
plt.xscale('log')
plt.yscale('log')
plt.show()

    