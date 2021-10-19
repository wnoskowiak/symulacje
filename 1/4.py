import numpy as np
import matplotlib.pyplot as plt
import get_brown
from matplotlib import animation

D=2
N=100
t=1000

fig = plt.plot()
x=2*D*np.linspace(0,t-1,t)
ax1,  = plt.plot(x)

def animate(frame):
    brownian_motions=np.sqrt(2*D)*get_brown.get_brownian_motion(t,frame)
    trajectories=np.cumsum(brownian_motions,axis=0)
    trajectories=np.transpose(trajectories)
    deviation=sum(trajectories*trajectories)/frame
    plt.plot(deviation)

anim = animation.FuncAnimation(
    fig, animate, frames=99, interval=0.01
)

plt.show()