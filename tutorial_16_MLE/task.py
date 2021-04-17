import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
data = [-.999, -.983, -.956, -.946, -.933, -.925, -.916, -.910, -.881, -.739, -.734, -.717, -.715, -.675, -.665, -.649,-.621, -.537, -.522, -.508, -.499, -.471, -.460, -.419, -.403, -.311, -.305, -.281, -.170, -.162, -.063, 0.214, 0.438, .444, .508, .586, .638, .677, .721, .730, 0.768, .785, .790, .793, .877, .896, .931, .938, 0.948, 0.999
]
#data = np.loadtxt('data_500')
sns.set_theme(context='paper' , style='darkgrid' , palette='rocket')

def given_dist(alpha , x):
    N = 2*(1+alpha/3)
    val = (1+alpha*(x**2))
    return val

def calc_lk(alpha , c_theta , log_lik = True):
    c_theta = np.asarray(c_theta)
    m = len(c_theta)
    denom = (2*(1+alpha/3))**m
    prod =1
    for th in c_theta:
        prod = prod*(1+alpha*(th**2))
    val = prod/denom
    if(log_lik):
        return np.log(val)
    else:
        return val

alpha = np.linspace(1,20 , num=100)
l_val = calc_lk(alpha,data)
alpha_max = alpha[np.argmax(l_val)]
l_max = calc_lk(alpha_max , data)
#print(l_max)
print(alpha_max)

x = np.linspace(-1,1)
model_dist = given_dist(alpha_max , x)

sns.lineplot(x=alpha,y=l_val)
plt.vlines(x=alpha_max , ymin=np.amin(l_val),ymax=np.amax(l_val) , linestyle='--')
plt.xlabel(r'$\alpha$')
plt.ylabel('Log-likelihood')
plt.show()

#plt.hist(data ,  bins=10)
sns.distplot(data, kde=False ,  bins=10 )
plt.plot(x,model_dist )
plt.show()


#plt.show()