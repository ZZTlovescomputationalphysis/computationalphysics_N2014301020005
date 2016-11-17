#Divergence Plots
'''
a=billiard(100,1,0,2,3,1.001,0,2,3,100,0.01)
for i in range(100):
    m=a.new_collisions()
    a.new_movement2(m[0],m[1],m[2],m[3])
a.show()
'''
import pylab as pl
r=13#set a global variable for the radius of stadium
import math
class billiard:
    def __init__(self,time_of_duration,intial_x_a,intial_y_a,intial_vx_a,intial_vy_a,intial_x_b,intial_y_b,intial_vx_b,intial_vy_b,accuracy,alpha):
        self.dt=0.01
        self.steps = int(time_of_duration // self.dt + 1)
        self.intial_vx_a=intial_vx_a
        self.intial_vy_a=intial_vy_a
        self.intial_x_a=intial_x_a
        self.x_a=[intial_x_a]
        self.y_a=[intial_y_a]
        self.vx_a=[intial_vx_a]
        self.vy_a=[intial_vy_a]
        
        self.intial_vx_b=intial_vx_b
        self.intial_vy_b=intial_vy_b
        self.intial_x_b=intial_x_b
        self.x_b=[intial_x_b]
        self.y_b=[intial_y_b]
        self.vx_b=[intial_vx_b]
        self.vy_b=[intial_vy_b]
        self.accuracy=accuracy
        self.alpha=alpha
        self.T_a=[0]
        self.T_b=[0]
    def new_movement(self):
        for i in range(self.steps):
            self.vx_a.append(self.intial_vx_a)
            self.vy_a.append(self.intial_vy_a)
                
            self.x_a.append(self.x_a[-1]+self.vx_a[-1]*self.dt/1)
            self.y_a.append(self.y_a[-1]+self.vy_a[-1]*self.dt/1)
            
            if (self.x_a[-1])**2+(self.y_a[-1]-self.alpha*r)**2>r**2:
                break
            self.T_a.append(self.T_a[-1]+self.dt)
          ###            
            self.vx_b.append(self.intial_vx_b)
            self.vy_b.append(self.intial_vy_b)
                
            self.x_b.append(self.x_b[-1]+self.vx_b[-1]*self.dt/1)
            self.y_b.append(self.y_b[-1]+self.vy_b[-1]*self.dt/1)
            
            if (self.x_b[-1])**2+(self.y_b[-1]-self.alpha*r)**2>r**2:
                break
            self.T_b.append(self.T_b[-1]+self.dt)
    def new_collisions(self):
        if self.y_a[-1]>=self.alpha*r:
            cos_theta=self.x_a[-1]/r
            sin_theta=(self.y_a[-1]-self.alpha*r)/r
            
            vi_prependicular_x=abs(self.vx_a[-1]*cos_theta+self.vy_a[-1]*sin_theta)*cos_theta
            vi_prependicular_y=abs(self.vx_a[-1]*cos_theta+self.vy_a[-1]*sin_theta)*sin_theta
            vi_parallel_x=self.vx_a[-1]-abs(self.vx_a[-1]*cos_theta+self.vy_a[-1]*sin_theta)*cos_theta
            vi_parallel_y=self.vy_a[-1]-abs(self.vx_a[-1]*cos_theta+self.vy_a[-1]*sin_theta)*sin_theta    
            
            vf_parallel_x=vi_parallel_x
            vf_parallel_y=vi_parallel_y
            vf_prependicular_x=-vi_prependicular_x
            vf_prependicular_y=-vi_prependicular_y
            
            vf_x_a=vf_parallel_x+vf_prependicular_x
            vf_y_a=vf_parallel_y+vf_prependicular_y

        if self.y_a[-1]<=-self.alpha*r:
            cos_theta=self.x_a[-1]/r
            sin_theta=(self.y_a[-1]+self.alpha*r)/r
            
            vi_prependicular_x=abs(self.vx_a[-1]*cos_theta+self.vy_a[-1]*sin_theta)*cos_theta
            vi_prependicular_y=abs(self.vx_a[-1]*cos_theta+self.vy_a[-1]*sin_theta)*sin_theta
            vi_parallel_x=self.vx_a[-1]-abs(self.vx_a[-1]*cos_theta+self.vy_a[-1]*sin_theta)*cos_theta
            vi_parallel_y=self.vy_a[-1]-abs(self.vx_a[-1]*cos_theta+self.vy_a[-1]*sin_theta)*sin_theta    
            
            vf_parallel_x=vi_parallel_x
            vf_parallel_y=vi_parallel_y
            vf_prependicular_x=-vi_prependicular_x
            vf_prependicular_y=-vi_prependicular_y
            
            vf_x_a=vf_parallel_x+vf_prependicular_x
            vf_y_a=vf_parallel_y+vf_prependicular_y

        if  -self.alpha*r<self.y_a[-1]<self.alpha*r:
            vf_x_a=-self.vx_a[-1]
            vf_y_a=self.vy_a[-1]

       
       ####
        if self.y_b[-1]>=self.alpha*r:
            cos_theta=self.x_b[-1]/r
            sin_theta=(self.y_b[-1]-self.alpha*r)/r
            
            vi_prependicular_x=abs(self.vx_b[-1]*cos_theta+self.vy_b[-1]*sin_theta)*cos_theta
            vi_prependicular_y=abs(self.vx_b[-1]*cos_theta+self.vy_b[-1]*sin_theta)*sin_theta
            vi_parallel_x=self.vx_b[-1]-abs(self.vx_b[-1]*cos_theta+self.vy_b[-1]*sin_theta)*cos_theta
            vi_parallel_y=self.vy_b[-1]-abs(self.vx_b[-1]*cos_theta+self.vy_b[-1]*sin_theta)*sin_theta    
            
            vf_parallel_x=vi_parallel_x
            vf_parallel_y=vi_parallel_y
            vf_prependicular_x=-vi_prependicular_x
            vf_prependicular_y=-vi_prependicular_y
            
            vf_x_b=vf_parallel_x+vf_prependicular_x
            vf_y_b=vf_parallel_y+vf_prependicular_y
            return[vf_x_a,vf_y_a,vf_x_b,vf_y_b]
        if self.y_b[-1]<=-self.alpha*r:
            cos_theta=self.x_b[-1]/r
            sin_theta=(self.y_b[-1]+self.alpha*r)/r
            
            vi_prependicular_x=abs(self.vx_b[-1]*cos_theta+self.vy_b[-1]*sin_theta)*cos_theta
            vi_prependicular_y=abs(self.vx_b[-1]*cos_theta+self.vy_b[-1]*sin_theta)*sin_theta
            vi_parallel_x=self.vx_b[-1]-abs(self.vx_b[-1]*cos_theta+self.vy_b[-1]*sin_theta)*cos_theta
            vi_parallel_y=self.vy_b[-1]-abs(self.vx_b[-1]*cos_theta+self.vy_b[-1]*sin_theta)*sin_theta    
            
            vf_parallel_x=vi_parallel_x
            vf_parallel_y=vi_parallel_y
            vf_prependicular_x=-vi_prependicular_x
            vf_prependicular_y=-vi_prependicular_y
            
            vf_x_b=vf_parallel_x+vf_prependicular_x
            vf_y_b=vf_parallel_y+vf_prependicular_y
            return[vf_x_a,vf_y_a,vf_x_b,vf_y_b]
        if  -self.alpha*r<self.y_b[-1]<self.alpha*r:
            vf_x_b=-self.vx_b[-1]
            vf_y_b=self.vy_b[-1]
            return[vf_x_a,vf_y_a,vf_x_b,vf_y_b]
    def new_movement2(self,vi_x_a,vi_y_a,vi_x_b,vi_y_b):       
        for i in range(self.steps):                        
            self.vx_a.append(vi_x_a)
            self.vy_a.append(vi_y_a)
                
            self.x_a.append(self.x_a[-1]+self.vx_a[-1]*self.dt/1)
            self.y_a.append(self.y_a[-1]+self.vy_a[-1]*self.dt/1)
            self.T_a.append(self.T_a[-1]+self.dt)
            
            if self.y_a[-1]>=self.alpha*r:
                if (self.y_a[-1]-self.alpha*r)**2+self.x_a[-1]**2>r**2:
                    break
            if   -self.alpha*r<=self.y_a[-1]<=self.alpha*r:
                if self.x_a[-1]>r or self.x_a[-1]<-r:
                    break
            if  self.y_a[-1]<=-self.alpha*r:
                if ((self.y_a[-1]+self.alpha*r)**2+self.x_a[-1]**2)>r**2:
                    break
        self.x_a[-1]=self.x_a[-2]#To imporve the accuracy near the boundary
        self.y_a[-1]=self.y_a[-2]     
        for i in range(self.steps):
            self.vx_a.append(vi_x_a)
            self.vy_a.append(vi_y_a)
            
            self.x_a.append(self.x_a[-1]+self.vx_a[-1]*self.dt/self.accuracy)
            self.y_a.append(self.y_a[-1]+self.vy_a[-1]*self.dt/self.accuracy)
            if self.y_a[-1]>=self.alpha*r:
                if (self.y_a[-1]-self.alpha*r)**2+self.x_a[-1]**2>r**2:
                    break
            if   -self.alpha*r<=self.y_a[-1]<=self.alpha*r:
                if self.x_a[-1]>r or self.x_a[-1]<-r:
                    break
            if  self.y_a[-1]<=-self.alpha*r:
                if ((self.y_a[-1]+self.alpha*r)**2+self.x_a[-1]**2)>r**2:
                    break
            self.T_a.append(self.T_a[-1]+self.dt)
        ###
        for i in range(self.steps):                        
            self.vx_b.append(vi_x_b)
            self.vy_b.append(vi_y_b)
                
            self.x_b.append(self.x_b[-1]+self.vx_b[-1]*self.dt/1)
            self.y_b.append(self.y_b[-1]+self.vy_b[-1]*self.dt/1)
            
            
            if self.y_b[-1]>=self.alpha*r:
                if (self.y_b[-1]-self.alpha*r)**2+self.x_b[-1]**2>r**2:
                    break
            if   -self.alpha*r<=self.y_b[-1]<=self.alpha*r:
                if self.x_b[-1]>r or self.x_b[-1]<-r:
                    break
            if  self.y_b[-1]<=-self.alpha*r:
                if ((self.y_b[-1]+self.alpha*r)**2+self.x_b[-1]**2)>r**2:
                    break
            self.T_b.append(self.T_b[-1]+self.dt)
        self.x_b[-1]=self.x_b[-2]#To imporve the accuracy near the boundary
        self.y_b[-1]=self.y_b[-2]     
        for i in range(self.steps):
            self.vx_b.append(vi_x_b)
            self.vy_b.append(vi_y_b)
            
            self.x_b.append(self.x_b[-1]+self.vx_b[-1]*self.dt/self.accuracy)
            self.y_b.append(self.y_b[-1]+self.vy_b[-1]*self.dt/self.accuracy)
            if self.y_b[-1]>=self.alpha*r:
                if (self.y_b[-1]-self.alpha*r)**2+self.x_b[-1]**2>r**2:
                    break
            if   -self.alpha*r<=self.y_b[-1]<=self.alpha*r:
                if self.x_b[-1]>r or self.x_b[-1]<-r:
                    break
            if  self.y_b[-1]<=-self.alpha*r:
                if ((self.y_b[-1]+self.alpha*r)**2+self.x_b[-1]**2)>r**2:
                    break
            self.T_b.append(self.T_b[-1]+self.dt)
    def show(self):
       distance=[]
       for i in range(len(self.T_a)):
            distance.append(math.sqrt((self.x_a[i]-self.x_b[i])**2+(self.y_a[i]-self.y_b[i])**2))
       
       pl.semilogy(self.T_a,distance,label='$\\alpha=%.4f$'%self.alpha)
       pl.legend(loc='lower right',frameon = True,fontsize='small')
       pl.title('Stadium Divergence,Intial divegence is %.4f($m$)'%distance[0])
       pl.show()


