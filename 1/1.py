import numpy as np
import matplotlib.pyplot as plt
import get_brown
from matplotlib import animation

brownian_motions=get_brown.get_brownian_motion(5000,10)
trajectories_transposed=np.cumsum(brownian_motions,axis=0)
trajectories=trajectories_transposed.transpose()
max_y=np.max(np.abs(trajectories))
x=np.arange(4999)

fig = plt.figure()
ax1 = plt.axes(xlim=(-10, 5010),ylim=(-(1.05*max_y),(1.05*max_y)))
line, = ax1.plot([]) 
plt.axhline(0,color='black')
plt.xlabel("krok")
plt.ylabel("odchylenie od położenia początkowego")

opis = []
lines = []
for i in range(10):
    temp=ax1.plot([], linewidth=1, alpha=0.7)[0]
    lines.append(temp)
    opis.append('Cząstka: {}'.format(i))

plt.legend(opis)

def init():
    #print("here")
    for line in lines:
        line.set_data([0],[0])
    return lines

#traj = np.append(np.zeros([10,1]),trajectories[:,1].reshape(10,1),axis=1)
#print(trajectories[:,:40].reshape(10,40))
#print(trajectories)

def animate(frame):
    data = trajectories[:,:frame].reshape(10,frame)
    #print(data)
    for lnum,line in enumerate(lines):
        #print(line)
        #print(data[lnum],x[:frame])
        line.set_data(x[:frame],data[lnum])
    return lines


anim = animation.FuncAnimation(
    fig, animate, init_func=init, frames=4998, interval=0.1, blit=True
)

plt.show()