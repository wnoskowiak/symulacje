import numpy as np
import matplotlib.pyplot as plt
import get_brown
from matplotlib.animation import FuncAnimation

def gauss(x,t,D):
    return 1/np.sqrt(4*np.pi*D*t)*np.exp((-x*x)/(4*D*t))

D=2
t=100
N=100000
  
brownian_motions=np.sqrt(2*D)*get_brown.get_brownian_motion(t,N)
trajectories=np.cumsum(brownian_motions,axis=0)
x=np.linspace(-100,100,10000)

for i in range(1,25):
    time = int((i*t)/10)
    fig=plt.figure()
    plt.xlim([-100,100])
    plt.ylim([0,0.1])
    plt.hist(trajectories[time],bins=50,alpha=0.75,density=True, color='green')
    plt.plot(x,gauss(x,time,D),color='black', linewidth=1, alpha=0.75)
    plt.show()