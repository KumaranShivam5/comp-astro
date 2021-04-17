import numpy as np 
from find_period import find_avg_time
from matplotlib import pyplot as plt

data = np.loadtxt('theta_rk4_all_v2.csv')
time = data[0,:]
theta_all = data[1:,:]

fig = plt.figure()
period = []
for th in theta_all:
    plt.plot(time , th)
    p = find_avg_time(th, time)
    period.append(p)
    #plt.title('Period  = {:.2f}'.format(p))
    #plt.show()
    #plt.plot(time , theta_all[3])
theta = [10 , 45 , 90 , 135]
leg = ['theta {:.2f} period = {:.2f}'.format(t, p) for t, p in zip(theta,period)]
print(leg)
plt.legend(leg)
plt.savefig('rk4_solutions.png')
plt.show()