import numpy as np
from root_methods import newton_roots, bisect_root

def calc_pos(a,E):
    return((a*np.cos(E),a*np.sin(E)))


def calc_E(t,e,params=False,method=newton_roots):
    def f(x):
        return (omega*t + e*np.sin(x)-x)
    def f_d(x):
        return (e*np.cos(x)-1)
    if(method=='newton'):
        E = newton_roots(f,f_d,10,1e-7,params=params)
    if(method=='bisect'):
        E = bisect_root(f,-10,10,1e-7,params=params)
    return E


def all_calc(e,t,method='newton'):
    E = (calc_E(t,e,params=True,method=method))
    x,y = calc_pos(a,E[0])
    print('Using {} method to calculate roots'.format(method))
    print('\nFor t={} days and Eccentricity = {}'.format(t,e))
    print('E:{},Iteration Counts :{},Fractional Error {}'.format(E[0],E[1],E[2]))
    print("x: {:.4e}, y:{:.4e} \n \n".format(x,y))


T = 365.2635
a = 1.496e16 # actual value of semi major axis for earth is different 1.496e11
omega = 2*np.pi/T
t = [91,182,273]

for days in t:
    all_calc(0.0167,days,method='newton')

for days in t:
    all_calc(0.99999,days,method='newton')

for days in t:
    all_calc(0.0167,days,method='bisect')

for days in t:
    all_calc(0.99999,days,method='bisect')