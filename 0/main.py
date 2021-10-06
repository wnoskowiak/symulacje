import scipy as sp
import numpy as np 
import matplotlib.pyplot as plt

x = np.arange(0,10,0.001)
y1 = np.sin(x)
y2 = np.cos(x)


plt.plot(x,y1, color='r', linestyle=':')
plt.plot(x,y2, color='g', linestyle='-')
plt.title('wykres')
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('wykres.png')
plt.show()