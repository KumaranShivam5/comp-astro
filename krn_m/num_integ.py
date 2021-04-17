def reimann(f,a,b,h,sum_order =1):
    '''
    return reimann integral for function f
    lower limit a , upper limit b, resolution h
    return lower sum, middle sum and higher sum
    
    '''
    s_m,s_l,s_h,x_a =0,0, 0,a
    while(x_a<=b):
        s_m += h*f(x_a+(h/2))
        s_l += h*f(x_a)
        s_h += h*f(x_a+h)
        x_a+=h 
    s = [s_l,s_m,s_h]
    return (s[sum_order])


'''


### checking accurcy
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return(np.sin(x))

def int_f(x):
    return reimann(f,0, x,0.001)[1]

x = (np.linspace(0,10,100))
y_int = [int_f(x) for x in x]
y = [f(x) for x in x]

y_true = [(1-np.cos(x)) for x in x]

res = [y1-y2 for y1,y2 in zip(y_int,y_true)]

plt.plot(x, y)
plt.plot(x, y_int)
plt.plot(x, y_true)
plt.plot(x,res)
plt.legend(['derivative','calc','true','res'])
plt.show()

'''