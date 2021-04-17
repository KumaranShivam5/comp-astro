import numpy as np

'''
lower and upper triangle decomposition 
using Doolittle's Algorithm
'''

def lu_decomp_doolittle(m):
    m = np.asarray(m)
    n = np.shape(m)[0]
    l = np.zeros((3,3))
    u = np.zeros((3,3))

    for k in range(n):
        for m in range(k,n):
            s = 0
            for j in range(k):
                s += l[k][j]*u[j][m]
            u[k][m] = a[k][m] - s

        for i in range(k,n):
            if(i==k):l[i][k] = 0
            else:
                s = 0
                for j in range(k):
                    s = l[i][j]*u[j][k]
                l[i][k] = (a[i][k]-s)/u[k][k]

    return(np.asarray(l),np.asarray(u))


a = [[2.0,3.0,-4.0],[1.0,5.0,-1.0],[3.0,7.0,-3.0]]
l , u = lu_decomp_doolittle(a)

print('lower:\n' , l)
print('upper:\n', u)
