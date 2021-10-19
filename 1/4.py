import numpy as np
import matplotlib.pyplot as plt
import get_brown
from matplotlib import animation

D=2
N=1500
t=1000

brownian_motions=np.sqrt(2*D)*get_brown.get_brownian_motion(t,N)
trajectories=np.cumsum(brownian_motions,axis=0)
trajectories=np.transpose(trajectories)

data = []

for i in range(1,int(N/10)):
    sett = trajectories[:(10*i)]
    deviation=sum(sett*sett)/(10*i)
    data.append(deviation)

y = 2*D*np.linspace(0,t-1,t)
x = np.arange(len(y))

fig = plt.figure()
ax1  = plt.axes(xlim=(0,1000), ylim=(0,4000))
const, = ax1.plot(x,y)
other, = ax1.plot(x,data[0])


title = ax1.text(0.93,.1, "", bbox={'facecolor':'w', 'alpha':0.5, 'pad':5},
                transform=ax1.transAxes, ha="center")

lines = [other, title]
def animate(frame):
    lines[0].set_data(x,data[frame])
    lines[1].set_text(str(frame*10))
    return lines

anim = animation.FuncAnimation(
    fig, animate, frames=148, interval=30
)

plt.show()
