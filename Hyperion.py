import math
import matplotlib.pyplot as plt
# physical constants
GM=4*(math.pi**2)
perihelion=0.39*(1-0.206) # to remain the oerihelion the same as that of Mercury.
# begin the class
class precession:
    def __init__(self,e=0.206,time=2.,dt=0.00001,vcoefficient=1,beta=2,alpha=0,intial_w=0,intial_sita=0):
        self.intial_sita=intial_sita
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
        self.w=[intial_w]
        self.sita=[intial_sita]
        self.T=[0]
        self.dt=dt
        self.time=time
        self.ThetaPrecession=[]
        self.TimePrecession=[]
        return None
    def calculate_reset(self):
        while self.T[-1]<self.time:
            r=math.sqrt(self.X[-1]**2+self.Y[-1]**2)
            newVx=self.Vx[-1]-(GM*(1+self.alpha/r**2)*self.X[-1]/r**(1+self.beta))*self.dt
            newX=self.X[-1]+newVx*self.dt
            newVy=self.Vy[-1]-(GM*(1+self.alpha/r**2)*self.Y[-1]/r**(1+self.beta))*self.dt
            newY=self.Y[-1]+newVy*self.dt
            newW=self.w[-1]-3*GM/(r**5)*(self.X[-1]*math.sin(self.sita[-1])-self.Y[-1]*math.cos(self.sita[-1]))*(self.X[-1]*math.cos(self.sita[-1])+self.Y[-1]*math.sin(self.sita[-1]))*self.dt
            newSita=self.dt*self.w[-1]+self.sita[-1]
           
            self.Vx.append(newVx)
            self.Vy.append(newVy)
            self.X.append(newX)
            self.Y.append(newY)
            self.w.append(newW)
            self.sita.append(newSita)
            self.T.append(self.T[-1]+self.dt)
            
            while self.sita[-1]>=1*math.pi:
                self.sita[-1]=self.sita[-1]-2*math.pi
            while  self.sita[-1]<=-1*math.pi:
                self.sita[-1]=self.sita[-1]+2*math.pi 
            
            
        return 0
    def calculate_nonreset(self):
        while self.T[-1]<self.time:
            r=math.sqrt(self.X[-1]**2+self.Y[-1]**2)
            newVx=self.Vx[-1]-(GM*(1+self.alpha/r**2)*self.X[-1]/r**(1+self.beta))*self.dt
            newX=self.X[-1]+newVx*self.dt
            newVy=self.Vy[-1]-(GM*(1+self.alpha/r**2)*self.Y[-1]/r**(1+self.beta))*self.dt
            newY=self.Y[-1]+newVy*self.dt
            newW=self.w[-1]-3*GM/(r**5)*(self.X[-1]*math.sin(self.sita[-1])-self.Y[-1]*math.cos(self.sita[-1]))*(self.X[-1]*math.cos(self.sita[-1])+self.Y[-1]*math.sin(self.sita[-1]))*self.dt
            newSita=self.dt*self.w[-1]+self.sita[-1]
           
            self.Vx.append(newVx)
            self.Vy.append(newVy)
            self.X.append(newX)
            self.Y.append(newY)
            self.w.append(newW)
            self.sita.append(newSita)
            self.T.append(self.T[-1]+self.dt)
                        
        return 0
    def plot(self,slogan=''):
        plt.scatter(self.sita,self.w,label=slogan,s=0.1)
        plt.legend(loc='upper right',frameon=False,fontsize='small')
        plt.grid(True)
        
        plt.title('Phase Plot(Elleptical Orbit) e=0.206 $\\theta$ versus $w$')
        #plt.title('The Hyperion(Circular orbit) $w$ versus time')
        #plt.title('The Hyperion(Elleptical orbit) $\\theta$ versus time')
        #plt.title('The Hyperion(Elleptical orbit) $w$ versus time')
        
        plt.ylabel('$w$')        
        plt.xlabel('$\\theta$')
        
        #plt.xlabel('timr(yr)')
        #plt.xlim(-0.6,0.6)
        #plt.ylim(-0.6,0.6)
        #plt.scatter(0,0)
        
        return 0
