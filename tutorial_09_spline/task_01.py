import scipy.interpolate as si 
import numpy as np
from interpol import lagrange
import matplotlib.pyplot as plt



def f(x):
    return(1/(25*x**2+1))


x = np.linspace(-1,1,101,endpoint=True)
y = f(x)

x_s = x[::10]
y_s = y[::10]



lx = [lagrange(xp,x_s,y_s) for xp in x]


plt.plot(x, y,'-k')

plt.plot(x,lx,'-m') ###  sample
#plt.legend(['true function','sampled points','end not inc, not inverted','end not inc, inverted','end point included'])

f = si.interp1d(x_s,y_s,kind='cubic')
y_spl = f(x)
plt.plot(x,y_spl,'-b')
plt.legend(['true','lagrange','spline'])
plt.show()

