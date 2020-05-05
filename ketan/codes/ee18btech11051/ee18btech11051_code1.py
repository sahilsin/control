import subprocess
import shlex
from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
from pylab import *

alpha = 5
t = 1/(5*2.6)

#      Original Signal
s = signal.lti([25], [1, 6, 5, 0])

#     Single Pass Compensated transfer function
s1 = signal.lti([25*1, 25], [1*0.0074*2, 1+6*0.0074*2, 6+5*0.0074*2, 5, 0])

#	  Double Pass Compensated transfer function
s2 = signal.lti(25*np.polymul([alpha*t, 1],[alpha*t, 1]),np.polymul([t, 1], np.polymul([1, 6, 5, 0], [t, 1])))

#     Compensator transfer function
#s = signal.lti([0.5, 1], [0.0074, 1])   


w,mag,phase = signal.bode(s)
w1,mag1,phase1 = signal.bode(s1)
w2,mag2,phase2 = signal.bode(s2)

plt.subplot(2,1,1)
plt.xlabel('Frequency(rad/s)')
plt.ylabel('Magnitude(deg)')
plt.semilogx(w, mag,'b-')
plt.semilogx(w1, mag1,'r-')
plt.semilogx(w2, mag2,'k-')
#plt.axvline(x = 2.038,ymin=0,color='k',linestyle='dashed')
plt.legend(['Uncompensated', 'Single Pass', 'Double Pass'])
#plt.plot(2.038,0,'o')
plt.grid() 

subplot(2,1,2)
plt.xlabel('Frequency(rad/s)')
plt.ylabel('Phase(deg)')
plt.semilogx(w,phase,'b-')  
plt.semilogx(w1,phase1,'r-') 
plt.semilogx(w2,phase2,'k-') 
plt.legend(['Uncompensated', 'Single Pass', 'Double Pass'])  
#plt.axvline(x = 2.038,ymin=0,color='k',linestyle='dashed')       # Bode phase plot
plt.axhline(y = -180,xmin=0,color = 'r',linestyle='dashed')
plt.grid() 

#If termux
plt.savefig('./figs/ee18btech11051/ee18btech11051_fig3.pdf')
plt.savefig('./figs/ee18btech11051/ee18btech11051_fig3.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11051/ee18btech11051_fig1.pdf"))

#else
#plt.show()
