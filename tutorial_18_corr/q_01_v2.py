import numpy as np 
from cross_corr import cross_corr , circ_corr
from fft import fft_freq , compute_fft , compute_ifft
from matplotlib import pyplot as plt 
import seaborn as sns
sns.set_theme('paper')

data = np.loadtxt('data-cor')
y = data[:,1]
time = data[:,0]

plt.plot(time , y)
plt.show()



plt.figure(figsize=(8,6))
t1 = [5.0,10.0]
for t_1 in t1:
    del_t = 0.05
    n_t = int(t_1/del_t)
    y_5 = y[:n_t]
    cor_5 , del_t_5 = circ_corr(y_5 , type='half')
    del_t_5 = [t*del_t for t in del_t_5]
    plt.plot(del_t_5 , cor_5)
plt.xlabel('Time Lag (x)')
plt.ylabel('Correlation')
plt.legend(['5.0s of data' , '10.0 s of data'])
plt.show()


plt.figure(figsize=(8,6))
cx , del_t = circ_corr(y , type='half')
del_t = [d*0.05 for d in del_t]
plt.plot(del_t , cx)

'''
l = len(y)
y = np.append(y , np.zeros(len(y)))
powspec = compute_fft(y)
pow_sq = [(abs(p))**2 for p in powspec]
c_fft = [x.real for x in compute_ifft(pow_sq)]
c_fft = np.append(c_fft[l+1:2*l], c_fft[:l])

'''

l = len(y)
#y = np.append(y , np.zeros(len(y)))
powspec = compute_fft(y)
pow_sq = [(abs(p))**2 for p in powspec]
c_fft = [x.real for x in compute_ifft(pow_sq)]
#c_fft = np.append(c_fft[l+1:2*l], c_fft[:l])



plt.plot(del_t , c_fft) 
plt.legend(['Using Correlation function','Using FFT'])
plt.xlabel('Time Lag (s)')
plt.ylabel('Correlation')
plt.savefig('fft_corr.png')
plt.show()

