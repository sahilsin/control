import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex
#end if

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                         #
#                                                         #
#          3.03*0.0001*0.0001*s^2 + 3.03*0.0001s+ 3.03    #
# T(s)=   ----------------------------------              #
#               (0.0001*0.0001)s^2 -0.000003s +1          #
#                                                         #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
num = [3.03*0.0001*0.0001, 3.03*3*0.0001, 3.03]	
den = [0.0001*0.0001,0,1]
system = signal.lti(num,den)
T, yout = signal.step(system)	#oscillating response
plt.plot(T,yout)
plt.grid()
plt.xlabel("time (t)")
plt.title("Oscillating system response ")
plt.xlim(0, 3.2)
plt.ylim(-15,15)
#plt.plot(data[:,0],data[:,1])  

#if using termux
plt.savefig('./figs/es17btech11002/es17btech11002.pdf')
plt.savefig('./figs/es17btech11002/es17btech11002.eps')
subprocess.run(shlex.split("termux-open ./figs/es17btech11002/es17btech11002.pdf"))
#else
#plt.show()