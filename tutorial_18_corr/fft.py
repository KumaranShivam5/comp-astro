import numpy as np
from ordering import order_bit_rev
def get_index_pair(n,stg):
    flag = 1
    x = np.arange(n)
    delta_stp = 2**(stg)
    grp_1 , grp_2 = [] , []
    for i in range(0,len(x),delta_stp):
        for k in range(i,i+delta_stp):
            #print(k , flag)
            if(flag==1):
                grp_1.append(x[k])
            else: grp_2.append(x[k])
            #print(flag)
        flag*=-1
    index_pair = [[i1,i2] for i1,i2 in zip(grp_1, grp_2)]
    return index_pair

def butterfly_fft(x , w ):
    f0 = x[0] + w*x[1]
    f1 = x[0] - w*x[1]
    return ([f0,f1])
def butterfly_ifft(x , w ):
    f0 = x[0] + x[1]
    f1 = w*(x[0] - x[1])
    return ([f0,f1])


def compute_fft(x):
    stages = int(np.log2(len(x)))
    x = order_bit_rev(x)
    for stg in range(stages):
        ind = get_index_pair(len(x),stg)
        i = 0
        N = 2**(stg+1)
        for pair in ind:
            k = i%(2**(stg))
            inp_pair = [x[pair[0]] , x[pair[1]]]
            w = np.exp(-(2j*np.pi*k)/(N)).round(15)
            x[pair[0]],x[pair[1]] = butterfly_fft(inp_pair , w)
            i+=1
    #x = [round(x_i,8) for x_i in x]
    #l = len(x)
    return x
    
def compute_ifft(x):
    l = len(x)
    stages = int(np.log2(l))
    for stg in range(stages):
        stg_ord = stages - stg - 1
        ind = get_index_pair(len(x),stg_ord)
        i = 0
        N = 2**(stg_ord+1)
        for pair in ind:
            k = i%(2**(stg_ord))
            inp_pair = [x[pair[0]] , x[pair[1]]]
            w = np.exp((2j*np.pi*k)/(N)).round(15)
            x[pair[0]],x[pair[1]] = butterfly_ifft(inp_pair , w)
            i+=1
    x = order_bit_rev(x)
    x = [x_i/len(x)  for x_i in x]
    return x 

def  fft_freq(n,del_t):
    del_om = (2*np.pi)/(del_t*n)
    set_a = np.arange(0 , n/2)*del_om 
    set_b = np.arange(-n/2 ,0)*del_om
    f = np.append(set_a , set_b)
    #sprint(len(f))
    #print()
    return f

#fft_freq(128 , 0.1)