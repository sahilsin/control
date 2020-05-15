###########################################
#coded by:M.Sai Mehar
#date :may 11,2020
#Released under GNU GPL
##########################################

import numpy as np
from scipy import signal
import control
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex
#end if

num1 = [0.0198727422,-13495920]
den1 = [3.33*(10**-12),0.000799,1]
G1 = signal.lti(num1,den1)
w1, mag1, phase1 = signal.bode(G1)
sys1 = control.tf(num1, den1)
gm1, pm1, wg1, wp1 = control.margin(sys1)
gm1 = -20*np.log10(gm1)



num2 = [-13495920]
den2 = [0.000000245,0.01555,1]
G2 = signal.lti(num2,den2)
w2, mag2, phase2 = signal.bode(G2)
sys2 = control.tf(num2, den2)
gm2, pm2, wg2, wp2 = control.margin(sys2)
gm2 = -20*np.log10(gm2)


#Magnitude plot
plt.figure()
plt.subplot(2, 1, 1) 
plt.xlabel("$\omega$")
plt.ylabel("20$log_{10}(|G(j\omega)|$")
plt.title("Magnitude Plot")
plt.semilogx(w2, mag2,label='$C_{f}$=0pF') 
plt.legend()

plt.text(100000,74.0722,'$f_{p1}$')
plt.text(1000000,34.533, '$f_{p2}$')
plt.semilogx(w1, mag1,label='$C_{f}$=58.9')

plt.plot(100000,74.0722,'o')
plt.plot(1000000,34.533,'o')
plt.plot(200,143.567,'o')
plt.plot(37950000,52.50,'o')

plt.text(200,143.567,'$f_{p1}^{1} $')
plt.text(37950000,49.50, '$f_{p2}^{1}$')
plt.legend()
plt.grid()

# Phase plot
plt.subplot(2, 1, 2) 
plt.xlabel("$\omega$")
plt.ylabel("$\phi(j\omega)$")
plt.title("Phase Plot")
plt.semilogx(w2, phase2,label='$C_{f}$=0pF')
plt.semilogx(w1, phase1,label='$C_{f}$=58.9pF')  

plt.legend()
plt.grid()

#if using termux
plt.savefig('./figs/ee18btech11039/ee18btech11039.pdf')
plt.savefig('./figs/ee18btech11039/ee18btech11039.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11039/ee18btech11039.pdf"))
#else
#plt.show() 

