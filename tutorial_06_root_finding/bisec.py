import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return(np.cos(x)-x**3)

x = np.linspace(-7.5,7.5)
y = f(x)
plt.plot(x, y)
#plt.show()

#### Bisection method ####


e = 0.0000001
x_a = -1
x_b = 0.89
root = 0
if(f(x_a)*f(x_b)<0):
    while((x_b-x_a)>e):
        c = (x_a+x_b)/2
        x_a,x_b = np.where(f(x_a)*f(c)<0,(x_a,c),(c,x_b))
    root = c
else:
    print("no root")

############# Newton Ralpson Method ###################
eps = 0.0001
x_np1 = 0
def newton_roots(f,fd,x_n, epsilon):
    x_n1 = x_n - f(x_n)/fd(x_n)
    while (abs(x_n1-x_n)>epsilon):
        temp = x_n1
        x_n1 = x_n  - f(x_n)/fd(x_n)
        x_n = temp


print(root)
print(f(root))
