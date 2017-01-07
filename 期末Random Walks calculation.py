###############################################
#Random Walks
import matplotlib.pyplot as pl
import numpy as np
import math
import random
import mpl_toolkits.mplot3d

class RandomWalk(object):
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
        self.direction=0
    def Move(self):
        if self.direction==1:
            self.x=self.x+3
        if self.direction==-1:
            self.x=self.x-1
        ''' 
        if self.direction==2:
            self.y=self.y+random.randint(-1,1)
        if self.direction==-2:
            self.y=self.y+random.randint(-1,1)
          
        if self.direction==3:
            self.z=self.z+random.randint(-1,1)
        if self.direction==-3:
            self.z=self.z+random.randint(-1,1)
        '''
        s=random.randint(0,1000)
        if s>500:
            self.direction=1
        if s<=500:
            self.direction=-1
        '''        
        if 0<s<=300:
            self.direction=2
        if -30<s<=0:
            self.direction=-2
        if -300<s<=-600:
            self.direction=3
        if s<-600:
            self.direction=-3
        '''
        
        m=[self.x,self.y,self.z]
        return m

#Part of the command
####################################################################################
#Plot the <x^2> versus time plot(you may need to change the direction with 2D to 1D)
'''
n2=0
xlist=[]
averagenumber=500
while n2<100:
    count=0
    tmp=[]
    while count<averagenumber:
        a=RandomWalk(0,0,0)
        n=0
        x=[0]
        while n<n2:
           b=a.Move()
           x.append(b[0])
        
        
           n+=1 
        tmpx=x[-1]**2
        tmp.append(tmpx)
        count+=1
    xaverage=sum(tmp)/averagenumber
    xlist.append(xaverage)
    
    n2+=1
pl.plot(np.linspace(1,len(xlist),len(xlist)),xlist,'.',label='Left Step Length = $3(m)$')
#pl.plot([0,100],[0,100],'k')
#pl.plot([0,100],[0,63],'k')
pl.xlabel('Step Number')
pl.ylabel('$<x^2>$')
#pl.title('Random Walk In One Dimension')
pl.grid(True) 
pl.legend(fontsize='small')
'''
##############################################################################################
#Plot the random walk plot in 3D                    
''' 
a=RandomWalk(0,0,0)
x=[0]
y=[0]
z=[0]
n=0
while n<5000:
    b=a.Move()
    x.append(b[0])
    y.append(b[1])
    z.append(b[2])
    n+=1
ax=pl.subplot(111,projection='3d')
ax.scatter(x, y, z,'1',cmap=pl.cm.coolwarm,c=u'g',marker=u'.',label='Step=%d'%(len(x)-1))
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
pl.title('Random For Three Dimension')
pl.grid(True) 
pl.legend(fontsize='small')
'''
##############################################################################################
##############################################################################################
#Plot the random walk plot in 2D                    
'''    
a=RandomWalk(0,0)
x=[0]
y=[0]
n=0
while n<10000:
    b=a.Move()
    x.append(b[0])
    y.append(b[1])
    print x[-1]
    n+=1
pl.subplot(224)
pl.plot(x,y,label='Step=%d'%(len(x)-1))
n2=np.linspace(1,len(x),len(x))
pl.xlabel('X')
pl.ylabel('Y')
#pl.title('Random For One Dimension')
pl.grid(True) 
pl.legend(fontsize='small')
'''
##############################################################################################
#Plot the random walk plot in 1D                    
'''     
a=RandomWalk(0,0)
x=[0]
n=0
while n<1000:
    b=a.Move()
    x.append(b[0])
    n+=1
pl.subplot(224)
n2=np.linspace(1,len(x),len(x))
pl.plot(n2,x,'.',label='Step=%d'%(len(x)-1))
n2=np.linspace(1,len(x),len(x))
#pl.xlabel('Step Number')
pl.ylabel('x')
#pl.title('Random For One Dimension')
pl.grid(True) 
pl.legend(fontsize='small')
'''
###########################################################################################