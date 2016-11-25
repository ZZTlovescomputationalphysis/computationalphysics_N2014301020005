import math
import numpy as np
import matplotlib.pyplot as plt
# physical constants
GM=4*(math.pi**2)
perihelion=0.39*(1-0.206) # to remain the oerihelion the same as that of Mercury.
# begin the class
class precession:
    def __init__(self,e=0.206,time=2.,dt=0.0001,vcoefficient=1,beta=2,alpha=0.0008):
        self.alpha=alpha
        self.beta=beta
        self.vcoefficient=vcoefficient
        self.e=e
        self.a=perihelion/(1-e)
        self.x0=self.a*(1+e)
        self.y0=0
        self.vx0=0
        self.vy0=self.vcoefficient*math.sqrt((GM*(1-e))/(self.a*(1+e)))
        self.X=[self.x0]
        self.Y=[self.y0]
        self.Vx=[self.vx0]
        self.Vy=[self.vy0]
        self.T=[0]
        self.dt=dt
        self.time=time
        self.ThetaPrecession=[]
        self.TimePrecession=[]
        return None
    def calculate(self):
        while self.T[-1]<self.time:
            r=math.sqrt(self.X[-1]**2+self.Y[-1]**2)
            newVx=self.Vx[-1]-(GM*(1+self.alpha/r**2)*self.X[-1]/r**(1+self.beta))*self.dt
            newX=self.X[-1]+newVx*self.dt
            newVy=self.Vy[-1]-(GM*(1+self.alpha/r**2)*self.Y[-1]/r**(1+self.beta))*self.dt
            newY=self.Y[-1]+newVy*self.dt
            if abs(newX*newVx+newY*newVy)<0.0014 and r<self.a:
                theta=math.acos(self.X[-1]/r)*180/math.pi
                if (self.Y[-1]/r)<0:
                    theta=360-theta
                theta=abs(theta-180)
                self.ThetaPrecession.append(theta)
                self.TimePrecession.append(self.T[-1])
            self.Vx.append(newVx)
            self.Vy.append(newVy)
            self.X.append(newX)
            self.Y.append(newY)
            self.T.append(self.T[-1]+self.dt)
        return 0
    def plot(self,slogan=''):
        plt.plot(self.X,self.Y,label=slogan)
        plt.legend(loc='upper right',frameon=False,fontsize='small')
        plt.grid(True)
        plt.title('The precession of Mercury with different Eccentricity')
        #plt.xlabel('x(AU)')
        #plt.ylabel('y(AU)')
        #plt.xlim(-0.6,0.6)
        #plt.ylim(-0.6,0.6)
        #plt.scatter(0,0)
        
        return 0
    def orientation(self,slogan=''):
        plt.plot(self.TimePrecession,self.ThetaPrecession,label=slogan)
        plt.scatter(self.TimePrecession,self.ThetaPrecession,label=slogan)
        plt.legend(loc='upper right',frameon=False,fontsize='xx-small')
        plt.grid(True)
        print self.ThetaPrecession
        print self.TimePrecession
        return 0

A=precession(e=0.206,time=50.0,alpha=0.8)
A.calculate()
A.orientation(slogan=r'$\alpha=0.008$')

    