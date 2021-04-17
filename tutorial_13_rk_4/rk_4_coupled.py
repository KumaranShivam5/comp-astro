import matplotlib.pyplot as plt

import numpy as np

def rk4_cp(x , x_0 , y_0 , z_0, fy , fz , tol=1e-5):

    def rk4_next_val(f,x_0 , y_0 , h):
        f0 = f(x_0,y_0)
        f1 = f(x_0+h/2 ,  y_0+(h/2)*f0)
        f2 = f(x_0+h/2 , y_0+(h/2)*f1)
        f3 = f(x_0+h , y_0+h*f2)
        y_next = y_0+(h/6)*(f0+2*f1+2*f2+f3)
        return y_next

    def calc(h):
        n = int(abs((x_0-x)/h))
        x_next,y_next ,z_next = x_0, y_0 , z_0
        for i in range(n):
            y_next = rk4_next_val(fy(z_next) , x_next , y_next , h)
            z_next = rk4_next_val(fz(y_next) , x_next , z_next , h)
            x_next += h              
        return y_next , z_next

    if(abs((x-x_0))<1e-14):
        return (y_0 , z_0)
    else:
        h = (x-x_0)/2
        prev = calc(h)
        h = h/2
        nxt = calc(h)
        err1 = abs((prev[0]-nxt[0])/(prev[0]))
        err2 = abs((prev[1]-nxt[1])/(prev[1]))
        i = 0

        while(err1>tol or err2>tol):
            i+=1
            h = h/2
            prev = nxt
            nxt = calc(h)
            err1 = abs((prev[0]-nxt[0])/(prev[0]))
            err2 = abs((prev[1]-nxt[1])/(prev[1]))
        return nxt
    
    #h = -1
    #return calc(h)
'''
# Example Function definition to be used

def fy(param):
    def f_in(x , y):
        return np.sin(param)+x+x**2
    return f_in

def fz(param):
    def f_in(x , y):
        return param*2+x
    return f_in
'''