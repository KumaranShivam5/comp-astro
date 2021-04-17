
import numpy as np
from matplotlib import pyplot as plt 

from interpol import lagrange

h0 = 67.4e3 # in m/s/mpc
c = 3e8 #in m/s


def filled_unive_calc_dl(z):
    val = 2*(c/h0)*(1+z)*(1-np.sqrt(1/(1+z)))
    return val

#creating sample (x,y) for interpolation
z = np.linspace(0,3,11)
dl = filled_unive_calc_dl(z)

# using lagrange interpolation for calculating value of z 
# corresponding to the given dl = 430 Mpc
z_cal = lagrange(430 , dl ,z)
print('Redshift corresponding to {} is : {}'.format(430 , z_cal))
#plt.scatter(z,dl)
#plt.show()