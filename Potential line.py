import numpy as np
from pylab import *
from mpl_toolkits.mplot3d import Axes3D

def init_v():
    v=np.zeros((100,100))
    
    v[0:99,50]=30
    return v
class Potential:
    def __init__(self,v=init_v(),E=np.zeros((100,100))):
        self.E=[]        
        self.v=[]
        self.v.append(v)
        self.E.append(E)
        self.q=np.zeros((100,100))
        #self.q[43:44,50]=+1
        #self.q[56:57,50]=-1
        self.dv=np.ones((100,100))
        x=np.linspace(-1,1,100)
        self.dx=x[2]-x[1]
        #print self.v[0][40][60]
        #self.v.append(v)
    
    def j_cal(self):
        while not(np.all(abs(self.dv)<1e-4)):
            next_v=np.zeros((100,100))
            next_E=np.zeros((100,100))
            for i in range(1,next_v.shape[0]-1):
                for j in range(1,next_v.shape[1]-1):
                    next_v[i][j]=0.25*(self.v[-1][i-1][j]+self.v[-1][i+1][j]+self.v[-1][i][j-1]+self.v[-1][i][j+1])+self.q[i][j]*self.dx**2
                    next_E[i][j]=(next_v[i][j-1]-next_v[i][j+1])/(2*self.dx)
                    next_v[0:99,50]=30                   
            self.v.append(next_v)
            self.dv=self.v[-1]-self.v[-2]
    def poplot(self):
        fig=figure()
        ax=fig.add_subplot(1,2,2)
        x=np.linspace(-1,1,100)
        X,Y=np.meshgrid(x,x)
        contourf(X,Y,self.v[-1])
        colorbar()
        ax=fig.add_subplot(1,2,1,projection='3d')
        ax.plot_surface(X,Y,self.v[-1],rstride=4,cstride=4,linewidth=0,cmap=cm.coolwarm)
        plt.title('Potential versus x-y plane')


a=Potential()
a.j_cal()
a.poplot()
print len(a.v)
show()