import numpy as np
from root_methods import newton_roots, bisect_root

'''
def f(x):
    return (x**2 - 1/16)

x_a,x_b = 0,1
e = 1e-7
root = bisect_root(f, x_a, x_b, e, params=True)
print(root)


'''
######## q_02------------

def f(x):
    return (np.tan(x)-1/x)

def fd(x):
    return ((1/np.cos(x))**2+1/x**2)
'''
x_a = 1
x_b = 1.7
delta = 0.00001
b = x_a
while(b<=x_b):
    a = b 
    b = b+delta
    sub_interval = a,b
    e = 1e-7
    root = bisect_root(f,sub_interval[0],sub_interval[1],e,params=False)
    print(root)
'''

x_a = np.pi/2
x_b = np.pi/2-0.1
e = 1e-7
#root = bisect_root(f,x_a,x_b,e,params=True)
root = newton_roots(f, fd, x_a, e, params=True)
print(root)


