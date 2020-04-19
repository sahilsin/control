#Coded by J. Prabhath
#14th April, 2020
#Released under GNU GPL

import matplotlib.pyplot as plt
from scipy import signal

s1 = signal.lti([1],[3,1,0])
s2 = signal.lti([1],[1,1,0])
w,mag1,phase1 = signal.bode(s1)
_,mag2,phase2 = signal.bode(s2)

plt.xlabel('Frequency (in rad/s)')
plt.ylabel('Phase (in deg)')
plt.title('Phase plot')
plt.semilogx(w,phase2, label = 'With Compensator')
plt.semilogx(w,phase1, label = 'Without Compensator')
plt.grid()
plt.legend()
plt.show()
