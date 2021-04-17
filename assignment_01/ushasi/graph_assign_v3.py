import numpy as np
import math as m
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#set figure style and figure customisation
plt.style.use('dark_background')
fig = plt.figure(figsize=(10,10))
plt.gca().set_aspect('equal', adjustable='box')


#set mass ratio
massr = int(input("enter mass ratio: "))
m1 = 1
m2 = massr

#add some customisations for better visibility
if(massr>10000):
    s1=5
    dist=100
elif(massr>100):
    s1=10
    dist=100
elif(massr>9):
    s1=50
    dist=150
else:
    s1=70
    dist=200
    
#set distance and size ratios
r1 = int(m2*dist/(m1+m2))
r2 = int(m1*dist/(m1+m2))
s2 = int((m2/m1)**(1/3)*s1)

#theta array
th = np.linspace(-m.pi,m.pi,int(1000))

#set artists for planet 1,2 and crosshair
l1, = plt.plot([],[],'gray',marker=".", markersize=s1)
l2, = plt.plot([],[],'gray',marker=".", markersize=s2)
complot, = plt.plot([],[],'red',marker="+", markersize=20)

#initialise animation
def init():
    return l1, l2, complot,

#stuff that needs to be updated in animation loop
def run(th2):
    x1 = r1*np.cos(th2-m.pi)
    y1 = r1*np.sin(th2-m.pi)
    x2 = r2*np.cos(th2)
    y2 = r2*np.sin(th2)
    l1.set_data(x1,y1)
    l2.set_data(x2,y2)
    complot.set_data(0,0)
    return l1, l2, complot,

#animation function    
ani = animation.FuncAnimation(fig, run, init_func = init, interval=1, frames=th, blit=True)
#static orbits
plt.plot(r1*np.cos(th), r1*np.sin(th),'r-')
plt.plot(r2*np.cos(th), r2*np.sin(th),'r-')

plt.show()
