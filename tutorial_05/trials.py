import numpy as np

def chk(a,z):
    t = np.where(a%2==1,0,np.where(z%2==0,12.0,-12.0))
    print(t)

chk(1,2)
chk(1,1)
chk(2,1)
chk(2,4)

