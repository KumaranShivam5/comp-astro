import numpy as np
#argument Params is used for getting loop count parameters
def newton_roots(f,fd,x_n,epsilon,params=False):
    i = 0
    x_n1 = x_n - f(x_n)/fd(x_n)
    while (np.abs((x_n1-x_n)/x_n)>=epsilon):
        i+=1
        x_n = x_n1
        x_n1 = x_n1  - f(x_n)/fd(x_n)
    f_err=np.abs((x_n1-x_n)/x_n1)
    if(params):return(x_n1,i,f_err)
    else: return (x_n1)


def bisect_root(f,x_a,x_b,e,params=False):
    x_tol = 1e-10
    y_asm_large = 1e4
    if(f(x_a)*f(x_b)<0):
        i=0
        c = (x_a+x_b)/2
        while((x_b-x_a)>e):
            i+=1
            c = (x_a+x_b)/2
            try:
                x_a,x_b = np.where(f(x_a)*f(c)<0,(x_a,c),(c,x_b))
                if(abs(f(c-x_tol)-f(c+x_tol))>y_asm_large):
                    print('An asymptote')
            except:
                print('Value explode')
                break
        f_err = np.abs((x_b-x_a))
        ## checking asymptote
        if(params):return(c,i,f_err)
        else: return (c)
    else:
        print("no root")
    #return(root)
