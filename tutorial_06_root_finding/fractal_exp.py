from root_methods import newton_roots
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return(x**3+1)
def fd(x):
    return(3*x**2)
r = np.arange(0,100)
i = np.arange(0,100)

r = np.linspace(-50,50,num=1500)
i = np.linspace(-10,10,num=300)

1+2j 
type_a = []
type_b = []
type_c = []
for x in r:
    for y in i:
        x_n = x+y*1j
        epsilon = 0.0001
        z = np.round(newton_roots(f, fd, x_n, epsilon, params=False),decimals=3)
        if(z==(0.5+0.866j)):
            type_a.append([x,y])
        elif (z==(-1+0j) or z==(-1-0j)):
            type_b.append([x,y])
        elif (z==(0.5-0.866j)):
            type_c.append([x,y])
        #print(z)

type_a = np.asarray(type_a).transpose()
type_b = np.asarray(type_b).transpose()
type_c = np.asarray(type_c).transpose()
#print(type_a.shape)

plt.plot(type_a[0],type_a[1],'+k', markersize = 1)
plt.plot(type_b[0],type_b[1],'+r', markersize = 1)
plt.plot(type_c[0],type_c[1],'+y', markersize = 1)
plt.xlabel('real(z)')
plt.ylabel('img(z)')
plt.title('initial value leading to cube root of unity')
plt.show()


'''
a_vec = type_a.transpose()
mag_a = [abs(a[0]+a[1]*1j) for a in a_vec]
theta_a = [np.arctan(a[1]/a[0]) for a in a_vec] 
plt.polar(theta_a, mag_a,'+k')

b_vec = type_b.transpose()
mag_b = [abs(b[0]+b[1]*1j) for b in b_vec]
theta_b = [np.arctan(b[1]/b[0]) for b in b_vec] 
plt.polar(theta_b, mag_b,'+r')

c_vec = type_c.transpose()
mag_c = [abs(c[0]+c[1]*1j) for c in c_vec]
theta_c = [np.arctan(c[1]/c[0]) for c in c_vec] 
plt.polar(theta_c, mag_c,'+y')
plt.show()

'''