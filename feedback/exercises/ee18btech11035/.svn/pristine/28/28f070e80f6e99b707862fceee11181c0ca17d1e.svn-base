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
den = [1,20*np.pi*1001]
closedlooptf = control.TransferFunction(num,den)

T = np.linspace(0,0.001,1000)
T,yout = control.step_response(closedlooptf,T)	
plt.plot(T,yout)
plt.grid()
plt.xlabel("time(sec)")
plt.ylabel("Closed loop circuit step response")
plt.title("Python verification of closed loop")


#if using termux
#plt.savefig('./figs/ee18btech11035/ee18btech11035_spice_verify1.pdf')
#plt.savefig('./figs/ee18btech11035/ee18btech11035_spice_verify1.eps')
#subprocess.run(shlex.split("termux-open ./figs/ee18btech11035/ee18btech11035_pythonverify2.pdf"))
#else
plt.show()
