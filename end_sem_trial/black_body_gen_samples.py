import random as rnd  
import numpy as np 
from matplotlib import pyplot as plt 
import seaborn as sns

rnd.seed(937638923829)

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

def gen_rand_n(x_min ,x_max , n):
    x = []
    n = int(n)
    for i in range(n):
        mu = rnd.uniform(0,1)
        xi = x_min + mu*(x_max-x_min)
        x.append(xi)
    if (len(x)==1):
        return x[0]
    else:
        return x

def gen_samples(f,x_min , x_max , N):
    x_val = np.linspace(x_min, x_max , N)
    y_val = [f(x) for x in x_val]
    #print(y_val)
    y_max = np.amax(y_val)
    x_acc = []
    i = 0
    while(i<N):
        x = gen_rand_n(x_min,x_max,1)
        y = gen_rand_n(0,y_max , 1)
        if(y<=f(x)):
            x_acc.append(x)
            i+=1
    return x_acc



def ne(t , N):
    def ne_(e):
        val = (1/2.40411*(t**3))*(e**2)/(np.exp(e/t)-1)
        return val
    def ne_norm(e):
        norm = N / integral(ne_ , 1 , 4000 , 1000) 
        val = norm*(1/2.40411*(t**3))*(e**2)/(np.exp(e/t)-1)
        return val 
    return ne_norm


N = 60
T = 80
en_min , en_max = 10 , 2000 
en1 = gen_samples(ne(T , N) , en_min , en_max, N)
np.savetxt('bb_data_02.csv' , en1)
sns.distplot(en1 , kde = 1)
plt.show()