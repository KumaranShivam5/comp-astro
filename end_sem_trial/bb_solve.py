import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt
data = np.loadtxt('bb_data.csv')
#print(len(data))
#sns.distplot(data , kde = True)
#plt.show()
from utilities import histogram_const_bin

def sort(x):
    return np.sort(x) 


def ne(t , N):
    def ne_(e):
        val = (1/2.40411*(t**3))*(e**2)/(np.exp(e/t)-1)
        return val
    def ne_norm(e):
        norm = N / integral(ne_ , 30 , 1000 , 500) 
        val = norm*(1/2.40411*(t**3))*(e**2)/(np.exp(e/t)-1)
        return val 
    return ne_norm

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


bin_len = 20 
data = sort(data)
binned_data = [data[i*20:(i+1)*20] for i in range(3)]

def cal_chi_sq(t):
    print('____________________')
    chi_sq = []
    for d in binned_data:
        en_min , en_max = d[0] , d[-1]
        th_count = integral(ne(t , 60) , en_min , en_max , 500)
        sigma = np.var(d)
        chi_sq.append(((th_count-20)**2)/(sigma))
        #print(th_count)
    s_chi_sq = sum(chi_sq)
    print(s_chi_sq)
    return s_chi_sq

T = np.arange(20,150 , step = 10)
chi_sq = [[t,cal_chi_sq(t)] for t in T]
print(chi_sq)
