import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
#if using termux
import subprocess
import shlex
#end

RC = 160 *(10**-6)


num = [9*(RC**2),27*RC,9]	#describing transfer function
den = [(RC**2),(-7)*RC,1]
system = signal.lti(num,den)

T, yout = signal.impulse(system)	#Impluse response

plt.plot(T,yout)
plt.grid()
plt.xlabel("time (t)")
plt.title("Impulse system response -- R2/R1 = 9")
#if using termux
plt.savefig('./figs/ee18btech11044/ee18btech11044_3_10.pdf')
plt.savefig('./figs/ee18btech11044/ee18btech11044_3_10.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11044_3_10.pdf"))
#plt.show()
