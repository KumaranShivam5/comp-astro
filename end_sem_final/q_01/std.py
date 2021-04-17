from matplotlib import pyplot as plt 
import numpy as np 
from scipy.integrate import odeint 
g = -9.8
L = 10/100
def f(u , x):
    return (u[1],(g/L)*np.sin(x))
y0 = [0,0]
xs = np.arange(0, 30 , 0.1)
us = odeint(f, y0, xs)
ys = us[:,0]

def convert_rs(theta):
    if(theta < 360):
        return(theta)
    else:
        theta = theta-360
        convert_rs(theta)

th = [(y) for y in ys]
print(len(th))
print(len(xs))
plt.plot(xs,th)
plt.show()