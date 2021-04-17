import numpy as np
def integral(f,a_0,b_0,n,kind='simp'):
    h = (b_0-a_0)/n
    t0 = f(a_0)+f(b_0)

    if (kind=='simp'):
        t1 = sum([f(a_0+h*(2*k-1)) for k in range(1,int(n/2)+1)])
        t3 = sum([f(a_0+h*(2*k)) for k in range(1,int(n/2))])
        val = (h/3)*(t0+4*t1+2*t3)
    if(kind=='tpz'):
        t1 = sum([f(a_0+k*h) for k in range(1,n)])
        val = (h/2)*(t0+2*t1)
    return(val)


def calc_r(f,a,b,i,j):
    if(j<=i):
        if(j==1):
            #print('calculating: ' , i, j)
            val = integral(f,a,b,int(2**(i-1)), kind='tpz')
            return(val)
        else:
            r_ij =( 4**(j-1)*calc_r(f,a,b,i,j-1) - calc_r(f,a,b,i-1,j-1) ) / (4**(j-1)-1)
        return r_ij
    else:
        print('Wrong indices')
        return(0)


def romberg_mat(f,a,b,m,n,e):
    '''
    f : integrand function
    a,b : integral limits
    m ,n :  maximum order
    e : desired accuracy
    returns: romberg matrix of size corresponding 
            to size computed by 
    '''
    err = 1 
    prev = calc_r(f,a,b,1,1)
    mat = np.zeros((m,n))
    mat[0][0] = prev
    for i in range(2,m+1):
        for j in range(1,i+1):
            nxt = calc_r(f,a,b,i,j)
            mat[i-1][j-1] = nxt
            err = abs(prev-nxt)
            if(err<e):
                print(i,j)
                mat = mat[:i,:j]
                return mat
            else:
                prev = nxt
    raise ValueError('Accuracy could not be achieved with given order limit')



def tabulate(res):
    m , n = res.shape 
    print('\t {}'.format(np.arange(1, n+1)))
    for i in range(0,m):
        print('{} : {}'.format(2**i , res[i]))

#for i in range(1,10):

#    print(calc_r(f,0,1,i,i))

