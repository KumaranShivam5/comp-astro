from math import asin
from matplotlib import pyplot as plt
import numpy as np

def integral(f,a_0,b_0,n,kind='simp'):
    h = (b_0-a_0)/n
    integ = 0
    for i in range(n):
        #print(i)
        a = a_0+i*h
        b = a_0 +(i+1)*h
        if(kind=='simp'):
            integ += (((b-a)/2)/3)*(f(a)+4*(f((a+b)/2))+f(b))
            #print(integ)
        elif(kind=='tpz'):
            integ += ((b-a)/2)*(f(a)+f(b))
    return(integ)

########-------------------------------------------------------

def f1(x):
    return ((1-x**2)**0.5)

def f2_p(x):
    return(2)

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
    
def integ_f2_p(a,b):
    return(2*(b-a))



def integ_f3(a,b):
    def integ_f3_x(xa,xb):
        fa=(xa**2)/2
        fb = (xb**2)/2
        return(fb-fa)
    return ((b**3)/3-(a**3))*integ_f3_x(0,2)


def analysis_simp(f,integ_f,a,b,acc=0.01 , growth = 'const'):
    n_max = int(2**100)
    n=2
    err=1
    index = []
    f_err = []
    t = integ_f(a,b)
    while((err-acc)>1e-6 and n<n_max):
        approx = integral(f,a,b,n,kind='simp')
        index.append(n)
        err = abs((approx-t)/t)*100
        f_err.append(err)
        if (growth=='const'):
            n = n+2 # keep this even number
        if(growth=='exp'):
            n = n*2
        #print(n ,err) 
    return(index,f_err)

def analysis_tpz(f,integ_f,a,b,acc=0.01,growth = 'const'):
    n_max = int(2**60)
    n=1
    err=1
    index = []
    f_err = []
    t = integ_f(a,b)
    while((err-acc)>1e-6 and n<n_max):
        approx = integral(f,a,b,n,kind='tpz')
        index.append(n)
        err = abs((approx-t)/t)*100
        f_err.append(err)
        if (growth=='const'):
            n = n+1 # keep this even number
        if(growth=='exp'):
            n = n*2
        #print(n ,err) 
    return(index,f_err)

#do_analysis(f1,integ_f1,-1,1)
#do_analysis(f2,integ_f2,0,2)
#do_analysis(f3,integ_f3,0,1)

#true value of integral
def analysis(f1,integ_f1,a,b,interval, simp_growth='const'):
    #display the true value of integral
    t = integ_f1(a,b)

    # Diplay values of integral calculated for different intervals

    print('true value of integral:' , t)
    print('Interval , Value_tpz , Err tpz , Value_simp ,  error_simp')
    for n in interval:
        if(n%2==0):
            f_a_simp = integral(f1,a,b,n ,kind ='simp')
            e_simp = 100*abs(f_a_simp-t)/t
            f_a_tpz = integral(f1,a,b,n,kind='tpz')
            e_tpz = 100*abs(f_a_tpz-t)/t
            print('{} \t\t {:.4f} \t {:.4f} \t {:.4f} \t {:.4f}'.format(n , f_a_tpz ,e_tpz , f_a_simp ,e_simp))
        else:
            f_a_tpz = integral(f1,a,b,n,kind='tpz')
            e_tpz = 100*abs(f_a_tpz-t)/t
            print('{} \t\t {:.4f} \t {:.4f}'.format(n , f_a_tpz ,e_tpz))            


    # estimate the percetage of error till error goes to 0.01 percent
    index_simp,err_simp = analysis_simp(f1,integ_f1,a,b , growth=simp_growth)
    print('Simpson: Took {} intervals to converge error to {:.4f}'.format(index_simp[-1],err_simp[-1]))
    index_tpz, err_tpz = analysis_tpz(f1,integ_f1,a,b , growth=simp_growth)
    print('Trapezoidal: Took {} intervals to converge error to {:.4f}'.format(index_tpz[-1],err_tpz[-1]))

    #plotting error vs step size
    step_size_simp = (b-a)/np.array(index_simp)
    step_size_tpz = (b-a)/np.array(index_tpz)
    plt.style.use('seaborn-darkgrid')
    plt.xlabel('Step Size')
    plt.ylabel('Error percentage')
    plt.plot(step_size_simp , err_simp)
    plt.plot(step_size_tpz , err_tpz)
    plt.legend(['Simpson ','Trapezoidal'])
    plt.savefig('Problem_{}.png'.format(f1))
    plt.show()

#analysis(f1,integ_f1,-1,1,np.arange(1,50), simp_growth='const')
#for f2(without transform) we need high computation
#analysis(f2,integ_f2,0,2,np.arange(1,50), simp_growth='exp') 
#analysis(f2_p,integ_f2_p,0,2**0.5,np.arange(1,5), simp_growth='exp')
#analysis(f3,integ_f3,0,1,np.arange(1,50), simp_growth='const')
def f_ps(x):
#    print(x)
    
    return (x/(1-x))**0.5

#print(f_ps(0.1))
#print(integral(f_ps , 0 , 0.9999999999 ,1000 , kind='tpz'))

analysis(f3,integ_f3,0,0.9999999999,np.arange(1,50), simp_growth='const')