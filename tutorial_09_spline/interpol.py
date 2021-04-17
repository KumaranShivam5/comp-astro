import numpy as np

def linear(x,x1,y1,x2,y2):
    y = (x-x1)*((y1-y2)/(x1-x2))+y1
    return (y)

def lagrange(x,x_s,y_s):
    return sum([yj*np.prod([(x-xi)/(xi-xj) for xi in x_s if xi!=xj]) for xj,yj in zip(x_s,y_s)])
