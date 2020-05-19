import numpy as np
import matplotlib.pyplot as plt


#if using termux 

import subprocess
import shlex
#end if

data=np.loadtxt('plotdata.data')  

data2=np.loadtxt('plotdata2.data')  

data3=np.loadtxt('plotdata3.data')  


plt.figure(1)
plt.title ('H from spice simulation')
plt.plot(data[:,0],data[:,1])
plt.ylabel('H')
plt.xlabel('frequency Hz')
plt.grid()


#if using termux
plt.savefig('./figs/H1.pdf')
plt.savefig('./figs/H1.eps')
subprocess.run(shlex.split("termux-open ./figs/H1.pdf"))
#else


plt.figure(2)
plt.title ('G from spice simulation')
plt.plot(data2[:,0],data2[:,1])
plt.ylabel('G')
plt.xlabel('frequency Hz')
plt.grid()


#if using termux
plt.savefig('./figs/G1.pdf')
plt.savefig('./figs/G1.eps')
subprocess.run(shlex.split("termux-open ./figs/G1.pdf"))
#else


plt.figure(3)
plt.title ('T from spice simulation')
plt.plot(data3[:,0],data3[:,1])
plt.ylabel('T')
plt.xlabel('frequency Hz')
plt.grid()


#if using termux
plt.savefig('./figs/T1.pdf')
plt.savefig('./figs/T1.eps')
subprocess.run(shlex.split("termux-open ./figs/T1.pdf"))
#else

#plt.show()
