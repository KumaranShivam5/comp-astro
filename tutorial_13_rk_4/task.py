from rk4 import rk4 
from rk_4_coupled import rk4_cp
import numpy as np
from matplotlib import pyplot as plt 
#constants 
kb = 1.38e-16
me = 9.1e-28
mp = 1.6e-24 
c = 2.988e10
rg = 3e6

def nx(m_dot ,  x):
    denom = 2*np.pi*mp*(rg**2)*c*(x**(3/2))
    val = m_dot/denom
    return val

def lmd(n,te):
    val = (1.4e-27)*(n**2)*(te**0.5)
    #print('lambda:' , val)
    return val

def gamma(n , tp, te ):
    #print(te)
    val = (3.2e-12)*(kb/mp)*(n**2)*(tp-te)*(((me)/(te**3))**0.5)
    #print('Te:' , te)
    #print(val)
    return val

def f_tp_wrap(m_dot):
    def f_tp(te):
        def f_in(x, tp):
            n = nx(m_dot,x)
            g = gamma(n , tp , te)
            term1 = ((4*np.pi*mp*rg**3)/(3*kb*m_dot))*g*(x**2)
            term2 = tp*((3*x-4)/(3*x*(x-1)))
            #print(term1,term2)
            val = term1 - term2
            return val
        return f_in
    return f_tp

def f_te_wrap(m_dot):
    def f_te(tp):
        def f_in(x, te):
            #print(te)
            n = nx(m_dot,x)
            g = gamma(n , tp , te)
            l = lmd(n,te)
            term1 = ((4*np.pi*mp*rg**3)/(3*kb*m_dot))*(g-l)*(x**2)
            term2 = te*((3*x-4)/(3*x*(x-1)))
            #print(term1 , term2)
            val = -term2 -term1
            return val
        return f_in
    return f_te

#print(f_te_wrap(1e17)(1e8)(1e3 , 1e8))
#print(f_te(1e8)(1e3 , 1e8 , 1e17))



#print(rk4_cp(999 , 1e3 , 1e8 , 1e8 , f_tp_wrap(1e17) , f_te_wrap(1e17)))

te_0 = 1e8 
tp_0 = 1e8 
x_0 = 1e3 
m_dot_0 = 1e19
#x = np.linspace(2,1e3 , 100)

#t_q1 = [rk4_cp(x , x_0 , te_0 , tp_0 , f_tp_wrap(m_dot_0) , f_te_wrap(m_dot_0)) for x in x]
data = rk4_cp(2 , x_0 , te_0 , tp_0 , f_tp_wrap(m_dot_0) , f_te_wrap(m_dot_0) )
#t_q1 = np.asarray(t_q1)
print(data)
#plt.loglog(x,t_q1[:,0])