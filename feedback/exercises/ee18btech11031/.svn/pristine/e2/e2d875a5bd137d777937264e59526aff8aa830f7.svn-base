#Code by Neil Dhami
#Date 20th May,2020
import numpy as np  
from matplotlib import pyplot as plt  

#if using termux
import subprocess
import shlex
#end if

data=np.loadtxt('ee18btech11031_1.dat')  #loading the data from the simulation output
plt.plot(data[:,0],data[:,1])  
plt.grid()
plt.xlabel("time")
plt.ylabel("Three stage oscillator output")
plt.title("Output from spice simulation")

#if using termux
#plt.savefig('./figs/ee18btech11031/ee18btech11031_spice_1.pdf')
#plt.savefig('./figs/ee18btech11031/ee18btech11031_spice_1.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11031/ee18btech11031_spice_1.pdf"))
#else
#plt.show()
