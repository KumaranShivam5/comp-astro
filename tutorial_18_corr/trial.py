import numpy as np 
from cross_corr import cross_corr
from fft import fft_freq , compute_fft , compute_ifft
from matplotlib import pyplot as plt 


data = np.loadtxt('data-cor')
y = data[:,1]
print(len(data))
x = [1,2,3,4]
c , _ = cross_corr(y , y)
print(c[0])
print(np.dot(y,y))