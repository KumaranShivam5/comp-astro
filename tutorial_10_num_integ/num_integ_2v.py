from math import asin
from matplotlib import pyplot as plt
import numpy as np

def integral(f,a_0,b_0,n,kind='simp'):
    h = (b_0-a_0)/n
    t0 = f(a_0)+f(b_0)

    if (kind=='simp'):
        t1 = sum([f(a_0+h*(2*k-1)) for k in range(1,int(n/2)+1)])
        t3 = sum([f(a_0+h*(2*k)) for k in range(1,int(n/2))])
        val = (h/3)*(t0+4*t1+2*t3)
    if(kind=='tpz'):
        t1 = sum([f(a_0+k*h) for k in range(1,n)])
        val = (h/2)*(t0+2*t1)
    return(val)


########-------------------------------------------------------
#########-------------------------------------------------------

def f1(x):
    return ((1-x**2)**0.5)

def f2(x):
    if(x!=0):
        val = 1/(x**0.5)
    else:
        val=0
    return(val)

def f3(y,):
    def f3_a(x):
        return (x)
    return (y**2)*integral(f3_a,0,2,2,'tpz')
    
def integ_f1(a,b):
    fa = 0.5*(asin(a))+0.5*(a*((1-a**2)**0.5))
    fb = 0.5*(asin(b))+0.5*(b*((1-b**2)**0.5))
    return (fb-fa)

def integ_f2(a,b):
    fa = 2*(a**0.5)
    fb = 2*(b**0.5)
    return(fb-fa)

def integ_f3(a,b):
    def integ_f3_x(xa,xb):
        fa=(xa**2)/2
        fb = (xb**2)/2
        return(fb-fa)
    return ((b**3)/3-(a**3))*integ_f3_x(0,2)

###______________________________________________________________

def do_analysis(f,integ_f,a,b,acc = 0.01):
    n_max = 1000
    t = integ_f(a,b)
    f_approx_simp = [integral(f,a,b,i,kind='simp') for i in range(2,n_max,2)]
    f_approx_tpz = [integral(f,a,b,i,kind='tpz') for i in range(1,n_max,1)]
    f_error_simp = [abs((f_val-t)/t)*100 for f_val in f_approx_simp]
    f_error_tpz = [abs((f_val-t)/t)*100 for f_val in f_approx_tpz]
    print(f_error_simp[-1] , f_error_tpz[-1]) 
    index_simp =[i for i in range(2,n_max,2)] 
    index_tpz =[i for i in range(1,n_max,1)] 
    step_size_simp = (b-a)/np.array(index_simp)
    step_size_tpz = (b-a)/np.array(index_tpz)
    plt.style.use('seaborn-darkgrid')
    plt.xlabel('Step Size')
    plt.ylabel('Error percentage')
    plt.plot(step_size_simp , f_error_simp)
    plt.plot(step_size_tpz , f_error_tpz)
    plt.legend(['Simpson ','Trapezoidal'])
    #plt.savefig('Problem_{}.png'.format(f1))
    plt.show()

def analysis_simp(f,integ_f,a,b,acc=0.01):
    n_max = 10000000
    n=2
    err=1
    index = []
    f_err = []
    t = integ_f(a,b)
    while((err-acc)>1e-5 and n<n_max):
        approx = integral(f,a,b,n,kind='tpz')
        index.append(n)
        err = abs((approx-t)/t)*100
        f_err.append(err)
        n+=1000 # keep this even number 
    print((index[-1]))
    print(f_err[-1])


do_analysis(f3,integ_f3,0,1)
#analysis_simp(f1,integ_f1,-1,1)
#analysis_simp(f2,integ_f2,0,2)
#analysis_simp(f3,integ_f3,0,1)
#do_analysis(f2,integ_f2,0,2)
#do_analysis(f3,integ_f3,0,1)