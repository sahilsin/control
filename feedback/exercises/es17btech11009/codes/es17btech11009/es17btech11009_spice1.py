# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex
#end

T = 15.3738 - 15.0569
f = 1/T
print(f)



#Loading the data
data = np.loadtxt( 'es17btech11009.dat' )
#PLotting the data from spice simulation
plt.plot(data[:,0],data[:,1],label="Oscillating output")
plt.xlim(15,17)
plt.ylim(-5,5)
plt.plot([15,17],[0,0],'r--',lw=1,label ='0V')
plt.plot(15.3738,0,'o')
plt.plot(15.0569,0,'o')
plt.legend()
plt.xlabel('time')
plt.ylabel('Vout')
plt.title('Output from spice simulation')

#if using termux
plt.savefig('./figs/es17btech11009/es17btech11009_spice1.pdf')
plt.savefig('./figs/es17btech11009/es17btech11009_spice1.eps')
subprocess.run(shlex.split("termux-open ./figs/es17btech11009/es17btech11009_spice1.pdf"))
#else
#plt.show()