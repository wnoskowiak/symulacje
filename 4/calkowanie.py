import numpy as np
import itertools
class Frog():

    def __init__(self, m, init_pos, init_momentum, parent):
        self.m = m
        self.pos = init_pos
        self.parent = parent
        self.half_speed = init_momentum/self.m
        self.speed = init_momentum/self.m

    def new_speed(self, f):
        return (2*self.parent.eta-1)*self.half_speed + self.parent.eta*(f/self.m)*self.parent.dt

    def new_helper_speed(self, f):
        return self.half_speed + (f/(2*self.m))*self.parent.dt

    def new_r(self, f, v):
        return self.pos + v*self.parent.dt

    def en_kin(self):
        return np.dot(self.half_speed,self.half_speed)*self.m/2

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
        speed = self.new_helper_speed(force)
        self.speed = speed
        return self.pos

class Simulation_frog():


    def __init__(self, eps, sig, temp, dt, box_size, param_list):
        self.eps = eps
        self.sig = sig
        self.dt = dt
        self.time = 0
        self.box_size = box_size
        self.temp = temp
        self.eta = temp
        self.momtemp= []
        self.pot = []
        self.press = []
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
        self.bake_forces()

    def closest_image(self,obj1,obj2):
        x12 = obj1 - obj2
        for i in range(len(x12)):
            if x12[i] > self.box_size / 2:
                x12[i] = x12[i] - self.box_size
            elif x12[i] < - self.box_size / 2:
                x12[i] = x12[i] + self.box_size
        return x12

    def force_element(self, pos1, pos2):
        #print(type(pos1.pos))
        #print(type(pos2.pos))
        r = self.closest_image((pos1.pos), (pos2.pos))
        r_length = np.linalg.norm(r)
        #print(r_length)
        r_ver = r/r_length
        parenth_pom = self.sig / r_length
        parenth = parenth_pom**13 - ((parenth_pom**7)/2)
        magnitude = (parenth * 48 * self.eps)/(self.sig)
        return np.multiply(magnitude,r_ver)

    def F(self, object):
        index = self.bodies.index(object)
        force = np.zeros(len(self.bodies[0].pos))
        for i in range(len(self.bodies)):
            try:
                a = self.forces[index][i]
            except:
                a = - self.forces[i][index]
            force += a 
        return force

    def bake_forces(self):
        zero = np.zeros(len(self.bodies[0].pos))
        forces = {}
        for i in range(len(self.bodies)):
            element = {
                j: zero
                if i == j
                else self.force_element(self.bodies[i], self.bodies[j])
                for j in range(i+1)
            }
            forces[i] = element
        self.forces = forces

    def pressure(self, object):
        index = self.bodies.index(object)
        pressure = 0
        for i in range(len(self.bodies)):
            if i != 0:
                r = self.closest_image(self.bodies[index].pos, self.bodies[i].pos)
                f = self.F(object)
                pressure =+ np.dot(r,f)
        return pressure

    def step(self):
        #self.bake_forces()
        self.time = self.time + self.dt
        Ek = np.sum([body.en_kin() for body in self.bodies])
        #self.ek.append(Ek)
        temp=self.temp
        self.momtemp.append(self.temp)
        cisn=16*temp/8/8
        for body in self.bodies:
            cisn -= self.pressure(body)/2/8/8
        self.press.append(cisn)
        self.eta = np.sqrt(self.temp/temp)
        self.bake_forces()
        for body in self.bodies:
            body.step()



