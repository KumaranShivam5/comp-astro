import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from matplotlib import style as st
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation


phi_p = np.radians(180)
phi_s = 0


theta = np.radians(np.linspace(0, 360,360,endpoint=True))

a = 1
m_c_p = 1 #mass constant for planet taken Unity
m_c_s = 10 #float(input('Enter Mass of star:(assuming mass of planet unity):'))


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

st.use('dark_background')
fig = plt.figure(1, figsize=(12,12))
ax = plt.gca()
ax.set_xlim(-1.2*a,1.2*a)
ax.set_ylim(-1.2*a,1.2*a)
ax.set_aspect(1)
ax.axis('off')

def init():
    plt.plot([0],[0],'+r',markersize=50,zorder=3) # center of mass
    plt.plot(orb_p[0],orb_p[1] ,'-r', markersize=m_p,zorder=0) #planet orit
    plt.plot(orb_s[0],orb_s[1],'-r', markersize=m_s,zorder=0) # star orbit
    #plt.show()


planet, = plt.plot([],[],'w.',markersize=m_p,zorder=3)
star, = plt.plot([],[],'w.',markersize=m_s,zorder=3)
planet_center, = plt.plot([],[],'y+',markersize=10,zorder=3)
star_center, = plt.plot([],[],'y+',markersize=10,zorder=3)


def move(i):
    planet.set_data(orb_p[0][i],orb_p[1][i])
    star.set_data(orb_s[0][i],orb_s[1][i])
    planet_center.set_data(orb_p[0][i],orb_p[1][i])
    star_center.set_data(orb_s[0][i],orb_s[1][i])





Writer = animation.writers['ffmpeg']
writer = Writer(fps=30, metadata=dict(artist='Me'), bitrate=1800)

sim_animation = FuncAnimation(fig,move,[i for i in range(len(theta))],init_func=init,interval=0.1)

plt.show()
'''
ch = 'S' #str(input('Display Plot or Save Plot : [D/S]:'))
if(ch=='D'):
    plt.show()
elif(ch=='S'):
    #matplotlib.use("Agg")
    sim_animation.save('ratio_'+str(m_c_s)+'.gif', writer=writer)

'''