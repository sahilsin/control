import numpy as np  
from matplotlib import pyplot as plt  

#if using termux
import subprocess
import shlex
#end if

# plotting the ngspice output 

data=np.loadtxt('Vout.dat')  
plt.plot(data[:,0],data[:,1])  
plt.grid()
plt.xlabel("time")
plt.ylabel("Vout")
plt.title('Output from Oscillator')

#if using termux
plt.savefig('./figs/es17btech11002/es17btech11002_2_spice.pdf')
plt.savefig('./figs/es17btech11002/es17btech11002_2_spice.eps')
subprocess.run(shlex.split("termux-open ./figs/es17btech11002/es17btech11002_2_spice.pdf"))
#else
#plt.show()
