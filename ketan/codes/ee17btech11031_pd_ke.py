# License
'''
Code by Pranjal Singh
April 26,2020
Released under GNU GPL
'''

import matplotlib.pyplot as plt
from scipy import signal

#if using termux
import subprocess
import shlex
#end if

KKp = 3.87
Td = -0.71

s1 = signal.lti([-1/Td],[0,-1], KKp)
s2 = signal.lti([],[0,-1], KKp)
w,mag1,phase1 = signal.bode(s1)
_,mag2,phase2 = signal.bode(s2)

plt.xlabel('Freq (in rad/s)')
plt.ylabel('Phase (in deg)')
plt.title('Phase plot')
plt.semilogx(w,phase1, label = 'With Controller')
plt.semilogx(w,phase2, label = 'Without Controller')
plt.grid()
plt.legend()

#if using termux
plt.savefig('./figs/ee17btech11031_pd_ke.pdf')
plt.savefig('./figs/ee17btech11031_pd_ke.eps')
subprocess.run(shlex.split("termux-open ./figs/ee17btech11031_pd_ke.pdf"))
#else
#plt.show()
