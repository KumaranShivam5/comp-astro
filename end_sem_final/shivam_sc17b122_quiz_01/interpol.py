import numpy as np

def lagrange(x,x_s,y_s):
    '''
    for correct interpolation
    Number of samples must be odd
    '''
    return sum([yj*np.prod([(x-xi)/(xi-xj) for xi in x_s if xi!=xj]) for xj,yj in zip(x_s,y_s)])