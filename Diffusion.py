import numpy as np
import matplotlib.pyplot as pl
from copy import deepcopy
import matplotlib.cm as cm
from mpl_toolkits.mplot3d import Axes3D

def Rho(time):

    x = np.linspace(-50,50,101)
    y = np.linspace(-50,50,101)
    x,y = np.meshgrid(x,y)
    A = np.zeros((101,101))
    A[45:55,50]=1
    B=deepcopy(d)

    for t in range(time):
        for i in range(101):
            for j in range(101):
                if i==0 or i==100 or j==0 or j==100:
                    pass
                else:
                    A[i][j]=0.25*(B[i+1][j] + B[i-1][j] + B[i][j+1] + B[i][j-1])
        B=deepcopy(A)

    for i in range(101):
            for j in range(101):
                if i==0 or i==100 or j==0 or j==100:
                    pass
                else:
                    if A[i][j]==0:
                        A[i][j]=0.25*(B[i+1][j] + B[i-1][j] + B][j+1] + B[i][j-1])

    return x,y,A
#Part of the command
####################################################################################
'''
pl.subplot(111)
x,z=Rho(time)[0],Rho(time)[2]
pl.plot(x,z,'b')
pl.scatter(x,z,s=0.5)
pl.xlabel('x')
#pl.ylabel('Density  $\\rho(x)$')
pl.title('Time Elapse')
pl.ylim(0,1.2)
pl.show()
pl.legend()
'''
'''
x,y,z = Rho(time)[0],Rho(time)[1],Rho(time)[2]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y,z,rstride=4,cstride=4,cmap=cm.coolwarm)
pl.contourf(x,y,z)
pl.colorbar()
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('density')
ax.set_title('Diffusion time t=%d(s)'%time)
pl.xlim(-50,50)
pl.ylim(-50,50)
pl.show()
'''
'''
x,y,z = Rho(time)[0],Rho(time)[1],Rho(time)[2]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z,rstride=4,cstride=4,cmap=cm.coolwarm)
pl.contourf(x,y,z)
pl.colorbar()
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('density')
ax.set_title('Diffusion time t=%d(s)'%time)
pl.xlim(-50,50)
pl.ylim(-50,50)
pl.show()
'''
