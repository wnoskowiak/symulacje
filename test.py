import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

boxsize=8.0
eps=1.0
sigma=1.0
r0=0.5
dt=0.01
T=0.1
kb =1
nx=4
ny=4
particlenumber=nx*ny
dx=boxsize/nx
dy=boxsize/ny
dx=2
dy=2

def pbc(x1):
    x12 = x1
    if x12[0] > boxsize / 2:
        x12[0] = x12[0] - boxsize
    elif x12[0] < -boxsize / 2:
        x12[0] = x12[0] + boxsize
    if x12[1] > boxsize / 2:
        x12[1] = x12[1] - boxsize
    elif x12[1] < -boxsize / 2:
        x12[1] = x12[1] + boxsize
    return x12

class czastka:
    
    def __init__(self, r, v):
        self.v=v
        self.r=r
        self.sila=np.array([0.,0.])

    def update(self,czastki,eta):
        '''sila=np.array([0.,0.])
        for c in czastki:
            if(c==self):
                continue
            sila+=self.F(c.r)'''
        self.v=(2*eta-1)*self.v+eta*self.sila*dt
        self.r=self.r+self.v*dt
        if(self.r[0]>boxsize):
            self.r[0]-=boxsize
        elif(self.r[0]<0):
            self.r[0]+=boxsize
        if(self.r[1]>boxsize):
            self.r[1]-=boxsize
        elif(self.r[1]<0):
            self.r[1]+=boxsize
        return

    def getv(self):
        sila=np.array([0.,0.])
        for c in czastki:
            if(c==self):
                continue
            sila+=self.F(c.r)
        self.sila=sila
        return self.v+sila*dt/2  
    
    def Energia(self):
        v=self.getv()
        return np.dot(v,v)/2

    def cisn(self,czastki):
        costam=0.
        for c in czastki:
            if(c==self):
                continue
            f=self.F(c.r)
            r=pbc(c.r-self.r)
            costam+=np.dot(r,f)
        return costam       

    def poten(self,czastki):
        V=0
        for c in czastki:
            if(c==self):
                continue
            r=self.r-c.r
            r=pbc(r)
            r=np.sqrt(np.dot(r,r))
            V+=4*eps*(sigma/(r**12)-sigma/(r**6))
        return V

    def F(self,r2):
        r=self.r-r2
        r=pbc(r)
        r=np.sqrt(np.dot(r,r))
        if(r>2.5*sigma):
            return 0
        return -48*eps/sigma/sigma*(((sigma/r)**(14)-((sigma/r)**(8)/2)))*pbc(r2-self.r)

czastki=[]  #generacja
for i in range(4):
    for ii in range(4):
        r=np.array([(i*dx+1),(ii*dy+1)])
        v=np.array([(np.random.random()-1/2),(np.random.random()-1/2)])
        czastki.append(czastka(r,v))

sumv=0. #środek masy
for c in czastki:
    sumv+=c.v
sumv/=particlenumber
for c in czastki:
    c.v-=sumv

sumv2=0. #skalowanie do temperatury
for c in czastki:
    sumv2+=np.dot(c.v,c.v)
sumv2 /= particlenumber
fs=np.sqrt(T/sumv2)
for c in czastki:
        c.v*=fs

en=0
while True:
    
    energia=0.
    for c in czastki:
        energia+=c.Energia()
    temp=energia*2/2/16*2
    cisn=16*temp/8/8
    pot=0
    #pot = np.sum([c.poten(czastki) for c in czastki ])
    for c in czastki:
        pot+=c.poten(czastki)
        cisn-=c.cisn(czastki)/2/8/8

    eta=np.sqrt(T/temp)
    czastkikopia=czastki
    for c in czastki:
        c.update(czastkikopia,eta)
    
    if (en%100==0): 
        plt.clf() 
        F = plt.gcf() 
        for c in czastki:
            a = plt.gca() 
            cir = Circle((c.r[0],c.r[1]), radius=r0) 
            a.add_patch(cir) 
            plt.plot() 
        print(en,temp,cisn[0],energia,pot,energia+pot)
        plt.xlim((0,boxsize)) 
        plt.ylim((0,boxsize))    
        F.set_size_inches((6,6)) 
        nStr=str(en)
        nStr=nStr.rjust(6,'0')
        plt.title("Symulacja gazu Lennarda-Jonesa, krok"+nStr)
        plt.savefig('img'+nStr+'.png')
    en+=1

