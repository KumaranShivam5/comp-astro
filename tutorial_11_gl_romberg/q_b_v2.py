import numpy as np
from matplotlib import pyplot as plt
def trans_f(f, a, b):
    #val = 0.5*(np.exp((-0.25)*((x+1)**2)))
    m = (b-a)/2
    c = (b+a)/2
    def f_mod(x):
        val = ((b-a)/2)*f(m*x+c)
        #print(val)
        return val
    return f_mod


#-------------------------------------
#Gauss weights and roots
#x,w = np.polynomial.legendre.leggauss(2)
#print(x,w)
#_______________________________________

def calc_gauss(f ,a,b , N):
    x,w = np.polynomial.legendre.leggauss(N)
    val = [trans_f(f,a,b)(x_n) for x_n in x]
    return(np.dot(val ,w))
#    print(len(val))
#    print(len(w[n]))


##__________________________________________
# Our function defiitions
def f_a(x):
    val = np.exp(-1*x**2)
    return val

def f_b(k):
    def f(x):
        val=1/((1-k*(np.sin(x))**2)**0.5)
        return val
    return f

def analysis(f,a,b):
    err = 1
    prev = calc_gauss(f,a,b,1)
    i = 2
    while(err>1e-7):
        nxt = calc_gauss(f,a,b,i)
        err = abs(prev-nxt)
        prev = nxt
        i+=1
        print(err)

#analysis(f_a,0,2)
analysis(f_b(0.9) , 0 ,np.pi/2)
#calc_gauss(f_a,0,2,20)
#calc_gauss(f_a,0,2,2)
#calc_gauss(f_a,0,2,3)
#calc_gauss(f_a,0,2,4)
#calc_gauss(f,0,2,2)
#calc_gauss(f_b(0.5) , 0 ,1,2)

