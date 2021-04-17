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


### including end points
x_s_end_inc = np.append(x[::10],x[len(x)-1])
y_s_end_inc = np.append(y[::10],y[len(y)-1])

x_s_end_inc = x[::10]
y_s_end_inc = y[::10]


lx = [lagrange(xp,x_s,y_s) for xp in x]
### this is the anamoly ....inverting this lx would give correct plot..
### i dont know why...still trying to figure out
lx_inv = [-1*lagrange(xp,x_s,y_s) for xp in x]

### but this anamoly does not happen if 
### end point is included
lx_e_i = [lagrange(xp,x_s_end_inc,y_s_end_inc) for xp in x]

plt.plot(x, y,'-k')
#plt.plot(x_s,y_s,'.r') # actual samples
### for this two end alues oscilation was much higher so to make plot clear
## dropping off some of the initial and end points
#plt.plot(x[5:90],lx[5:90],'-g') 
#plt.plot(x[5:90],lx_inv[5:90],'-b')
plt.plot(x,lx_e_i,'-m') ###  sample
#plt.legend(['true function','sampled points','end not inc, not inverted','end not inc, inverted','end point included'])
#plt.show()

f = si.interp1d(x_s_end_inc,y_s_end_inc,kind='cubic')
y_spl = f(x)
plt.plot(x,y_spl,'-b')
plt.show()

