from collections import deque
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from multiprocessing import Pool

def neighbours(i,n):
    sasiad=[]
    if(i[0]!=n-1):
        sasiad.append((i[0]+1,i[1]))
    if(i[0]!=0):
        sasiad.append((i[0]-1,i[1]))
    if(i[1]!=n-1):
        sasiad.append((i[0],i[1]+1))
    if(i[1]!=0):
        sasiad.append((i[0],i[1]-1))
    return sasiad

def Leath(p,n):
    brzeg=0
    lattice=np.ones((n,n))*(-1)
    tossing=np.random.random((n,n))<p
    start=(n//2,n//2)
    cluster=deque()
    cluster.append(start)
    lattice[start]=1
    while(len(cluster)>0):
        i=cluster.pop()
        neighboury=neighbours(i,n)
        if(len(neighboury)<4):
            brzeg=1
            break
        for neighbor in neighboury:
            if(lattice[neighbor]==-1):
                if(tossing[neighbor]):
                    lattice[neighbor]=1
                    cluster.append(neighbor)
                else:
                    lattice[neighbor]=0
    return brzeg

def f(x,pc,a):
    return np.tanh((x-pc)/a)/2+1/2
def lin(x,a,b):
    return x*a+b
def wyk(x,a):
    return a*(x**(-3/4))

def policz(s):
    size=50+5*s
    praw=[]
    P=[]
    for p in range(100):
        sumaP=0
        prop=p/1000+0.54
        for _ in range(100):
            Ph=Leath(prop,size)
            sumaP+=Ph
        P.append(sumaP/100)
        praw.append(prop)
    #print(size,praw,P)
    popt, _ = curve_fit(f, praw, P)
    print(size,popt)
    return popt[0], popt[1], size

sizes=[]
obl=[]
obl2=[]

if __name__ == '__main__':
    with Pool(12) as p:
        obliczone=p.map(policz, range(100))
        #sizes.append(size)
        #obl.append(po1)
        #obl2.append(po2)
    oblicz2=np.transpose(obliczone)
    
    xdata=[1/p for p in oblicz2[2]]
    popt2, _ = curve_fit(lin, xdata, oblicz2[0])
    print(popt2)

    plt.title('Perkolacja zmienne prawdopodobienstwo i rozmiar')
    plt.plot(xdata,oblicz2[0])
    ydata=[lin(x,popt2[0],popt2[1]) for x in xdata]
    plt.plot(xdata,ydata)
    plt.grid()
    plt.savefig('Perkolacja zmienne prawdopodobienstwo i rozmiar.png')
    plt.cla()

    popt3, _ = curve_fit(wyk, oblicz2[2], oblicz2[1])
    print(popt3)

    plt.title('Perkolacja zmienne prawdopodobienstwo i rozmiar2')
    ydata=[wyk(x,popt3) for x in oblicz2[2]]
    plt.yscale("log")
    plt.xscale("log")
    plt.plot(oblicz2[2],oblicz2[1])
    plt.plot(oblicz2[2],ydata)
    plt.grid()
    plt.savefig('Perkolacja zmienne prawdopodobienstwo i rozmiar2.png')