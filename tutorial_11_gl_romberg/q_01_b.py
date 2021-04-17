import numpy as np
from q_01 import romberg_mat , tabulate


n_max , m_max = 20,20
e = 1e-8

def f_b(k):
    def f(x):
        if(np.sin(x)==1):
            val = 0
        else:
            val=1/((1-k*(np.sin(x))**2)**0.5)
        return val
    return f

k = np.linspace(0,0.99 , 10)
for k_val in k:
    res = romberg_mat(f_b(k_val),0,np.pi/2,m_max,n_max,e)
    print(res , '\n' , res[-1,-1])

'''
tabulate(romberg_mat(f_b(0.8) , 0, np.pi/2,n_max,m_max,e))
#print(f_b(1)(np.pi/2))
'''
