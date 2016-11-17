import pylab as pl
r=13#set a global variable for the radius of stadium
import math
class billiard:
    def __init__(self,time_of_duration,intial_x,intial_y,intial_vx,intial_vy,accuracy,alpha):
        self.dt=0.01
        self.steps = int(time_of_duration // self.dt + 1)
        self.intial_vx=intial_vx
        self.intial_vy=intial_vy
        self.intial_x=intial_x
        self.x=[intial_x]
        self.y=[intial_y]
        self.vx=[intial_vx]
        self.vy=[intial_vy]
        self.accuracy=accuracy
        self.alpha=alpha
        self.T=[0]
    def movement(self):
        for i in range(self.steps):
            self.vx.append(self.intial_vx)
            self.vy.append(self.intial_vy)
            
            self.x.append(self.x[-1]+self.vx[-1]*self.dt/1)
            self.y.append(self.y[-1]+self.vy[-1]*self.dt/1)
            
            if self.x[-1]**2+self.y[-1]**2>r**2:                                
                break
            self.T.append(self.T[-1]+self.dt)
    
    def collisions(self):   
        cos_theta=self.x[-1]/r
        sin_theta=self.y[-1]/r
        
        vi_prependicular_x=abs(self.vx[-1]*cos_theta+self.vy[-1]*sin_theta)*cos_theta
        vi_prependicular_y=abs(self.vx[-1]*cos_theta+self.vy[-1]*sin_theta)*sin_theta
        vi_parallel_x=self.vx[-1]-abs(self.vx[-1]*cos_theta+self.vy[-1]*sin_theta)*cos_theta
        vi_parallel_y=self.vy[-1]-abs(self.vx[-1]*cos_theta+self.vy[-1]*sin_theta)*sin_theta    
        
        vf_parallel_x=vi_parallel_x
        vf_parallel_y=vi_parallel_y
        vf_prependicular_x=-vi_prependicular_x
        vf_prependicular_y=-vi_prependicular_y
        
        vf_x=vf_parallel_x+vf_prependicular_x
        vf_y=vf_parallel_y+vf_prependicular_y
        return[vf_x,vf_y]
    
    def movement2(self,vi_x,vi_y):       
        for i in range(self.steps):
                        
            self.vx.append(vi_x)
            self.vy.append(vi_y)
            
            self.x.append(self.x[-1]+self.vx[-1]*self.dt/1)
            self.y.append(self.y[-1]+self.vy[-1]*self.dt/1)
            self.T.append(self.T[-1]+self.dt)
            if self.x[-1]**2+self.y[-1]**2>r**2:
                break
        
        self.x[-1]=self.x[-2]#To imporve the accuracy near the boundary
        self.y[-1]=self.y[-2]     
        for i in range(self.steps):
            self.vx.append(vi_x)
            self.vy.append(vi_y)
            
            self.x.append(self.x[-1]+self.vx[-1]*self.dt/self.accuracy)
            self.y.append(self.y[-1]+self.vy[-1]*self.dt/self.accuracy)

            if self.x[-1]**2+self.y[-1]**2>r**2:
                break
    def new_movement(self):
        for i in range(self.steps):
            self.vx.append(self.intial_vx)
            self.vy.append(self.intial_vy)
                
            self.x.append(self.x[-1]+self.vx[-1]*self.dt/1)
            self.y.append(self.y[-1]+self.vy[-1]*self.dt/1)
            
            if (self.x[-1])**2+(self.y[-1]-self.alpha*r)**2>r**2:
                break
            self.T.append(self.T[-1]+self.dt)
    def new_collisions(self):
        if self.y[-1]>=self.alpha*r:
            cos_theta=self.x[-1]/r
            sin_theta=(self.y[-1]-self.alpha*r)/r
            
            vi_prependicular_x=abs(self.vx[-1]*cos_theta+self.vy[-1]*sin_theta)*cos_theta
            vi_prependicular_y=abs(self.vx[-1]*cos_theta+self.vy[-1]*sin_theta)*sin_theta
            vi_parallel_x=self.vx[-1]-abs(self.vx[-1]*cos_theta+self.vy[-1]*sin_theta)*cos_theta
            vi_parallel_y=self.vy[-1]-abs(self.vx[-1]*cos_theta+self.vy[-1]*sin_theta)*sin_theta    
            
            vf_parallel_x=vi_parallel_x
            vf_parallel_y=vi_parallel_y
            vf_prependicular_x=-vi_prependicular_x
            vf_prependicular_y=-vi_prependicular_y
            
            vf_x=vf_parallel_x+vf_prependicular_x
            vf_y=vf_parallel_y+vf_prependicular_y
            return[vf_x,vf_y]
        if self.y[-1]<=-self.alpha*r:
            cos_theta=self.x[-1]/r
            sin_theta=(self.y[-1]+self.alpha*r)/r
            
            vi_prependicular_x=abs(self.vx[-1]*cos_theta+self.vy[-1]*sin_theta)*cos_theta
            vi_prependicular_y=abs(self.vx[-1]*cos_theta+self.vy[-1]*sin_theta)*sin_theta
            vi_parallel_x=self.vx[-1]-abs(self.vx[-1]*cos_theta+self.vy[-1]*sin_theta)*cos_theta
            vi_parallel_y=self.vy[-1]-abs(self.vx[-1]*cos_theta+self.vy[-1]*sin_theta)*sin_theta    
            
            vf_parallel_x=vi_parallel_x
            vf_parallel_y=vi_parallel_y
            vf_prependicular_x=-vi_prependicular_x
            vf_prependicular_y=-vi_prependicular_y
            
            vf_x=vf_parallel_x+vf_prependicular_x
            vf_y=vf_parallel_y+vf_prependicular_y
            return[vf_x,vf_y]
        if  -self.alpha*r<self.y[-1]<self.alpha*r:
            vf_x=-self.vx[-1]
            vf_y=self.vy[-1]
            return[vf_x,vf_y]
    def new_movement2(self,vi_x,vi_y):       
        for i in range(self.steps):                        
            self.vx.append(vi_x)
            self.vy.append(vi_y)
                
            self.x.append(self.x[-1]+self.vx[-1]*self.dt/1)
            self.y.append(self.y[-1]+self.vy[-1]*self.dt/1)
            self.T.append(self.T[-1]+self.dt)
            
            if self.y[-1]>=self.alpha*r:
                if (self.y[-1]-self.alpha*r)**2+self.x[-1]**2>r**2:
                    break
            if   -self.alpha*r<=self.y[-1]<=self.alpha*r:
                if self.x[-1]>r or self.x[-1]<-r:
                    break
            if  self.y[-1]<=-self.alpha*r:
                if ((self.y[-1]+self.alpha*r)**2+self.x[-1]**2)>r**2:
                    break
        self.x[-1]=self.x[-2]#To imporve the accuracy near the boundary
        self.y[-1]=self.y[-2]     
        for i in range(self.steps):
            self.vx.append(vi_x)
            self.vy.append(vi_y)
            
            self.x.append(self.x[-1]+self.vx[-1]*self.dt/self.accuracy)
            self.y.append(self.y[-1]+self.vy[-1]*self.dt/self.accuracy)
            if self.y[-1]>=self.alpha*r:
                if (self.y[-1]-self.alpha*r)**2+self.x[-1]**2>r**2:
                    break
            if   -self.alpha*r<=self.y[-1]<=self.alpha*r:
                if self.x[-1]>r or self.x[-1]<-r:
                    break
            if  self.y[-1]<=-self.alpha*r:
                if ((self.y[-1]+self.alpha*r)**2+self.x[-1]**2)>r**2:
                    break
        return [self.x,self.y]  
    def keep_record_of_phaseplot(self):
        self.phase_x=[]
        self.phase_vx=[]
        for j in range(len(self.y)):
            if -0.01<self.y[j]<0.01:
                self.phase_x.append(self.x[j])
                self.phase_vx.append(self.vx[j])
            j=j+1
    def show_trajectory(self):
        pl.plot(self.x,self.y,label='$\\alpha$ is %.4f'%self.alpha)#label='Boundary recise is %d'%self.accuracy)
        #pl.title('Trajectory of the Stadium ball')
        #pl.xlabel('x($m$)')
        #pl.ylabel('y($m$)') 
        #pl.subplot(2,2,2)
        pl.legend(loc='upper right',frameon = True,fontsize='xx-small')
         
    def show_boundary(self):
       i=0
       tmp_x=[]
       tmp_y=[]
       while i <=2*math.pi:
            
            tmp_x.append(r*math.cos(i))
            tmp_y.append(r*math.sin(i))
            i=i+0.01
       pl.plot(tmp_x,tmp_y)
    
    def phase_plot(self):
        pl.scatter(self.phase_x,self.phase_vx,s=2,label='$\\alpha$ is %.4f'%self.alpha)
        #pl.title('Phase Plot')
        #pl.xlabel('x($m$)')
        #pl.ylabel('$v_{x}$($m/s$)')
        pl.legend(loc='upper right',frameon = True,fontsize='x-small')
        pl.show()
    def show_new_boundary(self):
       i=0
       tmp_x=[]
       tmp_y=[]
       while i <=1*math.pi:
            
            tmp_x.append(r*math.cos(i))
            tmp_y.append(self.alpha*r+r*math.sin(i))
            i=i+0.01
       while math.pi<=i<=2*math.pi:
            tmp_x.append(r*math.cos(i))
            tmp_y.append(-self.alpha*r+r*math.sin(i))
            i=i+0.01
       pl.plot(tmp_x,tmp_y)
       pl.plot([r,r],[-self.alpha*r,self.alpha*r])
       pl.plot([-r,-r],[-self.alpha*r,self.alpha*r])
        
        
kx=[]
ky=[]
px=[]
py=[]
distance=[]

a=billiard(100,3,0,2,2,100,0.01)
a.new_movement()
for i in range(1000):
    m=a.new_collisions()    
    a.new_movement2(m[0],m[1])
    k=a.new_movement2(m[0],m[1])
    kx.append(k[0][-1])
    ky.append(k[1][-1])

b=billiard(100,3,0,2,2,100,0.01)
b.new_movement()
for i in range(1000):
    n=a.new_collisions()    
    b.new_movement2(n[0],n[1])
    p=b.movement2(n[0],n[1])
    px.append(p[0][-1])
    py.append(p[1][-1])

