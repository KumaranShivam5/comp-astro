'''
import numpy as np



data = (np.loadtxt('opt_03.dat',dtype=[('t','i4'),('mag','f4'),('err','f4'),('fil','S')] , delimiter=',' ))

#data = np.loadtxt('opt.dat',dtype=float, delimiter=' ')

data_ar =[np.asarray(list(d)) for d in data]
time = data_ar[:,0]
mag = data_ar[:,1]
#err = data[:,2]
#fil = data[:,3]

#time_i = time[fil=='I']
print(time)
#plt.errorbar(time,mag)da

'''
import matplotlib.pyplot as plt


data = []
with open('opt.dat', 'r') as f:
    line = f.readlines()
    for i in line:
        data_temp = [val for val in i.split()]
        data.append(data_temp)

        
time = [int(t[0]) for t in data]
mag = [float(t[1]) for t in data]
err = [float(t[2]) for t in data]
filt = [(t[3]) for t in data]


#time_v = [time[i] if(filt[i=='V']) for i in range(len(filt))]
#time_v = [time]

time_v = [time[i] for i in range(len(filt)) if filt[i]=='V']
mag_v = [mag[i] for i in range(len(filt)) if filt[i]=='V']
err_v = [err[i] for i in range(len(filt)) if filt[i]=='V']
#filt_v = [mag[i] for i in range(len(filt)) if filt[i]=='V']

time_i = [time[i] for i in range(len(filt)) if filt[i]=='I']
mag_i = [mag[i] for i in range(len(filt)) if filt[i]=='I']
err_i = [err[i] for i in range(len(filt)) if filt[i]=='I']
#mag_i = [mag[i] for i in range(len(filt)) if filt[i]=='I']

