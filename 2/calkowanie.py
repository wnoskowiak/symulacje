import numpy as np
import matplotlib.pyplot as plt


class Euler():

    def __init__(self, m, init_pos, init_momentum, parent):
        self.m = m
        self.pos = init_pos
        self.momentum = init_momentum
        self.parent = parent

    def get_v(self):
        return self.momentum/self.m

    def new_r(self):
        element_1 = np.multiply(self.get_v(), self.parent.dt)
        element_2 = (np.multiply((self.parent.F(self)/self.m),(self.parent.dt*self.parent.dt)))/2
        return self.pos + element_1 + element_2

    def new_momentum(self):
        return self.momentum + np.multiply(self.parent.F(self), self.parent.dt)

    def step(self):
        pos = self.new_r()
        mom = self.new_momentum()
        self.pos = pos
        self.momentum = mom
        return self.pos, self.momentum


class Simulation_euler():


    def __init__(self, G, dt, param_list):
        self.G = G
        self.dt = dt
        self.time = 0
        bodies = [
            Euler(
                element['m'], element['init_pos'], element['init_momentum'], self
            )
            for element in param_list
        ]
        self.bodies = bodies

    def force_element(self, obj1, obj2):
        r = -obj1.pos + obj2.pos
        r_length = np.linalg.norm(r)
        #print(r_length)
        r_ver = np.divide(r,r_length)
        return np.multiply(((-self.G*obj1.m*obj2.m)/(r_length*r_length)),r_ver)

    def F(self, object):
        force = [
            self.force_element(element, object)
            for element in self.bodies
            if element != object
        ]
        print(force, object.m)
        return np.sum(force)

    def step(self):
        self.time = self.time + self.dt
        for body in self.bodies:
            body.step()
        

a = Simulation_euler(0.01,0.001,[{'m':0.1, 'init_pos':np.array([2,0]), 'init_momentum':np.array([0,0.1])}, {'m':500, 'init_pos':np.array([0,0]), 'init_momentum':np.array([0,0])}])
print(a)
body_1x = []
body_1y = []
body_2x = []
body_2y = []
for _ in range(3):
    a.step()
    body_1x.append(a.bodies[0].pos[0])
    body_1y.append(a.bodies[0].pos[1])
    body_2x.append(a.bodies[1].pos[0])
    body_2y.append(a.bodies[1].pos[1])
plt.plot(body_1x, body_1y)
plt.plot(body_2x, body_2y)
plt.show()
