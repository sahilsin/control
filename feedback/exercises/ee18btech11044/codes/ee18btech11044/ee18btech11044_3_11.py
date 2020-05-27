import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

RC = 160 *(10**-6)

#if using termux
import subprocess
import shlex
#end

num = [2.5*(RC**2),7.5*RC,2.5]	#describing transfer function
den = [(RC**2),(1.5)*RC,1]
system = signal.lti(num,den)


T, yout = signal.impulse(system)	#impulse response

plt.plot(T,yout)
plt.grid()
plt.xlabel("time (t)")
plt.title("Impulse system response -- R2/R1 = 1.5")

#if using termux
plt.savefig('./figs/ee18btech11044/ee18btech11044_3_14.pdf')
plt.savefig('./figs/ee18btech11044/ee18btech11044_3_14.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11044_3_14.pdf"))
#plt.show()
