import matplotlib.pyplot as plt
import math
import numpy as np
from matplotlib import animation

delta_x, c ,r , k = 0.001, 300 , 1 , 1000
delta_t=delta_x/c
T=0.04
N=int(T*c/delta_x)
t=np.linspace(0,T,N+1)

def next_step(y_previous,y_current):
    y_next=[0]
    c1,c2=2*(1-r**2),r**2
    for i in range(1,len(y_current)-1):
        y_next.append(c1*y_current[i]-y_previous[i]+c2*(y_current[i-1]+y_current[i+1]))
    y_next.append(0)
    return y_next

def initial_Gaussian(x_excite):
    y_initial=[]           
    for i in range(1+int(1./delta_x)):
        y_initial.append(math.exp(-k*(i*delta_x-x_excite)**2))
    return y_initial

def initial_real(x_excite):
    y_initial=[]
    for i in range(int(x_excite/delta_x)):
        y_initial.append(i*delta_x/x_excite)
    for i in range(int(x_excite/delta_x),1+int(1./delta_x)):
        y_initial.append((i*delta_x-1.)/(x_excite-1))
    return y_initial

def motion_of_a_point(x_observe,x_excite):
    y_initial=initial_Gaussian(x_excite
    y_observe=[]                
    I=int(x_observe/delta_x)
    y0=y_initial
    y1=y_initial
    y_observe.append(y1[I])
    for i in range(N):
        y2=next_step(y0,y1)
        y0,y1=y1,y2
        y_observe.append(y1[I])
    return y_observe
