'''
This version make no use of Animation library,
Rather it plots each frames which can later be combined to 
form  gif or video animation
'''



import numpy as np

#import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
from matplotlib import style as st
from matplotlib.animation import FuncAnimation
from os import system as sys

phi_p = np.radians(180)
phi_s = 0


theta = np.radians(np.linspace(0, 360,36,endpoint=True))
a = 1
m_c_p = 1 #mass constant for planet taken Unity
m_c_s = float(input('Enter Mass of star:(assuming mass of planet unity):'))


# scaling factor , as the actual astronomical distance is much large ,
# so for clarity, we need to scale up the size of the bodies
# we will scale up the size of both bodies using this value 
m_scale =  200/m_c_s


m_p = m_scale * m_c_p   #mass of planet
m_s = m_scale * m_c_s   #mass of star




##orbit size of bodies
a_p = np.divide(a*m_s,(m_s+m_p))
a_s = np.divide(a*m_p,(m_s+m_p))

orb_p = [a_p*np.cos(theta + phi_p),a_p*np.sin(theta+phi_p)]
orb_s = [a_s*np.cos(theta + phi_s),a_s*np.sin(theta+phi_s)]
#com_pos = np.divide((m_p*orb_p+m_s*orb_s),(m_p+m_s))


def plot_frame(i):
    plt.plot([0],[0],'+r',markersize=50,zorder=4) # center of mass
    plt.plot(orb_p[0],orb_p[1] ,'-r', markersize=m_p,zorder=0) #planet orit
    plt.plot(orb_s[0],orb_s[1],'-r', markersize=m_s,zorder=0) # star orbit
    plt.plot(orb_p[0][i],orb_p[1][i],'w.',markersize=m_p,zorder=3)
    plt.plot(orb_s[0][i],orb_s[1][i],'w.',markersize=m_s,zorder=3)
    plt.plot(orb_p[0][i],orb_p[1][i],'k+',markersize=10,zorder=3)
    plt.plot(orb_s[0][i],orb_s[1][i],'k+',markersize=10,zorder=3)
    plt.savefig('frames/'+str(i)+'.png')


sys('mkdir frames')

for i in range(len(orb_s[0])):
    st.use('dark_background')
    fig = plt.figure(1, figsize=(12,12))
    ax = plt.gca()
    ax.set_xlim(-1.2*a,1.2*a)
    ax.set_ylim(-1.2*a,2*a)
    ax.set_aspect(1)
    ax.axis('off')
    print('starting plot{}',i)
    plot_frame(i)
    plt.close()