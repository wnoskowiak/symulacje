import numpy as np
import matplotlib.pyplot as plt
from calkowanie import Simulation_frog, Frog
import itertools
import random
from matplotlib.patches import Circle

init_pos = itertools.combinations_with_replacement(np.arange(1,9,2),2)
init_mom = [(0, 0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0)]

particleNumber=16
boxsize=8.0
eps=1.0
sigma=1.0
promien=0.5
dt=0.001
temp=0.5
kb = 1
time = np.arange(0,1,dt)

dx = 2
temp=2.5


particles = []
for i in range(4):
    for j in range(4):
        info = {'m': 1, 'init_pos': np.array([i*dx+1, j*dx+1])}
        info['init_momentum']=np.array([(random.uniform(0, 1)-1./2),(random.uniform(0, 1) -1./2)])
        particles.append(info)

sumv=0.0
for p in particles:
    sumv += p['init_momentum']
sumv /= 16

for p in particles:
    p['init_momentum'] = p['init_momentum'] - sumv

sumv2 =0.0
for p in particles:
    sumv2 += np.dot(p['init_momentum'],p['init_momentum'])/2.0

sumv2 /= 16
fs=np.sqrt(temp/sumv2)
for p in particles:
    p['init_momentum']=p['init_momentum']*fs 

a = Simulation_frog(eps, sigma, temp,  dt, boxsize, particles)
a.step()
for t_i in range(len(time)):
    a.step()
    """
    if (t_i%100==0): # co 100-na klatka
        plt.clf() # wyczyść obrazek
        fig = plt.gcf() # zdefiniuj nowy
        for p in a.bodies: # pętla po cząstkach
            aa = plt.gca() # ‘get current axes’ (to add smth to them)
            cir = Circle((p.pos[0],p.pos[1]), radius=0.5) # kółko tam gdzie jest cząstka
            aa.add_patch(cir) # dodaj to kółko do rysunku
            plt.plot() # narysuj
            plt.xlim((0,boxsize)) # obszar do narysowania
            plt.ylim((0,boxsize)) 
            fig.set_size_inches((6,6)) # rozmiar rysunku
            plt.title("Symulacja gazu Lennarda-Jonesa, krok {:06d}".format(t_i))
            plt.savefig("img{:06d}.png".format(t_i)) 
    """

plt.plot(a.press)
plt.plot(a.momtemp)
plt.show()
