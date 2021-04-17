import numpy as np 
from matplotlib import pyplot as plt
from matplotlib import gridspec as gs 


from linear_solver_v2 import solve_mat_eqn
from mat_multiply import m_multiply



def poly(x,a):
    val = sum([a[j]*(x**(j)) for j in range(1,len(a))])
    return val



def regression(x,y,sigma,order):
    A = []
    for i in range(len(x)):
        temp = [(x[i]**j)/(sigma[i]) for j in range(order)]
        A.append(temp)
    A = np.asarray(A)
    b = np.asarray([y_i/sigma_i for y_i,sigma_i in zip(y,sigma)])
    b = np.reshape(b , (len(b),1))
    alpha = m_multiply(A.T , A)
    beta = m_multiply(A.T ,b)
    var_params = [alpha[i][i] for i in range(len(alpha))] 
    params = np.asarray(solve_mat_eqn(alpha ,beta))
    cov_mat = np.asarray(np.linalg.inv(alpha))
    return params , cov_mat

def cal_chi(y,y_mod,sigma):
    y_mod = poly(x , params)
    residuals = y_mod - y
    chi_sq_arr = [((y[i]-y_mod[i])**2)/(sigma[i]**2) for i in range(len(y))]
    chi_sq = sum(chi_sq_arr)
    print('Chi sq = ' , chi_sq)
    dof = len(y)-len(params)
    red_chi_sq = chi_sq/dof
    print(red_chi_sq) 



def analysis(order , print_all =True, plot_all=True):

    '''
    - Parameters
        - order - order of polyomial to be fitted , example 3 for quadratic
        - print_all : set True to print the result
        - plot_all : set True to plot the results
    
    '''

    params , cov = regression(x,y,sigma,order)
    p_err = np.asarray([cov[i][i]**0.5 for i in range(len(cov))])
    np.set_printoptions(precision=4)
    y_mod = poly(x , params)
    residuals = y_mod - y
    chi_sq_arr = [((y[i]-y_mod[i])**2)/(sigma[i]**2) for i in range(len(y))]
    chi_sq = sum(chi_sq_arr)
    dof = len(y)-len(params)
    red_chi_sq = chi_sq/dof



