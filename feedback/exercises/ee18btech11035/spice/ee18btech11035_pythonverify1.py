# License
'''
Code by Aashrith
May 19th,2020
Released under GNU GPL
'''

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import control

#if using termux
import subprocess
import shlex
#end if

num = [2*np.pi*10**6]		#describing transfer function
den = [1,20*np.pi]
closedlooptf = control.TransferFunction(num,den)

T = np.linspace(0,0.1,1000)
T,yout = control.step_response(closedlooptf,T)	
plt.plot(T,yout)
plt.grid()
plt.xlabel("time(sec)")
plt.ylabel("Open loop circuit step response")
plt.title("Python Verification of Open-loop")


#if using termux
#plt.savefig('./figs/ee18btech11035/ee18btech11035_spice_verify1.pdf')
#plt.savefig('./figs/ee18btech11035/ee18btech11035_spice_verify1.eps')
#subprocess.run(shlex.split("termux-open ./figs/ee18btech11035/ee18btech11035_pythonverify1.pdf"))
#else
plt.show()
