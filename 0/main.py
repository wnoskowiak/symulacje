import scipy as sp
import numpy as np 
import matplotlib.pyplot as plt

x = np.arange(0,10,0.001)
y = np.sin(x)

graph = plt.plot(x,y)
plt.savefig('wykres.png')
plt.show()