#if using termux
import subprocess
import shlex
#end if


import numpy as np
import matplotlib.pyplot as plt 
import control

#Creating the log space
f = np.logspace(-3,3,1000)
w = 2*np.pi*f

#Defining the Transfer function
Gs = control.TransferFunction([100,600,800,0],[1,97,610,800])

out = control.bode(Gs,w,dB=1,deg=1)

#if using termux
plt.savefig('./figs/ee18btech11045/ee18btech11045_bode1.pdf')
plt.savefig('./figs/ee18btech11045/ee18btech11045_bode1.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11045/ee18btech11045_bode1.pdf"))
#else
#plt.show()