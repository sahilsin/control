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
RC = 160 *(10**-6)
#closed loop TF's

s3 = signal.lti([2.13*(RC**2),2.13*2.13*RC,2.13], [(RC**2),(-0.03)*RC,1])
plt.figure()

t3,s3 = step(s3)


plt.title("Time response")

plt.plot(t3,s3,label = "Oscillating response K = 2.1")
plt.grid()
plt.legend()



#if using termux
plt.savefig('./figs/ee18btech11030/ee18btech11030_fc2.pdf')
plt.savefig('./figs/ee18btech11030/ee18btech11030_fc2.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11030/ee18btech11030_fc2.pdf"))
#else
#plt.show()
