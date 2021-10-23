import numpy as np
import matplotlib.pyplot as plt
from calkowanie import Simulation_frog, Simulation_vertel, Simulation_euler

a = Simulation_frog(1,0.001,[{'m':1, 'init_pos':np.array([0.97000436,-0.24308753]), 'init_momentum':np.array([-0.93240737/2,-0.86473146/2])},
                             {'m':1, 'init_pos':np.array([-0.97000436,0.24308753]), 'init_momentum':np.array([-0.93240737/2,-0.86473146/2])},
                             {'m':1, 'init_pos':np.array([0,0]), 'init_momentum':np.array([0.93240737,0.86473146])}])
print(a)
body_1x = []
body_1y = []
body_2x = []
body_2y = []
body_3x = []
body_3y = []
for _ in range(30000):
    a.step()
    body_1x.append(a.bodies[0].pos[0])
    body_1y.append(a.bodies[0].pos[1])
    body_2x.append(a.bodies[1].pos[0])
    body_2y.append(a.bodies[1].pos[1])
    body_3x.append(a.bodies[2].pos[0])
    body_3y.append(a.bodies[2].pos[1])

plt.plot(body_1x, body_1y)
plt.plot(body_2x, body_2y)
plt.plot(body_3x, body_3y)
plt.title("Frog")
plt.show()

a = Simulation_vertel(1,0.001,[{'m':1, 'init_pos':np.array([0.97000436,-0.24308753]), 'init_momentum':np.array([-0.93240737/2,-0.86473146/2])},
                             {'m':1, 'init_pos':np.array([-0.97000436,0.24308753]), 'init_momentum':np.array([-0.93240737/2,-0.86473146/2])},
                             {'m':1, 'init_pos':np.array([0,0]), 'init_momentum':np.array([0.93240737,0.86473146])}])
print(a)
body_1x = []
body_1y = []
body_2x = []
body_2y = []
body_3x = []
body_3y = []
for _ in range(30000):
    a.step()
    body_1x.append(a.bodies[0].pos[0])
    body_1y.append(a.bodies[0].pos[1])
    body_2x.append(a.bodies[1].pos[0])
    body_2y.append(a.bodies[1].pos[1])
    body_3x.append(a.bodies[2].pos[0])
    body_3y.append(a.bodies[2].pos[1])

plt.plot(body_1x, body_1y)
plt.plot(body_2x, body_2y)
plt.plot(body_3x, body_3y)
plt.title("Vertel")
plt.show()


a = Simulation_euler(1,0.001,[{'m':1, 'init_pos':np.array([0.97000436,-0.24308753]), 'init_momentum':np.array([-0.93240737/2,-0.86473146/2])},
                             {'m':1, 'init_pos':np.array([-0.97000436,0.24308753]), 'init_momentum':np.array([-0.93240737/2,-0.86473146/2])},
                             {'m':1, 'init_pos':np.array([0,0]), 'init_momentum':np.array([0.93240737,0.86473146])}])
print(a)
body_1x = []
body_1y = []
body_2x = []
body_2y = []
body_3x = []
body_3y = []

for _ in range(30000):
    a.step()
    body_1x.append(a.bodies[0].pos[0])
    body_1y.append(a.bodies[0].pos[1])
    body_2x.append(a.bodies[1].pos[0])
    body_2y.append(a.bodies[1].pos[1])
    body_3x.append(a.bodies[2].pos[0])
    body_3y.append(a.bodies[2].pos[1])
    

plt.plot(body_1x, body_1y)
plt.plot(body_2x, body_2y)
plt.plot(body_3x, body_3y)

plt.title("Euler")
plt.show()

a = Simulation_frog(1,0.001,[{'m':1, 'init_pos':np.array([0.97000436,-0.24308753]), 'init_momentum':np.array([-0.93240737/2,-0.86473146/2])},
                             {'m':1, 'init_pos':np.array([-0.97000436,0.24308753]), 'init_momentum':np.array([-0.93240737/2,-0.86473146/2])},
                             {'m':1, 'init_pos':np.array([-0.97000436*3,0.24308753*4]), 'init_momentum':np.array([0.93240737/1.2,0.86473146/0.8])},
                             {'m':1, 'init_pos':np.array([0,0]), 'init_momentum':np.array([0.93240737,0.86473146])}])
print(a)
body_1x = []
body_1y = []
body_2x = []
body_2y = []
body_3x = []
body_3y = []
body_4x = []
body_4y = []
for _ in range(30000):
    a.step()
    body_1x.append(a.bodies[0].pos[0])
    body_1y.append(a.bodies[0].pos[1])
    body_2x.append(a.bodies[1].pos[0])
    body_2y.append(a.bodies[1].pos[1])
    body_3x.append(a.bodies[2].pos[0])
    body_3y.append(a.bodies[2].pos[1])
    body_4x.append(a.bodies[3].pos[0])
    body_4y.append(a.bodies[3].pos[1])

plt.plot(body_1x, body_1y)
plt.plot(body_2x, body_2y)
plt.plot(body_3x, body_3y)
plt.plot(body_4x, body_4y)
plt.title("Frog")
plt.show()
