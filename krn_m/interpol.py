import numpy as np

def linear(x,x1,y1,x2,y2):
    y = (x-x1)*((y1-y2)/(x1-x2))+y1
    return (y)

def lagrange(x,x_s,y_s):
    return sum([yj*np.prod([(x-xi)/(xi-xj) for xi in x_s if xi!=xj]) for xj,yj in zip(x_s,y_s)])

'''
#example use

import numpy as np
from matplotlib import pyplot as plt

def f(x):
    return (np.sqrt(np.sin(x)**2))
x = np.linspace(0,10,500)
y = f(x)

xs = x[::20]
ys = y[::20]

yl = [lagrange(x,xs,ys) for x in x[100:400]]
plt.plot(x,y,'+')
plt.plot(xs,ys,'o')
plt.plot(x[100:400],yl)
plt.show()

'''