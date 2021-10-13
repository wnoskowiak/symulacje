import numpy as np
import matplotlib.pyplot as plt
import get_brown

brownian_motions=get_brown.get_brownian_motion(1000,2)
trajectories=np.cumsum(brownian_motions,axis=0)
trajectories=np.transpose(trajectories)
plt.plot(trajectories[0],trajectories[1], linewidth=1, alpha=0.7)
plt.axhline(0,color='black', linewidth=1)
plt.axvline(0,color='black', linewidth=1)
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()