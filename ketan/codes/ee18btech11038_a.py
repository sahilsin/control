import subprocess
import shlex
from scipy import signal
import matplotlib.pyplot as plt
import control.matlab as ml
from math import *

RN = 38  #roll no.

#Defining the transfer function  T(s)
#Since the transfer function T(s) is  (s+2)/(s^4 + 12s^3 + 47s^2 + 60s)
s1 = signal.lti([1, 2],[1, 12,47,60,0])
w,mag,phase = signal.bode(s1)

#Gain margin, Wpc -phase crossover freq. using builtin functions
s= ml.tf('s')
gm, pm, Wpc, Wgc = ml.margin((s+2)/(s**4 + 12*s**3 + 47*s**2 + 60*s))

#Gain(in dB) of T(s) at Wpc
gain_at_Wpc = -20*log10(gm)


plt.subplot(2,1,1)
plt.semilogx(w, mag,'b', label='_nolegend_')        # Bode Magnitude plot
plt.plot(Wpc,gain_at_Wpc,'o', label='_nolegend_')
plt.xlabel('Frequency(rad/s)')
plt.ylabel('Mag')
plt.axhline(y = -RN,xmin=0,xmax= Wpc,color = 'b',linestyle='dashed')
plt.text(1.2,-80, '({}, {})'.format(round(Wpc,2),round(gain_at_Wpc,2)))
plt.axvline(x = Wpc, ymin = 0.53, ymax= 0.625 ,color='k')
plt.text(Wpc+1,-53, 'len=20log(K)')     #len = length of black line
plt.legend(['-38 dB line'], loc= 'lower left')
plt.grid() 


plt.subplot(2,1,2)
plt.semilogx(w,phase, label='_nolegend_')  #Bode Pahse plot
plt.plot(Wpc,-180,'o', label='_nolegend_')
plt.subplot(2,1,2)
plt.xlabel('Frequency(rad/s)')
plt.ylabel('Phase(deg)')
plt.axhline(y = -180,xmin=0,xmax= Wpc,color = 'r',linestyle='dashed')
plt.legend(['-180 deg line'], loc= 'lower left')
plt.text(Wpc,-170, '({}, {})'.format(round(Wpc, 2),-180))
plt.grid() 


print('K = '  , pow(10, abs(gain_at_Wpc+RN)/20))

plt.savefig('./figs/ee18btech11038/ee18btech11038_a.pdf')
plt.savefig('./figs/ee18btech11038/ee18btech11038_a.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11038/ee18btech11038_a.pdf"))

#plt.show()