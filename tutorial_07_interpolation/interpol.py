import numpy as np

def linear(x):
    return ('to do')

def lagrange(x,x_s,y_s):
    return sum([yj*np.prod([(x-xi)/(xi-xj) for xi in x_s if xi!=xj]) for xj,yj in zip(x_s,y_s)])