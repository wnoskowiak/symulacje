import numpy as np
import itertools
class Frog():

    def __init__(self, m, init_pos, init_momentum, parent):
        self.m = m
        self.pos = init_pos
        self.parent = parent
        self.half_speed = init_momentum/self.m

    def new_speed(self, f):
        return self.half_speed + (f/self.m)*self.parent.dt

    def new_r(self, f, v):
        return self.pos + v*self.parent.dt


    def step(self):
        force = self.parent.F(self)
        new_speed = self.new_speed(force)
        pom = self.new_r(force, new_speed)
        x=0
        if pom[0]<0:
            pom[0] = pom[0] + 8 
        if pom[1]<0:
            pom[1] = pom[1] + 8 
        new_pos = np.array([pom[0]%8, pom[1]%8])
        self.half_speed = new_speed
        self.pos = new_pos
        return self.pos

class Simulation_frog():


    def __init__(self, eps, sig, dt, box_size, param_list):
        self.eps = eps
        self.sig = sig
        self.dt = dt
        self.time = 0
        self.box_size = box_size
        bodies = [
            Frog(
                element['m'], element['init_pos'],element['init_momentum'], self
            )
            for element in param_list
        ]
        self.bodies = bodies
        cases = []
        for element in itertools.combinations_with_replacement([1,2,3], len(self.bodies[0].pos)):
            a = itertools.combinations(element, len(self.bodies[0].pos))
            for b in a:
                cases.append(b)
        self.cases = cases

    def force_element(self, pos1, pos2):

        def closest_image(obj1,obj2):
            x12 = obj1 - obj2
            for i in range(len(x12)):
                if x12[i] > self.box_size / 2:
                    x12[i] = x12[i] - self.box_size
                elif x12[i] < - self.box_size / 2:
                    x12[i] = x12[i] + self.box_size
            return x12
        r = closest_image(pos1, pos2)
        r_length = np.linalg.norm(r)
        #print(r_length)
        r_ver = r/r_length
        parenth_pom = self.sig / r_length
        parenth = parenth_pom**13 - ((parenth_pom**7)/2)
        magnitude = (parenth * 48 * self.eps)/(self.sig)
        return np.multiply(magnitude,r_ver)

    def F(self, object):



        force = np.zeros(len(self.bodies[0].pos))
        for element in self.cases:
            for element in self.bodies:
                if element != object:
                    force = force + self.force_element(object.pos, element.pos)
        return force


    def step(self):
        self.time = self.time + self.dt
        for body in self.bodies:
            body.step()

