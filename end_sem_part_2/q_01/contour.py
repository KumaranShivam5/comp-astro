import numpy as np
from matplotlib import pyplot as plt 


def acc(theta, beta):
    num = 1-beta*np.cos(theta)
    val = 1/(num**3)
    return val 

theta = np.linspace(-np.pi,np.pi, 100)
beta = np.linspace( 0.0 , 0.5, 100)
k = []
for th in theta:
    temp = []
    for bt in beta:
        val = acc(th , bt)
        temp.append(val)
    k.append(temp)

b , t = np.meshgrid(beta, theta)
#theta_deg = np.linspace(-180 , 180 , 18)

fig , ax = plt.subplots(figsize=(8,6))
color_plot = ax.contourf((b), np.degrees(t), np.log(k), 100 , cmap=plt.cm.magma)
line_plot = ax.contour(color_plot, levels=color_plot.levels, colors='cyan' , linewidths=[0.3]*len(color_plot.levels) )
cbar = fig.colorbar(color_plot)
cbar.ax.set_ylabel(r'$Log(\alpha\times|\vec E_{acc}|)$')
y_ticks = ax.get_yticks()
y_ticks = np.append(y_ticks,[90,-90])
ax.set_yticks(y_ticks)
ax.set_ylim(-180,180)
ax.set_xlabel(r'$\beta$')
ax.set_ylabel(r'$\theta (deg)$')

plt.savefig('acc_.png')
plt.show()
#print(k)