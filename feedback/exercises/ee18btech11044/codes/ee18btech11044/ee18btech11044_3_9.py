import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

RC = 160 *(10**-6)

#if using termux
import subprocess
import shlex
#end

num = [9*(RC**2),27*RC,9]	#describing transfer function
den = [(RC**2),(-7)*RC,1]
system = signal.lti(num,den)


T, yout = signal.step(system)	#step response

plt.plot(T,yout)
plt.grid()
plt.xlabel("time (t)")
plt.title("Step system response -- R2/R1 = 9")

#if using termux
plt.savefig('./figs/ee18btech11044/ee18btech11044_3_11.pdf')
plt.savefig('./figs/ee18btech11044/ee18btech11044_3_11.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11044_3_11.pdf"))
#plt.show()
