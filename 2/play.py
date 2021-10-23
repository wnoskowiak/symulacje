import numpy as np
import matplotlib.pyplot as plt
from calkowanie import Simulation_frog, Simulation_vertel, Simulation_euler

a = Simulation_frog(1,0.001,[{'m':1, 'init_pos':np.array([0,-1]), 'init_momentum':np.array([.6,0])},
                             {'m':1, 'init_pos':np.array([0,1]), 'init_momentum':np.array([-.6,0])},])
print(a)
body_1x = []
body_1y = []
body_2x = []
body_2y = []
body_3x = []
body_3y = []
for _ in range(300000):
    a.step()
    body_1x.append(a.bodies[0].pos[0])
    body_1y.append(a.bodies[0].pos[1])
    body_2x.append(a.bodies[1].pos[0])
    body_2y.append(a.bodies[1].pos[1])
    #body_3x.append(a.bodies[2].pos[0])
    #body_3y.append(a.bodies[2].pos[1])

plt.plot(body_1x, body_1y)
plt.plot(body_2x, body_2y)
#plt.plot(body_3x, body_3y)
#plt.title("Frog")
plt.show()

