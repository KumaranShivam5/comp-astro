import numpy as np
import matplotlib.pyplot as plt

e = 1
a = 1 
p = 1

theta = np.arange(0,np.pi,0.01)
x = [(p*e)/(1+p*e*np.cos(th))*np.cos(theta) for th in theta]
y = [(p*e)/(1+p*e*np.cos(th))*np.sin(theta) for th in theta]
r = [x**2+y**2 for (x,y) in zip(x,y)]
plt.polar(theta,r)
plt.scatter(y,x)
plt.show()