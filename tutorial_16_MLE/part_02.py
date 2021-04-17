import numpy as np 
from functions import calc_lk ,  given_dist 
from matplotlib import pyplot as plt 

x = np.random.uniform(high=1 , low=-1 , size=100)
plt.hist(x)
plt.show()
