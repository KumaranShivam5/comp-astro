import numpy as np
import matplotlib.pyplot as plt

a_1 = 15.8
a_2 = 18.3
a_3 = 0.714
a_4 = 23.2

def calc_b(A,Z):
    a_5 = np.where(A%2==1,0,np.where(Z%2==0,12.0,-12.0))
    t_1 = a_1*A 
    t_2 = a_2*(A**(2/3))
    t_3 = a_3*((Z**2)/(A**(1/3)))
    t_4 = a_4*(((A-2*Z)**2)/(A))
    t_5 = a_5/(A**0.5)
    B = t_1-t_2-t_3-t_4+t_5
    return(B)

data = np.loadtxt('atomicdata.txt', skiprows=2,dtype='S5,i8,i8')
data = np.asarray([list(d) for d in data])
name = [n.decode() for n in data[:,0]]
Z = [int(z.decode()) for z in data[:,1]]
A = [int(a.decode()) for a in data[:,2]]
B = [calc_b(a,z) for a,z in zip(A,Z)]
print(name,Z,A)
print(B)
plt.plot(A,B,'-o')
for x,y,n in zip(A,B,name):
    label = n
    plt.annotate(label,(x,y),ha='right')
plt.title('Binding Energy')
plt.xlabel('B (MeV)')
plt.ylabel('A (mass number)')
plt.show()
#plt.subplots(112)

B_a = [b/a for b,a in zip(B,A)]
plt.plot(A,B_a,'-o')
plt.title('Binding Energy per Nucleon')
plt.xlabel('B (MeV)')
plt.ylabel('B/A')
for x,y,n in zip(A,B_a,name):
    label = n
    plt.annotate(label,(x,y),ha='right')
#plt.subplots(212)
plt.show()
#print(data)


