import numpy as np
import matplotlib.pyplot as plt
from calkowanie import Simulation_euler


a = Simulation_euler(0.01,0.001,[{'m':0.1, 'init_pos':np.array([2,0]), 'init_momentum':np.array([0,0.1])}, {'m':500, 'init_pos':np.array([0,0]), 'init_momentum':np.array([0,0])}])
print(a)
body_1x = []
body_1y = []
body_2x = []
body_2y = []
for _ in range(30000):
    a.step()
    body_1x.append(a.bodies[0].pos[0])
    body_1y.append(a.bodies[0].pos[1])
    body_2x.append(a.bodies[1].pos[0])
    body_2y.append(a.bodies[1].pos[1])
plt.plot(body_1x, body_1y)
plt.plot(body_2x, body_2y)
plt.show()
