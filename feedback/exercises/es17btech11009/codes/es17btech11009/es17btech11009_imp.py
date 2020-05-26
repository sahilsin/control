# -*- coding: utf-8 -*-
"""
Created on Tue May 26 09:52:22 2020

@author: Hrithik
"""

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex
#end if

G = 1
num = [0,-0.01,0.05]		#describing transfer function
den = [0.0001,0,1]
system = signal.lti(num,den)

T, yout = signal.impulse(system)	#oscillating response

plt.plot(T,yout)
plt.grid()
plt.xlabel("time (t)")
plt.title("Impulse system response ")
#if using termux
plt.savefig('./figs/es17btech11009/es17btech11009_imp.pdf')
plt.savefig('./figs/es17btech11009/es17btech11009_imp.eps')
subprocess.run(shlex.split("termux-open ./figs/es17btech11009/es17btech11009_imp.pdf"))
#else
#plt.show()