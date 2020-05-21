#Code by C Shruti
#Date 16 May,2020


import numpy as np  
from matplotlib import pyplot as plt  

#if using termux
import subprocess
import shlex
#end if

data=np.loadtxt('/home/shruti/Desktop/ee18btech11006.dat')  
plt.plot(data[:,0],data[:,1])  
plt.grid()
plt.xlabel("Input Voltage")
plt.ylabel("Output of the system")
plt.title("Output from spice simulation")

#if using termux
plt.savefig('./figs/ee18btech11006/ee18btech11006_8.pdf')
plt.savefig('./figs/ee18btech11006/ee18btech11006_8.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11006/ee18btech11006_8.pdf"))
#else
#plt.show()

