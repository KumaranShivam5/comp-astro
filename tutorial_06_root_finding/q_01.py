from root_methods import bisect_root,newton_roots
import numpy as np
def f1(x):
    return(np.cos(x)-x**3)
def f1d(x):
    return (-np.sin(x)-3*x**2)

print(bisect_root(f1,-1,1,0.001))
print((newton_roots(f1,f1d,1,0.001)))

x = np.linspace(0.85,0.89)
import matplotlib.pyplot as plt
plt.grid()
plt.plot(x, f1(x))
plt.show()