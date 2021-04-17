import numpy as np 
from matplotlib import pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D as ax3d 

t_max , x_max= 48 , 100 
del_t , del_x = 0.5 , 1.0
lt , lx= t_max/del_t , x_max/del_x 
k = 0.1
v = 0.5

u = []

x_grid = np.arange(0,100 , step=del_x)
t_grid = np.arange(0, 48 , step = del_t)

for j in range(len(t_grid)):
    temp = [0]*len(x_grid)
    # boundary conditions
    temp[0] , temp[-1] = 0 , 0
    for i in range(1,len(x_grid)-1):
        if(j==0):
            temp[i] =  np.exp(-0.05*((x_grid[i]-20)**2))
            #initial condition 
        else:
            u_curr = u[j-1]
            term1 = ((k*del_t)/(del_x**2))*u_curr[i+1]
            term2 = -((2*del_t*k)/(del_x**2)+(v*del_t)/(del_x)-1)*u_curr[i]
            term3 = (k+v)*(del_t/(del_x**2))*u_curr[i-1]
            temp[i] = term1+term2+term3 
    u.append(temp)
u = np.asarray(u)
#print(u.shape)
plt.plot(x_grid, u[0])
plt.plot(x_grid, u[int(len(t_grid)/2)])
plt.plot(x_grid , u[-1] , 'k')

plt.show()