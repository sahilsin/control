import numpy as np
import matplotlib.pyplot as plt


#if using termux 

import subprocess
import shlex
#end if

data=np.loadtxt('plotdata.dat')  

data2=np.loadtxt('plotdata2.dat')  

data3=np.loadtxt('plotdata3.dat')  

#plot of H
plt.figure(1)
plt.title ('H from spice simulation')
plt.plot(data[:,0],data[:,1])
plt.xlim(50000)
plt.ylabel('H')
plt.xlabel('frequency Hz')
plt.grid()


#if using termux
plt.savefig('./figs/H.pdf')
plt.savefig('./figs/H.eps')
subprocess.run(shlex.split("termux-open ./figs/H.pdf"))
#else

#plot of G
plt.figure(2)
plt.title ('G from spice simulation')
plt.plot(data2[:,0],data2[:,1])
plt.xlim(50000)
plt.ylabel('G')
plt.xlabel('frequency Hz')
plt.grid()


#if using termux
plt.savefig('./figs/G.pdf')
plt.savefig('./figs/G.eps')
subprocess.run(shlex.split("termux-open ./figs/G.pdf"))
#else

#plot of T
plt.figure(3)
plt.title ('T from spice simulation')
plt.plot(data3[:,0],data3[:,1])
plt.xlim(50000)

plt.ylabel('T')
plt.xlabel('frequency Hz')
plt.grid()


#if using termux
plt.savefig('./figs/T.pdf')
plt.savefig('./figs/T.eps')
subprocess.run(shlex.split("termux-open ./figs/T.pdf"))
#else

#plt.show()
