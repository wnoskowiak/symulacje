import numpy as np
import matplotlib.pyplot as plt
import get_brown
from matplotlib import animation

def gauss(x,t,D):
    return 1/np.sqrt(4*np.pi*D*t)*np.exp((-x*x)/(4*D*t))

D=2
t=100
N=100000
  
brownian_motions=np.sqrt(2*D)*get_brown.get_brownian_motion(t,N)
trajectories=np.cumsum(brownian_motions,axis=0)
x=np.linspace(-100,100,10000)

fig = plt.figure()
ax1 = plt.axes(ylim=[0,0.1])
plt.axvline(0,color='black', linewidth=1, alpha=0.75)
hist = ax1.hist([],bins=50,alpha=0.75,density=True, color='green', animated=True)
title = ax1.text(0.93,.9, "", bbox={'facecolor':'w', 'alpha':0.5, 'pad':5},
                transform=ax1.transAxes, ha="center")
gss, = ax1.plot([],[],color='black', linewidth=1, alpha=0.75)

lines = [hist[-1], gss]

def init():
    temp1 = ax1.hist(trajectories[0],bins=50,alpha=0.75,density=True, color='green')[-1]
    lines[1].set_data(x,gauss(x,0,D))
    title.set_text("0")
    return [lines[1],*temp1, title]

def animate(frame):
    temp1 = ax1.hist(trajectories[frame],bins=50,alpha=0.75,density=True, color='green')[-1]
    lines[1].set_data(x,gauss(x,frame,D))
    title.set_text(str(frame))
    return [lines[1],*temp1, title]


"""
for i in range(1,25):
    time = int((i*t)/10)
    fig=plt.figure()
    plt.xlim([-100,100])
    plt.ylim([0,0.1])
    plt.hist(trajectories[time],bins=50,alpha=0.75,density=True, color='green')
    plt.plot(x,gauss(x,time,D),color='black', linewidth=1, alpha=0.75)
    plt.show()

"""

anim = animation.FuncAnimation(
    fig, animate, init_func=init, frames=99, interval=0.01, blit=True
)

plt.show()