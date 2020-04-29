#Code by  P.Aashrith
#April 28, 2020
#Released under GNU GPL

import control
import numpy as np
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex
#end if

num = 4
den = [1,3,2,0]
[n1,d1]=control.pade(0.1744,10)   #Creating delay of 0.1744
[n2,d2]=control.pade(0.5,10)	#Creating delay of 0.5
[n3,d3]=control.pade(0.0005,10)	#Creating delay of 0.0005

#Creating a transfer function G = num/den
G = control.tf(num,den) 
G1=control.tf(n1,d1)
G2=control.tf(n2,d2)
G3=control.tf(n3,d3)

#assigning delay to system G
G4=G*G1 
G5=G*G2
G6=G*G3

#plotting nyquist plot with variable tau
control.nyquist(G4,label='$t=0.1744$')
control.nyquist(G5,label='$t=0.5$')
control.nyquist(G6,label='$t=0.0005$')
plt.grid(True)
plt.xlim(-4,0)
plt.ylim(-2,2)
plt.legend()
plt.annotate("-1+0j",(-1,0))
plt.xlabel('Re(s)')
plt.ylabel('Im(s)')
#if using termux
plt.savefig('./figs/ee18btech11035/ee18btech11035_1.pdf')
plt.savefig('./figs/ee18btech11035/ee18btech11035_1.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11035/ee18btech11035_1.pdf"))
#else
#plt.show()
