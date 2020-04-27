#Code by P.Aditya
#April 18th,2020
#Released under GNU GPL

import control
import matplotlib.pyplot as plt
#if using termux
import subprocess
import shlex
#end if


num = [-1,1]  #numerator coefficients of G(s)
den = [2,4]	  #denominator coefficients of G(s)

#Creating a transfer function G = num/den
G = control.tf(num,den) 

control.nyquist(G)
#plotting the nyquist plot
plt.grid(True)
plt.title('Nyquist Diagram of G(s)')
plt.xlabel('Re(G(s))')
plt.ylabel('Im(G(s))')

#if using termux
plt.savefig('./figs/ee18btech11034.pdf')
plt.savefig('./figs/ee18btech11034.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11034.pdf"))
#else
#plt.show()
