import numpy as np
from q_01 import romberg_mat , tabulate


n_max , m_max = 7,7


def f(x):
    val = np.exp(-1*x**2)
    return val

res  = romberg_mat(f,0,1,6,6,1e-8)
#print(res)


tabulate(res)