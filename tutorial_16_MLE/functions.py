def given_dist(alpha , x):
    N = 2*(1+alpha/3)
    val = (1+alpha*(x**2))
    return val

def calc_lk(alpha , c_theta , log_lik = True):
    c_theta = np.asarray(c_theta)
    m = len(c_theta)
    denom = (2*(1+alpha/3))**m
    prod =1
    for th in c_theta:
        prod = prod*(1+alpha*(th**2))
    val = prod/denom
    if(log_lik):
        return np.log(val)
    else:
        return val