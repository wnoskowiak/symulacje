import numpy as np
import matplotlib.pyplot as plt
import get_brown

D=2
N=700
t=1000

brownian_motions=np.sqrt(2*D)*get_brown.get_brownian_motion(t,N)
trajectories=np.cumsum(brownian_motions,axis=0)
trajectories=np.transpose(trajectories)
deviation=sum(trajectories*trajectories)/N
x=2*D*np.linspace(0,t-1,t)
plt.plot(deviation)
plt.plot(x)
plt.show()