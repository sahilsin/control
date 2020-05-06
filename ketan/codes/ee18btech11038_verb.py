import subprocess
import shlex
from scipy import signal
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import control.matlab as ml
from math import *

k = 86.8753439248997

#Defining the transfer function  T(s)
#Since the transfer function T(s) is  (s+2)/(s^4 + 12s^3 + 47s^2 + 60s)
s1 = signal.lti([1*k, 2*k],[1, 12,47,60,0])

#signal.bode takes transfer function as input and returns frequency,magnitude and phase arrays
w,mag,phase = signal.bode(s1)



#Wgc using builtin functions
s= ml.tf('s')
gm, pm, Wpc, Wgc = ml.margin((s*k+2*k)/(s**4 + 12*s**3 + 47*s**2 + 60*s))
print('Wgc = ', Wgc, ' which matches the graphical solution')
print('PM =',pm, 'which is close to 40 degrees')

# phase of G(s) at Wgc
phase_at_Wgc = -180 +pm.round()  

plt.subplot(2,1,1)
plt.semilogx(w, mag,'b', label='_nolegend_')        # Bode Magnitude plot
plt.plot(Wgc,0,'o', label='_nolegend_')
plt.xlabel('Frequency(rad/s)')
plt.ylabel('Mag')
plt.axhline(y = 0,xmin=0,xmax= 1,color = 'b',linestyle='dashed')
plt.axvline(x = Wgc, ymin = 0, ymax= 0.6 ,color='k', linestyle='dashed')
plt.text(1,-30, '({}, {})'.format(Wgc.round(2), 0))
plt.legend(['0 dB line'], loc= 'lower left')
plt.grid() 


plt.subplot(2,1,2)
plt.semilogx(w,phase, label='_nolegend_')    #Bode phase plot
plt.plot(Wgc,-140,'o', label='_nolegend_')
plt.xlabel('Frequency(rad/s)')
plt.ylabel('Phase(deg)')
plt.axhline(y= phase_at_Wgc,xmin=0,xmax= 1,color = 'r',linestyle='dashed')
plt.axvline(x = Wgc, ymin = 0.7, ymax= 1 ,color='k', linestyle='dashed')
plt.text(0.5,-170, '({}, {})'.format(Wgc.round(2),phase_at_Wgc))
plt.legend(['-140 deg line'], loc= 'lower left')
plt.grid() 


plt.savefig('./figs/ee18btech11038/ee18btech11038_verb.pdf')
plt.savefig('./figs/ee18btech11038/ee18btech11038_verb.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11038/ee18btech11038_verb.pdf"))

#plt.show()
