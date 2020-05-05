import subprocess
import shlex
from scipy import signal
import matplotlib.pyplot as plt
from pylab import *

#      Original Signal
s = signal.lti([25], [1, 6, 5, 0])

#     Compensated transfer function
s1 = signal.lti([25*0.5, 25], [1*0.0074, 1+6*0.0074, 6+5*0.0074, 5, 0]) 

#     Compensator transfer function
#s = signal.lti([0.5, 1], [0.0074, 1])   


w,mag,phase = signal.bode(s)
w1,mag1,phase1 = signal.bode(s1)

subplot(2,1,1)
plt.xlabel('Frequency(rad/s)')
plt.ylabel('Magnitude(deg)')
plt.semilogx(w, mag,'b-')
plt.semilogx(w1, mag1,'r-')
plt.legend(['Uncompensated', 'Compensated'])
#plt.axvline(x = 2.038,ymin=0,color='k',linestyle='dashed')
#plt.plot(2.038,0,'o')
plt.grid() 

subplot(2,1,2)
plt.xlabel('Frequency(rad/s)')
plt.ylabel('Phase(deg)')
plt.semilogx(w,phase,'b-')
plt.semilogx(w1,phase1,'r-')
plt.legend(['Uncompensated', 'Compensated'])
#plt.axvline(x = 2.038,ymin=0,color='k',linestyle='dashed')    
plt.axhline(y = -180,xmin=0,color = 'r',linestyle='solid')
plt.grid()

#If termux
plt.savefig('./figs/ee18btech11051/ee18btech11051_fig1.pdf')
plt.savefig('./figs/ee18btech11051/ee18btech11051_fig1.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11051/ee18btech11051_fig1.pdf"))

#else
#plt.show()
