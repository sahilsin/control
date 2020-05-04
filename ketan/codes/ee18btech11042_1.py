#if using termux
import subprocess
import shlex
#end if

import control
import matplotlib.pyplot as plt
import numpy as np
G1 = control.tf([1],[1,2,2,2,1]) 
G2 = control.tf([1],[1,2,0,0,-1]) 
G3 = control.tf([1],[1,2,1,1,0]) 
w = np.linspace(-50,50,5000)
control.nyquist(G1,w,label='k=1'); 
control.nyquist(G2,w,label='k=-1');
control.nyquist(G3,w,label='k=0');
plt.legend()
#if using termux
plt.savefig('./figs/ee18btech11042_1.pdf')
plt.savefig('./figs/ee18btech11042_1.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11042_1.pdf"))
#else
#plt.show()

plt.show()

