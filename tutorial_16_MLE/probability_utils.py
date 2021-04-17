#import random as rnd 
import numpy as np
def gen_rand_n(x_min ,x_max , n):
    import random as rnd 
    x = []
    n = int(n)
    for i in range(n):
        mu = rnd.uniform(0,1)
        xi = x_min + mu*(x_max-x_min)
        x.append(xi)
    if (len(x)==1):
        return x[0]
    else:
        return x

def gen_samples(f,x_min , x_max , y_max , N):
    import numpy as np 
    x_acc = []
    i = 0
    while(i<N):
        x = gen_rand_n(x_min,x_max,1)
        y = np.random.uniform(0,y_max)
        if(y<=f(x)):
            x_acc.append(x)
            i+=1
    return x_acc

def calc_likelihood(pdf , data , log_lik = True , neg = False):
    log_l = 0
    if(log_lik):
        log_l = sum([np.log(pdf(d)) for d in data])
        if(neg):
            return -log_l
        else :
            return (log_l)

def min_lkhd(f , p_min , p_max , data ,method='gs'):
    p = p_min 
    delta = 0.01
    prev = calc_likelihood(f(p) , data , neg=True)
    p = p+delta
    nxt = calc_likelihood(f(p) , data , neg=True)
    grad = (nxt - prev)/delta
    while(grad>1e-8 and p < p_max):
        grad = (nxt - prev)/delta
        p = p - grad * delta
        prev = nxt 
        nxt = calc_likelihood(f(p) , data , neg=True)
    return p
