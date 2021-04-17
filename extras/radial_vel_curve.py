from krn_m.num_integ import reimann
import numpy as np

import matplotlib.pyplot as plt
from matplotlib import style as st


def integ_theta_time(x,e):
    def f(x):
        return (1/((1+e*np.cos(x))**2))
    r = reimann(f,0,x,0.1,sum_order=1)
    return(r)


pi = np.pi 
P = 5*365*24*60*60
a = 0.05*1.49e11*1e-3
inc = np.radians(60)

theta = np.radians(np.linspace(0,720,100,endpoint=True))
eccentricity = [0,0.7]
omega = [0,30,60,90]

#['Solarize_Light2', '_classic_test_patch', 'bmh', 'classic',
#  'dark_background', 'fast', 'fivethirtyeight', 'ggplot', 
# 'grayscale', 'seaborn', 'seaborn-bright', 'seaborn-colorblind', 
# 'seaborn-dark', 'seaborn-dark-palette', 'seaborn-darkgrid', 
# 'seaborn-deep', 'seaborn-muted', 'seaborn-notebook', 'seaborn-paper', 
# 'seaborn-pastel', 'seaborn-poster', 'seaborn-talk', 'seaborn-ticks', 
# 'seaborn-white', 'seaborn-whitegrid', 'tableau-colorblind10']



rows,cols =4,2
#st.use('seaborn-notebook')
fig , ax  = plt.subplots(rows, cols, figsize=(8.5,12), sharex=True)
plt.rcParams.update({'font.size': 10})
i,j=0,0
j=0
for e in eccentricity:
    i=0
    for om in omega:
        time_coeff = (P/(2*pi))*((1-e**2)**(3/2))/(24*60*60)
        time = np.asarray([integ_theta_time(th,e) for th in theta])*time_coeff

        vr = e*np.cos(np.radians(om))+np.cos(np.radians(om)+theta)
        coeff = np.sin(inc)*(2*np.pi*a)/(P*np.sqrt(1-e**2))
        vr = vr*coeff
        plt.rcParams.update({'font.size': 10})
        #plt.rcParams.update({'font.size': 8})
        #_____________________________________________________
        #Toggle these for plotting Radial velocity
        # with respect to theta or time 
        #_____________________________________________________
        ## For TIME plot
        #----------------------------
        #ax[i,j].plot(time,vr)  ## uncomment for time plot
        ax[i,j].hlines(0,xmin=0,xmax=np.amax(np.degrees(theta)),colors='m',linewidth=0.7,linestyle='dashed')
        #---------------------------------------------------
        ## For THETA Plot 
        ax[i,j].plot(np.degrees(theta),vr)
        #-------------------------------------------------------
        ax[i,j].set_title('e = {}, $\omega = {}^o$'.format(e,om))
        i+=1
    j+=1

plt.rcParams.update({'font.size': 12})
#-----------------------------------------------------------------------
#fig.text(0.5, 0.06, 'Time (days)', ha='center', va='center')
fig.text(0.5, 0.06, 'Phase Angle $\theta$ (degree)', ha='center', va='center')
#-----------------------------------------------------------------------
fig.text(0.04, 0.5, 'Radial Velocity ,$V_r^*$ ($km/s$)', ha='center', va='center', rotation='vertical')
fig.suptitle('Synthatic Radial Velocity curves')
plt.savefig('plots/plot_theta.png')
plt.show()


