
import numpy as np  
from matplotlib import pyplot as plt  

#if using termux
import subprocess
import shlex
#end if

data=np.loadtxt('Vout.dat')  
plt.xlim(120, 130)
plt.ylim(-10,10)
plt.plot([117,140], [0,0], 'g--', lw=1, label='OV')
plt.plot(122.60,0,'o')
plt.plot(124.150,0,'o')

plt.plot(data[:,0],data[:,1])  
plt.grid()
plt.xlabel("time")
plt.ylabel("Vout")
plt.title('Output from spice simulation')

#if using termux
plt.savefig('./figs/es17btech11002/es17btech11002_2_spice2.pdf')
plt.savefig('./figs/es17btech11002/es17btech11002_2_spice2.eps')
subprocess.run(shlex.split("termux-open ./figs/es17btech11002/es17btech11002_2_spice2.pdf"))
#else
#plt.show()
