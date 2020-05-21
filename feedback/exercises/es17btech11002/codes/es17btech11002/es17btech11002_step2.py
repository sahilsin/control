from scipy import signal
import matplotlib.pyplot as plt
from pylab import*

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
plt.title("Step system response ")

#if using termux
plt.savefig('./figs/es17btech11002/step2.pdf')
plt.savefig('./figs/es17btech11002/step2.eps')
subprocess.run(shlex.split("termux-open ./figs/es17btech11002/step2.pdf"))
#else
#plt.show()
