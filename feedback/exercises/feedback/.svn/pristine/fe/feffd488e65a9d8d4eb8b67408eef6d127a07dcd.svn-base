#Code by Tejaswini
#Date 10 May,2020

import numpy as np  
from matplotlib import pyplot as plt  

#if using termux
import subprocess
import shlex
#end if

data=np.loadtxt('ee18btech11047.dat')  
plt.plot(data[:,0],data[:,1])  
plt.grid()
plt.xlabel("time")
plt.ylabel("oscillating response")
plt.title("Output from spice simulation")

#if using termux
plt.savefig('./figs/ee18btech11047/ee18btech11047_spice.pdf')
plt.savefig('./figs/ee18btech11047/ee18btech11047_spice.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11047/ee18btech11047_spice.pdf"))
#else
#plt.show()
