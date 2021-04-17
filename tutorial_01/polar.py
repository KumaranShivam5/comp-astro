import numpy as np
import matplotlib.pyplot as plt

e = [0,0.5,1,3]
a=1

p = np.zeros(len(e))
p[0] = a
p[1] = a*(1-e[1]**2)/e[1]
p[2] = 2*a
p[3] = a*(e[3]**2-1)/e[3]

r= []
theta = np.arange(0,2*np.pi,0.01)
for i in range(len(e)) :
    r = [((p[i]*e[i])/(1-e[i]*np.cos(th))) for th in theta]
    #r= np.ones(len(theta))
    #plt.polar(theta,r)
    #for i in range(len(theta)):
    plt.plot(r*np.cos(theta),r*np.sin(theta))
    #plt.plot()
    plt.show()
#plt.show()