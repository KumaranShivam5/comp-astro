import numpy as np
from ecln import calc_ecl

def calc_row_sol(mat_vec,sol_vec):
    sol = (mat_vec[-1] - np.dot(mat_vec[1:-1],sol_vec))/mat_vec[0]
    return(sol)

def solve_mat_eqn(m,b_vec):
    
    if(np.shape(m)[0]!=len(b_vec)):
        raise ValueError('Matrix and vector dim mismatch')
    else:
        mat_given = np.column_stack((m,b_vec))
        mat = calc_ecl(mat_given)
        sol_vec = []
        for i in reversed(range(np.shape(mat)[0])):
            sol_vec.insert(0,calc_row_sol(mat[i,i:],sol_vec))
        return(sol_vec)
