import numpy as np
data = np.loadtxt('opt_v2.dat',dtype='i8,f8,f8,S4',encoding=None)
 
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
