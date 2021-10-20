import numpy as np
class Euler():

    def __init__(self, m, init_pos, init_momentum, parent):
        self.m = m
        self.pos = init_pos
        self.momentum = init_momentum
        self.parent = parent

    def get_v(self):
        return self.momentum/self.m

    def new_r(self, f, v):
        element_1 = v*self.parent.dt
        element_2 = (f*self.parent.dt*self.parent.dt/(self.m*2))
        return self.pos + element_1 + element_2

    def new_momentum(self, f):
        return self.momentum + f*self.parent.dt

    def step(self):
        force = self.parent.F(self)
        speed = self.get_v()
        pos = self.new_r(force, speed)
        mom = self.new_momentum(force)
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
        force = np.zeros(len(self.bodies[0].pos))
        for element in self.bodies:
            if element != object:
                force = force+self.force_element(element, object)
        #print(force, object.m)
        return force

    def step(self):
        self.time = self.time + self.dt
        for body in self.bodies:
            body.step()