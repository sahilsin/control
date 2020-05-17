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
#          3.03*0.0625s^2 + 3.03*0.75s + 3.03
#  T{s}=   ----------------------------------
#               0.0625s^2 - 0.0075s + 1
#
# # # # # # # # # # # # # # # # # # # # # # # # # # #
num = [3.03*0.0625, 3.03*0.75, 3.03]	
den = [0.0625,-0.0075,1]
system = signal.lti(num,den)
T, yout = signal.step(system)	#oscillating response

plt.plot(T,yout)
plt.grid()

plt.xlabel("time (t)")
plt.title("Oscillating system response ")

#if using termux
plt.savefig('./figs/es17btech11002/es17btech11002.pdf')
plt.savefig('./figs/es17btech11002/es17btech11002.eps')
subprocess.run(shlex.split("termux-open ./figs/es17btech11002/es17btech11002.pdf"))
#else
#plt.show()
