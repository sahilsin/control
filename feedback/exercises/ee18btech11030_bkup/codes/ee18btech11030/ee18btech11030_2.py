###################################################################

# This is python code for Bode plots.    
# By Moparthi Varun Sankar
# May 13 , 2020 
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
s1 = signal.lti([0.1*5,0], [1, 2*5,25])               
s2 = signal.lti([0.686*5,0], [1,  1.4142135*5,25])
s3 = signal.lti([2.1*5,0], [1, 0,25])
plt.figure()
t2,s2 = step(s2)
t1,s1 = step(s1)
t3,s3 = step(s3)


plt.title("Time responses")
plt.plot(t1,s1,label = "Poles are coincident K = 0.1")
plt.plot(t2,s2,label = "Maximally flat response K = 0.686")
plt.plot(t3,s3,label = "Oscillating response K = 2.1")
plt.grid()
plt.legend()



#if using termux
plt.savefig('./figs/ee18btech11030/ee18btech11030_fc2.pdf')
plt.savefig('./figs/ee18btech11030/ee18btech11030_fc2.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11030/ee18btech11030_fc2.pdf"))
#else
#plt.show()
