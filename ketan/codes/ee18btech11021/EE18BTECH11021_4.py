#Coded by J. Prabhath
#14th April, 2020
#Released under GNU GPL

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

K = 96
Kp = 1
Ti = 2.713

s1 = signal.lti([-1/Ti],[0,0,-2,-4,-6], K)
s2 = signal.lti([],[0,-2,-4,-6], K)
w,mag1,phase1 = signal.bode(s1)
_,mag2,phase2 = signal.bode(s2)

plt.xlabel('Freq (in rad/s)')
plt.ylabel('Phase (in deg)')
plt.title('Phase plot')
plt.semilogx(w,phase1, label = 'With Controller')
plt.semilogx(w,phase2, label = 'Without Controller')
plt.grid()
plt.legend()
plt.show()
