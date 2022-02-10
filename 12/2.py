import numpy as np
from random import randint
import queue
import matplotlib.pyplot as plt

que = queue.Queue()
n = 31
lat = np.zeros((n, n),int)
iter = 3000
sizes = []

for i in range(iter):
    nx, ny = n//2, n//2
    lat[nx][ny] += 1
    if lat[nx][ny] == 4:
        que.put((nx, ny))
        sizes.append(np.sum(lat))
    while not que.empty():
        (lx, ly) = que.get()
        try:
            if lat[lx][ly] >= 3:
                lat[lx][ly] = 0
                que.put((lx+1, ly))
                que.put((lx-1, ly))
                que.put((lx, ly+1))
                que.put((lx, ly-1))
            else:
                lat[lx][ly] += 1
        except:
            pass
    if i%100 == 0 :
        plt.imshow(lat,interpolation='nearest')
        plt.savefig(str(i))

    