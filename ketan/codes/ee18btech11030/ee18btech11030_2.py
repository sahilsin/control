###################################################################

# This is python code for Bode plots.    
# By Moparthi Varun Sankar
# April 28 , 2020 
# Released under GNU GPL

###################################################################
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.signal import  step

#if using termux
import subprocess
import shlex
#endif

#closed loop TF's
s1 = signal.lti([1473,30933,162030], [11, 18 ,1572,31095,162030])  #uncompensated system              
s2 = signal.lti([16200,342160.2,1823164.2,215622],[8296.2,149333,821522+16200,1344116.2+342160.2,1823164.2,215622])  #compensated system

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


#if using termux
plt.savefig('./figs/ee18btech11030/ee18btech11030_3.pdf')
plt.savefig('./figs/ee18btech11030/ee18btech11030_3.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11030/ee18btech11030_3.pdf"))
#else
#plt.show()
