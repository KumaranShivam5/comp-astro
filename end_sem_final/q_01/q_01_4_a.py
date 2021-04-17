import numpy as np 
from ode import euler_cp
from matplotlib import pyplot as plt

def euler_cp(x , x_0 , y_0 , z_0, fy , fz , tol=1e-5):

    def rk4_next_val(f,x_0 , y_0 , h):
        y_next = y_0+h*f(x_0 , y_0 )
        return y_next

    def calc(h):
        n = int(abs((x_0-x)/h))
        x_next,y_next ,z_next = x_0, y_0 , z_0
        for i in range(n):
            y_next = rk4_next_val(fy(z_next) , x_next , y_next , h)
            z_next = rk4_next_val(fz(y_next) , x_next , z_next , h)
            x_next += h              
        return [y_next , z_next]

    del_t = 1e-5
    return calc(del_t)


def rk4_cp(x , x_0 , y_0 , z_0, fy , fz , tol=1e-5):

    def rk4_next_val(f,x_0 , y_0 , h):
        f0 = f(x_0,y_0)
        f1 = f(x_0+h/2 ,  y_0+(h/2)*f0)
        f2 = f(x_0+h/2 , y_0+(h/2)*f1)
        f3 = f(x_0+h , y_0+h*f2)
        y_next = y_0+(h/6)*(f0+2*f1+2*f2+f3)
        return y_next

    def calc(h):
        n = int(abs((x_0-x)/h))
        x_next,y_next ,z_next = x_0, y_0 , z_0
        for i in range(n):
            y_next = rk4_next_val(fy(z_next) , x_next , y_next , h)
            z_next = rk4_next_val(fz(y_next) , x_next , z_next , h)
            x_next += h              
        return [y_next , z_next]

    del_x = 1e-5
    return calc(del_x)




def fy(z):
    def f_in(x , y):
        return z
    return f_in

def fz(y):
    def f_in(x , z):
        return (-g/L)*np.sin(y)
    return f_in

g = 9.8 
L = 10/100

z_0 = 0 
t_0 = 0 


t = np.arange(0, 4 , step = 0.01)
theta_0_collection = np.radians([10 , 45 , 90 , 135])
theta_collection = [t]
 
for theta_0 in theta_0_collection:
    #theta_0  = np.radians(10)
    y_0 = theta_0
    theta = []
    theta_dot = []
    for ti in t:
        soln = rk4_cp( ti , t_0 , y_0 , z_0 , fy , fz)
        t_0 = ti 
        th = soln[0]
        th_dot = soln[1]
        theta.append(th)
        theta_dot.append(th_dot)
        y_0 = th 
        z_0 = th_dot 

    theta_collection.append(theta)

np.savetxt('theta_rk4_all_v2.csv' , theta_collection)

