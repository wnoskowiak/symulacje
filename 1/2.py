import numpy as np
import matplotlib.pyplot as plt
import get_brown
from matplotlib import animation

brownian_motions=get_brown.get_brownian_motion(1000,2)
trajectories=np.cumsum(brownian_motions,axis=0)
trajectories=np.transpose(trajectories)
max_y=np.max(np.abs(trajectories[1]))
max_x=np.max(np.abs(trajectories[0]))

fig = plt.figure()
ax1 = plt.axes(xlim=(-(1.05*max_x),(1.05*max_x)),ylim=(-(1.05*max_y),(1.05*max_y)))

plt.axhline(0,color='black', linewidth=1)
plt.axvline(0,color='black', linewidth=1)
plt.xlabel('x')
plt.ylabel('y')
plt.grid()

line, = ax1.plot([],[], linewidth=1, alpha=0.7)
point, = ax1.plot([],[], 'ro')
lines= [line, point]

def init():
    lines[0].set_data([0],[0])
    lines[1].set_data([0],[0])
    return lines

def animate(frame):
    data = trajectories[:,:frame].reshape(2,frame)
    lines[0].set_data(data[0],data[1])
    if len(data[0])>1:
        lines[1].set_data(data[0][-1],data[1][-1])
    return lines

anim = animation.FuncAnimation(
    fig, animate, init_func=init, frames=999, interval=0.01, blit=True
)

plt.show()