import numpy as np
import matplotlib.pyplot as plt

def linear(x,x1,y1,x2,y2,err_y1,err_y2):
    y = (x-x1)*((y1-y2)/(x1-x2))+y1
    ## error propogation
    err_1 = ((x-x1)/(x1-x2)+1)*err_y1
    err_2 = -((x-x1)/(x1-x2))*err_y2
    err = abs(err_1+err_2)
    return (y,err)

data = np.loadtxt('opt.dat',dtype='i8,f8,f8,S4',encoding=None)

time = [int(t[0]) for t in data]
mag = [float(t[1]) for t in data]
err = [float(t[2]) for t in data]
filt = [(t[3]).decode() for t in data]


time_v = [time[i] for i in range(len(filt)) if filt[i]=='V']
mag_v = [mag[i] for i in range(len(filt)) if filt[i]=='V']
err_v = [err[i] for i in range(len(filt)) if filt[i]=='V']


time_i = [time[i] for i in range(len(filt)) if filt[i]=='I']
mag_i = [mag[i] for i in range(len(filt)) if filt[i]=='I']
err_i = [err[i] for i in range(len(filt)) if filt[i]=='I']


i = [(x,y,z) for x,y,z in zip(list(time_i),list(mag_i),list(err_i))]
#print(time_v)
#print(time_i)


##assumption that at one epoch only one of the measurment is taken
## that is V and I are not measured at exact same time
## also expected that data is arranged ascending order time-wise 
## (which is usually the case for time series data)
'''
'''


def find_next(t,in_array):
    '''
    takes time t and return the array index 
    corresponding to its neighbourhood in the 
    given array in_array
    '''
    i,h,l = 0,0,0
    try:
        while(t > in_array[i]):
            i+=1
            h = i
            l=i-1
    except:
        h,l=0,0
    return((l,h))

i = 0
inter_data = []
for t in time_i:
    l,h = (find_next(t,time_v))
    #print(l,h)
    if(h):
        x1,x2,y1,y2 ,err_y1,err_y2= time_v[l],time_v[h],mag_v[h],mag_v[l],err_v[l],err_v[h]
        mag_v_int ,mag_v_err= linear(t,x1,y1,x2,y2,err_y1,err_y2)
        ##absolute errors are added
        total_err = mag_v_err+err_i[i]
        temp = [t,mag_v_int-mag_i[i],total_err]
        inter_data.append(temp)
    #print(i)
    i+=1
inter_data = np.asarray(inter_data)
color_time = inter_data[:,0]
color_index = inter_data[:,1]
color_err = inter_data[:,2]
plt.gca().invert_yaxis()
plt.xlabel('Time')
plt.ylabel('Color Index $V-I$')
plt.title('Color Index')
plt.xscale('log')
plt.errorbar(color_time, color_index, fmt='ok', yerr=color_err)
#print(time)
plt.show()
