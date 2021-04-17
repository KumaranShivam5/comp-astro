import numpy as np

def find_avg_time(theta , time):
    zero_cross = []
    for i in range(len(theta)-1):
        prev = theta[i]
        nxt = theta[i+1]
        if(prev*nxt<0):
            zero_cross.append(time[i])
    #print(zero_cross)
    z_odd = zero_cross[0::2]
    z_even = zero_cross[1::2]
    
    t_avg_list = [(z2-z1)*2 for z1, z2 in zip(z_odd, z_even)]
    t_avg = sum(t_avg_list)/len(t_avg_list)
    return t_avg

#print(t_avg)