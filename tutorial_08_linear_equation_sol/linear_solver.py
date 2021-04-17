import numpy as np
from ecln import calc_ecl



m3 = np.asarray([[2.0,3.0,-4.0,12.0],[1.0,5.0,-1.0,12.0],[3.0,7.0,-3.0,20.0]])
print(m3)
sol_vec = []

def calc_row_sol(mat_vec,sol_vec):
    const = mat_vec[-1]
    print(const)
    coeff_vec = mat_vec[1:-1]
    print(sol_vec)
    print(coeff_vec)
    sol = (const - np.dot(coeff_vec,sol_vec))/mat_vec[0]
    return(sol)
'''

i = 0

print(ecl_m)
mat_vec = ecl_m[i,i:]
print(mat_vec)
sol_vec = np.asarray([1,2])

print(calc_row_sol(mat_vec,sol_vec))

sol_vec = []
'''
ecl_m = calc_ecl(m3)

def solve_mat_eqn(mat):
    sol_vec = []
    print(np.shape(mat))
    for i in reversed(range(np.shape(mat)[0])):
        print(i)
        sol_vec.insert(0,calc_row_sol(mat[i,i:],sol_vec))
    print(sol_vec)

solve_mat_eqn(ecl_m)
