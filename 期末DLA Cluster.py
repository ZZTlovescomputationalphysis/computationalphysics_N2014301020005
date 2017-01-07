import matplotlib.pyplot as pl
import random
class Particle(object):#def a class"particle"
	direction = 0
	def __init__(self,x,y,state):
		self.x=x
		self.y=y
		self.state=state
	def RandomWalk(self):
             if self.direction==1:
                 self.x+=0.5
             if self.direction==-1:
                 self.x+=-0.5
             if self.direction==2:
                 self.y+=0.5
             if self.direction==-2:
                 self.y+=-0.5
             s=random.randint(-1000,1000)
             if 500<s<=1000:
                 self.direction=1
             if 0<s<=500:
                 self.direction=-1
             if -500<s<=0:
                 self.direction=2
             if -1000<s<=500:
                 self.direction=-2
class screen(object):#def a class"screen"
	Particle_Group=[Particle(50.0,50.0,0)]# To creat a list of exsisting praticle,here the intial praticil at origin x=y=50 was created already
	state=1
	def Test_particle(self,x,y):
		for i in self.Particle_Group:#To testify whether the particle ha already exsist
			if i.x==x and i.y==y:#To go through all the exsisting particle in the screen
				return 1
		return 0
	def addparticle(self,x=65.0,y=65.0):#add a new particle at x=y=65 
		m=self.Test_particle(x,y)
		if self.state==1:#stat=1 means feasible partice while state=0 means unfeasible particle 
			if m==0:
				self.Particle_Group.append(Particle(x,y,1))#If the new adding charge is diffenret from the already exsisting 'lis' charege,then add a new particle to 'lis'
			else:
				print 'same particle'
				self.state=0
		else:
			print 'full screen'
		for a in self.Particle_Group:#Clean out the particle that is out of range of x=y=66 or x=y=34.
			if a.x>66.0 or a.y>66.0 or a.x<34.0 or a.y<34.0:
				self.state=0
		return
	def delparticle(self,x,y):#Delete particle??
		for i in range(len(self.lis)):
			if self.Particle_Group[i].x==x and self.Particle_Group[i]==y:
				self.Particle_Group.pop(i)
				self.state=1
				return
		return
	def showscreen(self):
		x=[]
		y=[]
		for i in self.Particle_Group:
			x.append(i.x)
			y.append(i.y)
		pl.plot(x,y,'r.')
		pl.show()
	def move(self):#random walk of particle
		tmp=self.Particle_Group.pop()#Return the last term in the list 'lis' and delete this term.
		while tmp.state==1 and tmp.x<75.0 and tmp.y<75.0 and tmp.x>=25 and tmp.y>=25:
			m1=self.Test_particle(tmp.x+0.5,tmp.y)
			m2=self.Test_particle(tmp.x-0.5,tmp.y)
			m3=self.Test_particle(tmp.x,tmp.y-0.5)
			m4=self.Test_particle(tmp.x,tmp.y+0.5)
			s=[m1,m2,m3,m4]
			if m1==0 and m2==0 and m3==0 and m4==0:#If the particle does not exsist,then move the particle.
				tmp.RandomWalk()
			elif random.randint(1,100)>85:
				tmp.state=0
			elif m1==1 and m2==1 and m3==1 and 4==1:#If the particle alreadt exsist,then delete the particle.
				tmp.state=0
			else:
				while s[tmp.direction]==1:
					tmp.direction=random.randint(0,3)
				tmp.RandomWalk()
			#print 'move a particle'
			#print t1.x,t1.y
		if tmp.state==0 :
			self.Particle_Group.append(tmp)

##Order Command is not shown here.