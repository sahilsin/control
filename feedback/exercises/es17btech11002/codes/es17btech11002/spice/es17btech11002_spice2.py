# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex
#end

T = 0.0313164 - 0.03060
f = 1/T
print(f)


#Loading the data
data = np.loadtxt( 'es17btech11002.dat' )
#PLotting the data from spice simulation
plt.plot(data[:,0],data[:,1])
plt.grid()
plt.xlim(0.03,0.04)
plt.ylim(-0.7,0.7)
plt.xlabel('time')
plt.ylabel('Vout')
plt.title('Output (spice simulation)')
plt.plot([0.03,0.04],[0,0],'r--',lw=1)

plt.axhline(y = -0.47,xmin=0,xmax= 6.438,color = 'r',linestyle='dashed')
plt.axvline(x = 2.03,ymin=0,color='k',linestyle='dashed')


plt.plot(0.031316,0,'o')
plt.plot(0.03060,0,'o')
plt.legend()


#if using termux
plt.savefig('./figs/es17btech11002/es17btech11002_spice2.pdf')
plt.savefig('./figs/es17btech11002/es17btech11002_spice2.eps')
subprocess.run(shlex.split("termux-open ./figs/es17btech11002/es17btech11002_spice2.pdf"))
#else
#plt.show()