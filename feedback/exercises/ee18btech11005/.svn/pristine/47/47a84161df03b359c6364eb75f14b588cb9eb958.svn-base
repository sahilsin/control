#Code by B.Varuni
#Date 4 May,2020
#Released Under GNU GPL

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex
#end if

gain = [7.816*10**12]
char_eq =[1,125*10**4,7.816*10**11]		
num = []
zeros=np.roots(num)
poles=np.roots(char_eq)
Transfer_function = signal.lti(zeros,poles,np.array([gain]))
T, ystep = signal.step(Transfer_function)	
plt.plot(T,ystep)
plt.grid()
plt.title("Step response")
plt.xlabel("Time")
plt.ylabel("y(t)")
#if using termux
#plt.savefig('./figs/ee18btech11005/ee18btech11005_2.pdf')
#plt.savefig('./figs/ee18btech11005/ee18btech11005_2.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11005/ee18btech11005_3.pdf"))
#else
#plt.show()
