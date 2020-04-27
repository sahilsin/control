import numpy as np
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex
#end if

root3=np.sqrt(3)
t=np.linspace(0,2,100)
a=np.exp(-5*t)
b=np.cos(5*root3*t)
d=np.sin(5*root3*t)
C=(-((51/50)*b)-((17*root3/50)*d))*a+1.02
val = round(1.02,2)

plt.figure()
plt.plot(t, C,label="step response")
plt.hlines(val, xmin = 0, xmax = 2, color = 'red',label="steady state")
plt.xlabel('$t$')
plt.ylabel('$c(t)$')
plt.grid()
plt.legend()


#if using termux
plt.savefig('./figs/es17btech11015.pdf')
plt.savefig('./figs/es17btech11015.eps')
subprocess.run(shlex.split("termux-open ./figs/es17btech11015.pdf"))
#else
#plt.show()
