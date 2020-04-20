######################################################################################
#Coded by: Rishitha
#Date : April 19,2020
# Released Under GNU GPL
#####################################################################################

import control
import numpy as np
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex
#end if

omega = np.linspace(-20,20,2000)

num=[1]
den=[1,6,11,7]

G = control.tf(num,den)
magnitude, phase, W = G.freqresp(omega)

ax1 = plt.subplot(111, projection='polar')
ax1.plot(phase.reshape((2000,))[-1000:],magnitude.reshape((2000,))[-1000:])
plt.plot(-1,0,'o')
plt.annotate("(-1,0)", (-1, 0))
plt.title("polar plot")
plt.savefig('polar.png')

#if using termux
plt.savefig('./figs/ee18btech11033.pdf')
plt.savefig('./figs/ee18btech11033.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11033.pdf"))
#else
#plt.show()
