#Code by B.Varuni
#date 23rdh,May 2020

import numpy as np  
from matplotlib import pyplot as plt  

#if using termux
import subprocess
import shlex
#end if

data=np.loadtxt('ee18btech11005.dat')  #loading the data from the simulation output
plt.plot(data[:,0],data[:,1])  
plt.grid()
plt.xlabel("time")
plt.ylabel("unit step response")
plt.title("Output from spice simulation")

#if using termux
#plt.savefig('./figs/ee18btech11005/ee18btech11005_spice.pdf')
#plt.savefig('./figs/ee18btech11005/ee18btech11005_spice.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11005/ee18btech11005_spice.pdf"))
#else
#plt.show()
