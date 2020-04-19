######################################################################################
#Coded by:M.Sai Mehar
#Date : April 18,2020
# Released Under GNU GPL
#####################################################################################

import mpl_toolkits.axisartist.floating_axes as floating_axes
from matplotlib.projections import PolarAxes
from mpl_toolkits.axisartist.grid_finder import FixedLocator, \
     MaxNLocator, DictFormatter
import control
import numpy as np
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex
#end if

#defining the range of values of omega
omega = np.linspace(-20,20,2000)

#writing the coefficients of transfer function
num=[0.000862,0.0594,1]
den=[0.000005,0.006,1,0,0,0]

#forming the transfer function
G = control.tf(num,den)
magnitude, phase, W = G.freqresp(omega)



#plotting the polar plot
ax1 = plt.subplot(111, projection='polar')
ax1.plot(phase.reshape((2000,))[-1000:],magnitude.reshape((2000,))[-1000:])
plt.plot(-1,0,'o')
plt.annotate("(-1,0)", (-1, 0))
plt.title("polar plot")


#if using termux
plt.savefig('./figs/ee18btech11029.pdf')
plt.savefig('./figs/ee18btech11029.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11029.pdf"))
#else
#plt.show()
