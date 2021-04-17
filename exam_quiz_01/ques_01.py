from root_methods import newton_roots
import numpy as np
'''
constants
'''

h0 = 67.4e3 # in m/s/mpc
c = 3e8 #in m/s


def calc_z(dl):
    dl = dl 
    def f(x):
        t1 = 2*(c/h0)
        t2 = (1+x)
        t3 = (1-np.sqrt(1/(1+x)))
        return (t1*t2*t3-dl)

    def fd(x):
        val = 2*c/h0*(1-0.5/(np.sqrt(1+x)))
        return(val)
    return(newton_roots(f,fd,1,0.0001,params=False))


print(calc_z(430))


