import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex
#end if

# # # # # # # # # # # # # # # # # # # # # # # # # # #
#                  Transfer function     
#
#          3*0.0625s^2 + 3*0.75s + 3
#  T{s}=   ----------------------------------
#               0.0625s^2 - 0s + 1
#
# # # # # # # # # # # # # # # # # # # # # # # # # # #
G = 3
num = [3*0.0625,3*0.75,3]		#describing transfer function
den = [0.0625,0,1]
system = signal.lti(num,den)

T, yout = signal.step(system)	#oscillating response

plt.plot(T,yout)
plt.grid()

plt.xlabel("time (t)")
plt.title("Step system response ")

#if using termux
plt.savefig('./figs/es17btech11002/step1.pdf')
plt.savefig('./figs/es17btech11002/step1.eps')
subprocess.run(shlex.split("termux-open ./figs/es17btech11002/step1.pdf"))
#else
#plt.show()
