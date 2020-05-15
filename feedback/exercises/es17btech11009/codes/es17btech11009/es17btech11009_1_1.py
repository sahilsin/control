import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex
#end if

G = 50                  #High gain
num = [0,-1,0.05]		#describing transfer function
den = [1,-0.05,1]
system = signal.lti(num,den)

T, yout = signal.step(system)	#oscillating response

plt.plot(T,yout)
plt.grid()
plt.xlabel("time (t)")
plt.title("Oscillating system response ")

#if using termux
plt.savefig('./figs/es17btech11009/es17btech11009_1_1.pdf')
plt.savefig('./figs/es17btech11009/es17btech11009_1_1.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11047/es17btech11009_1_1.pdf"))
#else
#plt.show()