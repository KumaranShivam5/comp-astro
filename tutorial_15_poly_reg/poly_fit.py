import numpy as np 
from matplotlib import pyplot as plt
from matplotlib import gridspec as gs 
plt.rcdefaults()
#plt.style.use('seaborn-whitegrid')
plt.style.use('seaborn-dark-palette')



from linear_solver_v2 import solve_mat_eqn
from mat_multiply import m_multiply




data = np.loadtxt('data2')
x = data[:,0]
y = data[:,1]
sigma = data[:,2]



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

    if(print_all):
        print('Polynomial of degree : ', order-1)
        print('______________________________')
        print('\nparameters:')
        print(params)
        print('\nErrors:')
        print(p_err)
        print('______________________________')
        print('Chi sq = %.4f' %chi_sq)
        print('Reduced Chi sq = %.4f' %red_chi_sq) 

    #Plot title and text generation
    if(plot_all):
        title = 'y='
        textbox = '$\chi^2 = {:.4f}$'.format(chi_sq)+'\n$\chi^2/dof = {:.4f}$\n'.format(red_chi_sq)
        for i in range(0,order):
            if(i==0):
                title += '$a_'+str(i)+'x^'+str(i)+'$'
            else:
                title += '+$a_'+str(i)+'x^'+str(i)+'$'
            textbox += '\n$a_'+str(i)+' = {:.4f} \pm {:.4f}$'.format(params[i] , p_err[i]) 

        fig = plt.figure(figsize=(8,6))
        spec = gs.GridSpec(nrows=2, ncols = 1 , height_ratios=[1,0.2] , hspace=0)
        ax = fig.add_subplot(spec[0,0])
        ax.errorbar(x,y,yerr=sigma , fmt= '.' , capsize = 2)
        #ax.set_title('Model')
        ax.set_ylabel('y')
        ax.plot(x,y_mod)
        ax.legend([title , 'given data'])

        #ax.text(0,-20 ,  ,bbox = {'facecolor':'blue' , 'alpha':0.2} , fontsize = 10)
        pad = 0
        ax.text(0,np.amin(y) , textbox ,bbox = {'facecolor':'blue' , 'alpha':0.2 } , fontsize = 10)
        #plt.style.use('bmh')
        res_plot = fig.add_subplot(spec[1,0],sharex=ax)
        res_plot.errorbar(x,residuals , yerr=sigma , fmt='.' , color='k' , capsize = 2)
        res_plot.set_ylabel('residuals')
        res_plot.set_xlabel('x')
        res_plot.axhline(np.mean(residuals) , linewidth=0.5)
        plt.show()
        #print(y_mod)



#analysis(2 , print_all=1 , plot_all=True)
analysis(3 , print_all=1 , plot_all=True)
#analysis(4 , print_all=1 , plot_all=True)
#analysis(5 , print_all=1 , plot_all=True)

