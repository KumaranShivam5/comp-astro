import numpy as np
from matplotlib import pyplot as plt
from matplotlib import gridspec as gs 
import seaborn as sns
from scipy.optimize import curve_fit
sns.set_style('darkgrid')
plt.style.use('seaborn-dark-palette')


data = np.loadtxt('data1' , dtype = 'f4,f4,f4')
#print(data)

data = np.asarray([list(d) for d in data])
x = data[:,0]
y = data[:,1]
sigma = data[:,2]



s = sum([1/(sig**2) for sig in sigma])
sum_x = sum([(xi/(sigma_i**2)) for xi , sigma_i in zip(x,sigma)])
sum_y = sum([(xi/(sigma_i**2)) for xi , sigma_i in zip(y,sigma)])
sum_x_sq = sum([(xi**2/(sigma_i**2)) for xi , sigma_i in zip(x,sigma)])
sum_x_y = sum([(xi*yi/(sigma_i**2)) for xi ,yi, sigma_i in zip(x,y,sigma)])


denom = s*sum_x_sq - (sum_x**2)
a1 = (sum_y*sum_x_sq - sum_x*sum_x_y)/denom
a2 = ( s*sum_x_y - sum_x*sum_y ) /denom
print(a1,a2)


sigma_a1_sq = sum([(((sum_x_sq-x_i*sum_x))**2)/(sigma_i**2) for x_i,sigma_i in zip(x,sigma)])/(denom**2)
sigma_a2_sq = sum([((s*x_i-sum_x)**2)/(sigma_i**2) for x_i , sigma_i in zip(x,sigma)])/(denom**2)

err_a1 = sigma_a1_sq**0.5
err_a2 = sigma_a2_sq**0.5
#print(sigma_a1_sq , sigma_a2_sq)
print(err_a1,err_a2)


def linear_model(x,a1,a2):
    val = a1+a2*x
    return(val)


y_mod = linear_model(x,a1,a2)

'''
Goodness of FIT

'''

chi_sq_val = [((y_mi-y_i)**2)/(sigma_i**2) for y_mi , y_i , sigma_i in zip(y_mod,y,sigma)]
chi_sq = sum(chi_sq_val)
print('Chi Sq:',chi_sq)
print('DOF :' , len(y)-2)
reduced_chi_sq = chi_sq/(len(y)-2)
print('Reduced chi sq:' , reduced_chi_sq)


'''
Comparing With Scipy curvefit Module
'''


params , perr = curve_fit(linear_model,x,y , p0=[0,0])
print(params)
err = np.sqrt(np.diag(perr))
print(err)





fig = plt.figure(figsize=(10,8) , constrained_layout=False)
spec = gs.GridSpec(ncols=1 , nrows=2 , height_ratios=[1,0.2] , hspace=0)
ax = fig.add_subplot(spec[0,0])
ax.plot(x,y_mod)
ax.errorbar(x,y,yerr=sigma , fmt='.' , capsize =2 , ecolor='crimson' , color='k' , markersize=5)
ax.text(40,1 , 'a1 = {:.4f}$\pm${:.4f} \n a2 = {:.4f}$\pm${:.4f}'.format(a1,err_a1 , a2, err_a2) , 
        bbox = {'facecolor':'red' , 'alpha':0.3, 'pad':10 } , fontsize = 12)
ax.legend(['Model' , 'Data Observed'])
ax.set_ylabel('y')

plt.style.use('seaborn-whitegrid')
res_plot = fig.add_subplot(spec[1,0] , sharex = ax)
res_plot.step(x,chi_sq_val , where= 'mid')
res_plot.text(40,2.5 , 'Chi sq : {:.4f} \n Reduced Chi sq : {:.4f}'.format(chi_sq,reduced_chi_sq) , 
        bbox = {'facecolor':'blue' , 'alpha':0.2, } , fontsize = 10)
res_plot.set_ylabel('$\chi^2$')
res_plot.set_xlabel('x')
#res_plot.errorbar(x,chi_sq_val , yerr = sigma , fmt='.')
plt.show()



