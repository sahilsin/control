#Code by Tejaswini
#Date 8 May,2020

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex
#end if

G = 3
num = [3*0.0625,3*0.75,3]		#describing transfer function
den = [0.0625,0,1]
system = signal.lti(num,den)

T, yout = signal.step(system)	#oscillating response

plt.plot(T,yout)
plt.grid()
plt.xlabel("time (t)")
plt.title("Oscillating system response ")

#if using termux
plt.savefig('./figs/ee18btech11047/ee18btech11047.pdf')
plt.savefig('./figs/ee18btech11047/ee18btech11047.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11047/ee18btech11047.pdf"))
#else
#plt.show()

