#Code by C Shruti
#Date 16 May,2020import numpy as np

from scipy import signal
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex
#end if

V=np.linspace(0,10,11,dtype=int)
vout=np.zeros(11)
for i in range(len(V)):
	num=[V[i]*10**7,V[i]*2*10**(11),V[i]*10**15]
	den=[1,3*(10**4),3*(10**8),2*(10**12),0]
	system=signal.lti(num,den)
	T,yout=signal.step(system)
	vout[i]=yout[14]
plt.plot(V,vout) #considering value at t=1
plt.grid()
plt.xlabel('Input Voltage')
plt.ylabel('Output of system')
plt.title('Time domain output')

#if using termux
plt.savefig('./figs/ee18btech11006/ee18btech11006_9.pdf')
plt.savefig('./figs/ee18btech11006/ee18btech11006_9.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11006/ee18btech11006_9.pdf"))
#else
#plt.show()

