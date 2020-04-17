###################################################################

# This a python code for System response Gm(t) vs t  
# By Moparthi Varun Sankar
# April 17 , 2020 
# Released under GNU GPL

###################################################################
import matplotlib.pyplot as plt
import numpy as np
import math

#if using termux
import subprocess
import shlex
#end if

t = np.linspace(0, 30,1000)

y = (8.00/73.00)*np.cos(2*t) +(152.00/73.00)*np.sin(2*t) + (-8.00/73.00)*np.exp(-3*t/4)

plt.grid()
plt.title("$g_m(t)$")
plt.xlabel("$t$")
plt.ylabel("Oscillator")
plt.plot(t,y)

#if using termux
plt.savefig('./figs/ee18btech11030/ee18btech11030_1.pdf')
plt.savefig('./figs/ee18btech11030/ee18btech11030_1.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11030/ee18btech11030_1.pdf"))
#else
#plt.show()
