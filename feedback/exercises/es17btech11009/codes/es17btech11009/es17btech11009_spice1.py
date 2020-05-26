# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex
#end

T = 3.3801-3.317
f = 1/T
print(f)


#Loading the data
data = np.loadtxt( 'es17btech11009.dat' )
#PLotting the data from spice simulation
plt.plot(data[:,0],data[:,1],label='Oscillator output')
plt.xlim(3,3.5)
plt.ylim(-5,5)
plt.xlabel('time')
plt.ylabel('Vout')
plt.title('Output from Oscillator')
plt.plot([3,3.5],[0,0],'r--',lw=1,label ='0V')
plt.plot(3.3801,0,'o')
plt.plot(3.317,0,'o')
plt.legend()

#if using termux
plt.savefig('./figs/es17btech11009/es17btech11009_spice1.pdf')
plt.savefig('./figs/es17btech11009/es17btech11009_spice1.eps')
subprocess.run(shlex.split("termux-open ./figs/es17btech11009/es17btech11009_spice1.pdf"))
#else
#plt.show()