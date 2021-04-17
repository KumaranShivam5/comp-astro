
def dec_to_bin(n):
    if (n==1): return [1]
    if(n==0): return [0]
    q = n//2
    rem = n%2
    #print(q)
    bin_val = []
    while(q!=0):
        q = n//(2)
        rem = n%(2)
        bin_val.append(rem)
        n = q 
    return bin_val[::-1]
def bin_to_dec(x):
    p = [2**i for i in range(len(x))][::-1]
    val = sum( [x*p for x,p in zip(x,p)])
    return val
#print(dec_to_bin(2))

def order_bit_rev(x):
    import numpy as np
    index = [i for i in range(len(x))]
    p = int(np.log2(len(x)))
    bin_index = [dec_to_bin(i) for i in range(len(x))]
    for i in range(len(bin_index)):
        l = len(bin_index[i])
        while(l<p):
            bin_index[i].insert(0,0)
            l = len(bin_index[i])

    bin_index_rev = [b[::-1] for b in bin_index]
    index_rev = [bin_to_dec(b) for b in bin_index_rev]
    x_temp= [1]*len(x)

    for i in range(len(x)):
        x_temp[i] = x[index_rev[i]]
    return (x_temp)

#x = [0,1,2, 3 , 4 ,5 ,6 ,7]
#order_bit_rev(x)