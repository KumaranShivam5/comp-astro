import numpy as np
from matplotlib import pyplot as plt 
def shift(x,a):
    l = len(x)
    x = np.asarray(x)
    z = np.zeros(abs(a))
    if(a>0):
        x = np.concatenate((z,x))
        x = x[:l]
    else:
        x = np.concatenate((x,z))
        #print(x)
        x = x[abs(a):]
    return x

def dot(v1,v2):
    return sum([x*y for x,y in zip(v1,v2)])

def cross_corr(x,y):
    m ,n = len(x) , len(y)
    if(m>n):
        z = np.zeros(m-n)
        y = np.concatenate((y,z))
    elif(m<n):
        z = np.zeros(n-m)
        x = np.concatenate((x,z))
    m ,n = len(x) , len(y)
    #res = np.zeros(m+n-1)
    res = []
    del_t = []
    for i in range(-n+1,n):
        temp = dot(shift(y,i) , x)
        #print(temp)
        res.append(temp)
        del_t.append(i)
    return res , del_t





def circ_shift(x,a):
    l=len(x)
    if (a>0):
        a = abs(a)
        x = x[(l-a):]+x[:(l-a)]
    if(a<0):
        a = abs(a)
        x = x[a:]+x[:a]
    return x
'''
x = [1,2,3,4,5,6,7,8]
print(circ_shift(x,3))
print(circ_shift(x,-3))
'''
def circ_corr(x , type = 'full'):
    n = len(x) 
    x = np.asarray(x)
    x = x.tolist()
    #res = np.zeros(m+n-1)
    res = []
    del_t = []
    if(type=='half'):
        for i in range(0,n):
            res.append(dot(circ_shift(x , i) , x))
            del_t.append(i)
    if(type=='full'):
        for i in range(-n+1,n):
            res.append(dot(circ_shift(x , i) , x))
            del_t.append(i)
    return res , del_t

'''
x = [1,2,3]

print(auto_corr(x))
'''