# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex
#end

#T = 0.0313905 - 0.03062
#f = 1/T
#print(f)


#Loading the data
data = np.loadtxt( 'es17btech11002.dat' )
#PLotting the data from spice simulation
plt.plot(data[:,0],data[:,1])
plt.grid()
plt.xlabel('time')
plt.ylabel('Vout')
plt.title('Output from Oscillator')
plt.legend()



#if using termux
plt.savefig('./figs/es17btech11002/es17btech11002_spice.pdf')
plt.savefig('./figs/es17btech11002/es17btech11002_spice.eps')
subprocess.run(shlex.split("termux-open ./figs/es17btech11002/es17btech11002_spice.pdf"))
#else
#plt.show()