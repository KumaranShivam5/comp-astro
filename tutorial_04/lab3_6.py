import matplotlib.pyplot as plt
import random as rd
import numpy as np

ls =[]
for i in range(0,500):
    ls.append(rd.random()*100)

bins = np.linspace(0,100,21)

plt.hist(ls, bins=bins)
plt.show()
