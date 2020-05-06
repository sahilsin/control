import subprocess
import shlex
from scipy import signal
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import control.matlab as ml
from math import *

#Defining the transfer function  T(s)
#Since the transfer function T(s) is  (s+2)/(s^4 + 12s^3 + 47s^2 + 60s)
s1 = signal.lti([1, 2],[1, 12,47,60,0])

#signal.bode takes transfer function as input and returns frequency,magnitude and phase arrays
w,mag,phase = signal.bode(s1)

#Finding frequency at which phase =-140 degree
#Can't be done using builtin Wgc function since K is unknown
#Using interpolation
s= ml.tf('s')
freq_as_fn_of_w = interp1d(phase, w)
Wgc = freq_as_fn_of_w(-140)

#Evaluating Gain of T(s) at Wgc of G(s)
gain_at_Wgc = 20*log10(abs(ml.evalfr(((s+2)/(s**4 + 12*s**3 + 47*s**2 + 60*s)), complex(0,Wgc))))


plt.subplot(2,1,1)
plt.semilogx(w, mag,'b', label='_nolegend_')        # Bode Magnitude plot
plt.plot(Wgc,gain_at_Wgc,'o', label='_nolegend_')
plt.xlabel('Frequency(rad/s)')
plt.ylabel('Mag')
plt.axhline(y = 0,xmin=0,xmax= 1,color = 'b',linestyle='dashed')
plt.text(1,-70, '({}, {})'.format(Wgc.round(2), round(gain_at_Wgc,2)))
plt.axvline(x = Wgc, ymin = 0.60, ymax= 0.88 ,color='k')
plt.text(Wgc+0.5,-25, 'len=20log(K)')  #len = length of black line
plt.legend(['0 dB line'], loc= 'lower left')
plt.grid() 


plt.subplot(2,1,2)
plt.semilogx(w,phase, label='_nolegend_')    #Bode phase plot
plt.plot(Wgc,-140,'o', label='_nolegend_')
plt.xlabel('Frequency(rad/s)')
plt.ylabel('Phase(deg)')
plt.axhline(y = -140,xmin=0,xmax= 1,color = 'r',linestyle='dashed')
plt.text(0.5,-170, '({}, {})'.format(Wgc.round(2),-140))
plt.legend(['-140 deg line'], loc= 'lower left')
plt.grid() 

#print K
print('K=', pow(10,(abs(gain_at_Wgc-0)/20)))


plt.savefig('./figs/ee18btech11038/ee18btech11038_b.pdf')
plt.savefig('./figs/ee18btech11038/ee18btech11038_b.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11038/ee18btech11038_b.pdf"))

#plt.show()