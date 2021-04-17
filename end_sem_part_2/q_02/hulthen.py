import numpy as np 
from linear_solver_v2 import solve_mat_eqn


e2 = -2.0
e4 = -1.5 
e6 = -1.4343 
e8 = -1.4128 
e10 = -1.4031 

const_vec = [e2,e4,e6,e8,e10]

coeff = []
for j in range(1,6):
    c = [(1/(2*j)**i) for i in range(5)]
    coeff.append(c)

coeff = np.asarray(coeff)

solution = solve_mat_eqn(coeff,const_vec) 
eps_inf = solution[0]
print('Epsilon infinity : {:.4f}'.format(eps_inf))
