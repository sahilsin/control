#if using termux
import subprocess
import shlex
#end if
import numpy as np
import matplotlib.pyplot as plt
din = np.loadtxt('./spice/ee18btech11042/input.dat')
dout = np.loadtxt('./spice/ee18btech11042/output.dat')
plt.subplot(2,1,1)

plt.ylabel('$v_{in}$')
plt.plot(din[:,0],din[:,1])

plt.subplot(2,1,2)
plt.xlabel('$t$')
plt.ylabel('$v_{out}$')
plt.plot(dout[:,0],dout[:,1])
#if using termux
plt.savefig('./figs/ee18btech11042/ee18btech11042.pdf')
plt.savefig('./figs/ee18btech11042/ee18btech11042_1.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11042/ee18btech11042.pdf"))
#else
#plt.show()

plt.show()

