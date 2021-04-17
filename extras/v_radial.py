import numpy as np
import matplotlib.pyplot as plt



a = 0.05e14
p = 5*365*24*60*60
e =0.7
omega = np.radians(60)
theta = np.radians(np.linspace(0,720,1000))

'''
theta =90
#t1 = a^2*e*np.cos(theta)*np.sin(theta+omega)*2*np.pi*(1/(p*np.sqrt(1-e**2)))
t2 = a*(1-e**2)*((np.cos(theta))/(1+e*np.cos(theta)))

vr = t2

'''
ecc =[0,0.2,0.5,0.7,0.9]
omega = np.radians(90)
for e in ecc:
    vr2 = e*np.cos(omega)+np.cos(omega+theta)
    coeff = (2*np.pi*a)/(p*np.sqrt(1-e**2))
    vr2 = vr2*coeff
    plt.plot(theta, vr2)

#plt.plot(theta,vr1)
#plt.plot(theta,vr2)
plt.show()