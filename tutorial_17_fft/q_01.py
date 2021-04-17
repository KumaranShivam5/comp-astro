import numpy as np
from fft import compute_fft , compute_ifft , fft_freq
from matplotlib import pyplot as plt
import seaborn as sns
sns.set_theme('paper')
np.random.seed(878627362)

def f(t):
    val = np.cos(6*np.pi*t)
    return val

def analysis(n, delta_t , f ,  save_plot=""):
    t = []
    t_0 = 0   
    for i in range(n):
        t.append(t_0 +  i*delta_t)

    t = np.asarray(t)
    om = fft_freq(n,delta_t)
    ft= f(t)
    fw = compute_fft(ft)
    fw_p = [abs(f)**2 for f in fw]

    om_max = om[np.argmax(fw_p)]

    fig = plt.figure(figsize=(12,4))
    ax1 = fig.add_subplot(121)
    ax1.stem(t,ft , linefmt='-')
    #ax1.stem(fw_p)
    ax2 = fig.add_subplot(122)
    ax2.stem(om,fw_p)
    ax1.set_title('Time series data')
    ax2.set_title('Power spectrum')
    ax1.set_xlabel('Time')
    ax1.set_ylabel('f(t)')
    ax2.set_xlabel("$\omega$")
    ax2.set_ylabel("Power")
    ax2.legend(["Max Power at freq: {:.2f}".format(om_max)])
    if(save_plot!=""):
        plt.savefig(save_plot)
    plt.show()

analysis(128, 0.5 , f , save_plot="0p5.png")
analysis(128, 0.25 , f , save_plot="0p25.png")
analysis(128, 0.15 , f , save_plot="0p15.png")
analysis(128, 0.1 , f , save_plot="0p1.png")
analysis(128, 0.05 , f , save_plot="0p05.png")
