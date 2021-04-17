import numpy as np
from ecln import calc_ecl

def lu_decomp(m):
    def calc_row(sol_vec,u_vec,const):
        sol = (const-np.dot(sol_vec,u_vec[:-1]))/u_vec[-1]
        return sol
    u = calc_ecl(m)
    u_t = (np.copy(u)).transpose()
    lt = []
    for mat_vec in m:
        sol_vec = []
        for i in range(0,3):
            sol_vec.append(calc_row(sol_vec,u_t[i,:i+1],mat_vec[i]))
        lt.append(sol_vec)
    return(np.asarray(lt),u)

m = np.asarray([[2.0,3.0,-4.0],[1.0,5.0,-1.0],[3.0,7.0,-3.0]])
l , u = lu_decomp(m)
print('lower triangle:\n',l)
print('upper triangle:\n', u)

