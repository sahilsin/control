#Code by Neil Dhami
#Date 20th May,2020
import numpy as np  
from matplotlib import pyplot as plt  

#if using termux
import subprocess
import shlex
#end if

data=np.loadtxt('ee18btech11031_2.dat')  #loading the data from the simulation output
plt.plot(data[:,0],data[:,1])  
plt.grid()
plt.xlabel("time")
plt.ylabel("Three stage oscillator output")
plt.title("Output from spice simulation")
plt.plot([0.00422288,0.004229],[0,0],'b--')
plt.plot(0.004229,0,'o')
plt.plot(0.00422288,0,'o')
plt.text(0.004229,-0.05,"(0.004229,0)")
plt.text(0.00422,-0.05,"(0.00422288,0)")
#if using termux
#plt.savefig('./figs/ee18btech11031/ee18btech11031_spice_2.pdf')
#plt.savefig('./figs/ee18btech11031/ee18btech11031_spice_2.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11031/ee18btech11031_spice_2.pdf"))
#else
#plt.show()
