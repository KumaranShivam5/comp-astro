import numpy as np
from ecln import calc_ecl
from linear_solver_v2 import solve_mat_eqn

'''
find upper triangle matrix using Gaussian elimination
now, ith row of lower trianglr matrix will be simply the solution of 
U(transpose)*X = A(ith row)
where A(ith row) is represented as column vector

I am using here the linear equation solving problem
developed in previous exercise.
'''

def lu_decomp(m):
    u = calc_ecl(m)
    u_t = (np.copy(u)).transpose()
    l = [solve_mat_eqn(u_t,m_vec) for m_vec in m]
    return(np.asarray(l),u)

m = np.asarray([[2.0,3.0,-4.0],[1.0,5.0,-1.0],[3.0,7.0,-3.0]])
l , u = lu_decomp(m)
print('lower triangle:\n',l)
print('upper triangle:\n', u)

