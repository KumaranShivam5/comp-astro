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

def gen_rand_n(x_min ,x_max , n):
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

def gen_samples(f,x_min , x_max , N):
    import numpy as np 
    x_val = np.linspace(x_min, x_max , N)
    y_val = [f(x) for x in x_val]
    print(y_val)
    y_max = np.amax(y_val)
    print(y_max)
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

def histogram(x,bins):
    if(type(bins)=='int'):
        hist , bins = histogram_const_bin(x,bins)
    else:
        hist , bins = histogram_given_bin(x,bins)
    return(hist, bins)

def histogram_const_bin(x, bins):
    x = np.asarray(x)
    v_min = np.amin(x)
    v_max = np.amax(x)
    h = (v_max-v_min)/bins
    #print(v_min , v_max)
    hist = []
    x_axis = []
    for i in range(bins):
        temp_min = v_min+i*h
        temp_max = v_min+(i+1)*h
        #print(temp_min, temp_max)
        temp = [x_val for x_val in x if ((x_val>temp_min) and (x_val<=temp_max))] 
        #print(temp)
        count = len(temp)
        hist.append(count)
        x_axis.append((temp_min+temp_max)/2)
    return(hist , x_axis)

def histogram_given_bin(x, bins):
    x = np.asarray(x)
    v_min = np.amin(x)
    v_max = np.amax(x)
    h = (v_max-v_min)/bins
    #print(v_min , v_max)
    hist = []
    x_axis = []
    for i in range(len(bins)):
        temp = [x_val for x_val in x if ((x_val>bins[i]) and (x_val<=bins[i+1]))] 
        #print(temp)
        count = len(temp)
        hist.append(count)
        #x_axis.append((temp_min+temp_max)/2)
    return(hist, bins)
