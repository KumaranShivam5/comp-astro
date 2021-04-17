import numpy as np

a_1 = 15.8
a_2 = 18.3
a_3 = 0.714
a_4 = 23.2

def calc_b(A,Z):
    a_5 = np.where(A%2==1,0,np.where(Z%2==0,12.0,-12.0))
    return(15.8*A - 18.3*(A**(2/3)) - 0.714*((Z**2)/(A**(1/3))) -a_4*(((A-2*Z)**2)/(A)) +a_5/(A**0.5))


#print(Z[3])
Z = np.arange(1,101)
A = [np.arange(z,3*z+1) for z in Z]
B = [[(calc_b(a,z)/a,a,z) for a in A_l] for A_l,z in zip(A,Z)]
B = np.asarray([val for b in B for val in b])
print(B)
print('Binding Energy(MeV): ',B[np.argmax(B[:,0])][0],"\nA:",B[np.argmax(B[:,0])][1],"\nZ",B[np.argmax(B[:,0])][2])

