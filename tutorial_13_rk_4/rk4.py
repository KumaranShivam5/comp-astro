import matplotlib.pyplot as plt
import numpy as np


def f(x , y):
    return (x**2)


def rk4(x , x_0 , y_0 , f):

    def rk4_next_val(f,x_0 , y_0 , h):
        f0 = f(x_0,y_0)
        f1 = f(x_0+h/2 ,  y_0+(h/2)*f0)
        f2 = f(x_0+h/2 , y_0+(h/2)*f1)
        f3 = f(x_0+h , y_0+h*f2)
        y_next = y_0+(h/6)*(f0+2*f1+2*f2+f3)
        return y_next

    def calc(h):
        n = int(abs((x_0-x)/h))
        x_next,y_next =x_0, y_0
        for i in range(n):
            #print('itr:',i)
            #print('original:' , y_next , x_next)
            y_next = rk4_next_val(f , x_next , y_next , h)
            x_next += h  
            #print('modified:', y_next , x_next)
        return y_next

    tol = 1e-2
    if(abs((x-x_0))<1e-14):
        #print('inside if')
        return (y_0)
    else:
        h = (x-x_0)/2
        prev = calc(h)
        nxt = calc(h/2)
        err = abs(prev-nxt)
        while(err>tol):
            h = h/2
            prev = nxt
            nxt = calc(h)
        return nxt




def rk4_cp(x , x_0 , y_0 , z_0, f1 , f2 ):

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
            #print('itr:',i)
            #print('original:' , y_next , x_next)
            y_next = rk4_next_val(fy(z_next) , x_next , y_next , h)
            z_next = rk4_next_val(fy(y_next) , x_next , z_next , h)
            x_next += h  
            #print('modified:', y_next , x_next)
        return y_next , z_next

    tol = 1e-2
    if(abs((x-x_0))<1e-14):
        #print('inside if')
        return (y_0)
    else:
        h = (x-x_0)/2
        prev = calc(h)
        nxt = calc(h/2)
        err = abs(prev-nxt)
        while(err>tol):
            h = h/2
            prev = nxt
            nxt = calc(h)
        return nxt




#print(rk4_next_val(f,0,0,5))
#x = np.linspace(-1,1 ,100, endpoint=False)
#y = [rk4(x,1,1/3,f) for x in x]

#plt.plot(x,y)
#plt.show()

#print(rk4(-1,0,0,f))