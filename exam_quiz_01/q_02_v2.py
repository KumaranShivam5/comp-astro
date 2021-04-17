from interpol import lagrange
import numpy as np
from matplotlib import pyplot as plt

'''
constants
'''

h0 = 67.4e3 # in m/s/mpc
c = 3e8 #in m/s


#filled model calculate dl from z 
def filled_calc_dl(z):
    val = (2*c/h0)*(1+z)*(1-1/(np.sqrt(1+z)))
    return val

## empty universe model

def empty_univ_calc_dl(z,omega):
    val = (1+z)*(c/(h0*omega))*np.sinh(2.7*np.sqrt(omega))
    return val

# calc distance modulus from distance dl

def calc_dm(dl):
    '''
    dl must be in Mpc
    '''
    val = 5*np.log10(dl)+25
    return val



##############_____________________________________
#reading data

data = np.loadtxt('SCPdata.txt', dtype='S8 , f4, f4, f4' , encoding=None)
data = np.asarray([list(d) for d in data])
names = data[:,0]
name = [n.decode() for n in names]
rs = data[:,1]
dm = data[:,2]
dm_err = data[:,3]

rs = [float(r.decode()) for r in rs] # redshifts
dm = [float(d.decode()) for d in dm] # ditance Modulus
dm_err = [float(de.decode()) for de in dm_err] # error in distance odulus

'''
# just checking if everythiing is loaded alright
i = 14
print(name[i] , rs[i] , dm[i] , dm_err[i])
'''

#done with readin data

##__________________________________________________


## calculation dl values for the range of redshifts in the data

rs_m = np.linspace(np.amin(rs),np.amax(rs),100)

dl_01 = [empty_univ_calc_dl(z , 0.1) for z in rs_m]
dl_02 = [empty_univ_calc_dl(z , 0.5) for z in rs_m]
dl_03 = [filled_calc_dl(z) for z in rs_m]

dm_01 = [calc_dm(d) for d in dl_01]
dm_02 = [calc_dm(d) for d in dl_02]
dm_03 = [calc_dm(d) for d in dl_03]


plt.style.use('seaborn-darkgrid')
plt.figure(figsize=(8,6))

plt.plot(rs_m ,dm_01 ,color ='teal'    ,zorder = 1)
plt.plot(rs_m, dm_02 ,color='indigo', zorder =2)
plt.plot(rs_m, dm_03,color='firebrick' , zorder =2)
plt.errorbar(rs,dm, yerr=dm_err ,fmt='.k' ,ecolor='k' , elinewidth=0.5, zorder=1 , capsize=1)
plt.ylabel('Model Distance Modulus $\mu_{model}$')
plt.xlabel('Redshifts')
plt.legend(['Empty Universe with $\Omega=0.1$' ,'Empty Universe with $\Omega=0.5$' ,'Filled Universe Model' ,'Observed Data'])
plt.savefig('q_02_a.png')
plt.show()



## calculating model redshifts at the values of observed redshift


dl_01 = [empty_univ_calc_dl(z , 0.1) for z in rs]
dl_02 = [empty_univ_calc_dl(z , 0.5) for z in rs]
dl_03 = [filled_calc_dl(z) for z in rs]

dm_01 = [calc_dm(d) for d in dl_01]
dm_02 = [calc_dm(d) for d in dl_02]
dm_03 = [calc_dm(d) for d in dl_03]


del_01 = [d1-d2 for d1,d2 in zip(dm,dm_01)]
del_02 = [d1-d2 for d1,d2 in zip(dm,dm_02)]
del_03 = [d1-d2 for d1,d2 in zip(dm,dm_03)]


plt.figure(figsize=(8,6))
plt.errorbar(rs ,del_01 , yerr=dm_err , fmt='.k', ecolor='k' ,elinewidth=0.5)
plt.errorbar(rs ,del_02 , yerr=dm_err , fmt='.b', ecolor='b' ,elinewidth=0.5)
plt.errorbar(rs ,del_03 , yerr=dm_err , fmt='.',color='crimson', ecolor='crimson' ,elinewidth=0.5)
plt.ylabel('Residuals  ($\Delta \mu_{observed} - \Delta \mu_{model}$)')
plt.xlabel('Redshifts')
plt.legend(['Empty Universe with $\Omega=0.1$' ,'Empty Universe with $\Omega=0.5$' ,'Filled Universe Model'])
plt.savefig('q_02_b.png')
plt.show()

