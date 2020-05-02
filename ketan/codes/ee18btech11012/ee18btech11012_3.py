import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.signal import  step

#if using termux
import subprocess
import shlex
#endif


s1 = signal.lti([75000,75000*7], [7,140,75525,75000*7,0])  #Uncompensated system

s2 = signal.lti([10714.29,10714.29*(29.23+7.753+7),10714.29*(29.23*7.753+7.753*7+7*29.23),10714.29*(29.23*7.753*7)],[1,226.802,4437.7214+10714.29,18910.371+10714.29*(29.23+7.753+7),(205.7*15*5*1.102)+10714.29*(29.23*7.753+7.753*7+7*29.23),10714.29*(29.23*7.753*7)])  #compensated system

plt.figure()
t2,s2 = step(s2)
t1,s1 = step(s1)
plt.subplot(2,1,1)
plt.title("Time responses")
plt.plot(t1,s1,label = "Uncompensated")
plt.grid()
plt.legend()
plt.subplot(2,1,2)
plt.plot(t2,s2,label = "Compensated")
plt.grid()
plt.legend()
plt.show()


#if using termux
plt.savefig('./figs/ee18btech11012/ee18btech11012_3.pdf')
plt.savefig('./figs/ee18btech11012/ee18btech11012_3.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11012/ee18btech11012_3.pdf"))
#else
#plt.show()
