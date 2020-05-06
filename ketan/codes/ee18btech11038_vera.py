import subprocess
import shlex
from scipy import signal
import matplotlib.pyplot as plt
import control.matlab as ml
from math import *

k= 3.38132966133896   #substituted K
RN = 38  #roll no.

#Defining the transfer function  T(s)
#Since the transfer function T(s) is  (s+2)/(s^4 + 12s^3 + 47s^2 + 60s)
s1 = signal.lti([1*k, 2*k],[1, 12,47,60,0])
w,mag,phase = signal.bode(s1)

#Wpc -phase crossover freq. using builtin functions
s= ml.tf('s')
gm, pm, Wpc, Wgc = ml.margin((k*s+2*k)/(s**4 + 12*s**3 + 47*s**2 + 60*s))

#Verifying Gain Margin of G(s)
gm = 20*log10(gm)
print('Gain Margin of G(s) =',gm, ', when K is substituted')


plt.subplot(2,1,1)
plt.semilogx(w, mag,'b', label='_nolegend_')        # Bode Magnitude plot
plt.plot(Wpc,-38,'o', label='_nolegend_')
plt.xlabel('Frequency(rad/s)')
plt.ylabel('Mag')
plt.axhline(y = -RN,xmin=0,xmax= Wpc,color = 'b',linestyle='dashed')
plt.axvline(x = Wpc, ymin = 0, ymax= 0.56 ,color='k', linestyle='dashed')
plt.text(1.0,-60, '({}, {})'.format(round(Wpc,2),-38))
plt.legend(['-38 dB line'], loc= 'lower left')
plt.grid() 


plt.subplot(2,1,2)
plt.semilogx(w,phase, label='_nolegend_')  #Bode Pahse plot
plt.plot(Wpc,-180,'o', label='_nolegend_')
plt.subplot(2,1,2)
plt.xlabel('Frequency(rad/s)')
plt.ylabel('Phase(deg)')
plt.axhline(y = -180,xmin=0,xmax= Wpc,color = 'r',linestyle='dashed')
plt.axvline(x = Wpc, ymin = 0.5, ymax= 1 ,color='k', linestyle='dashed')
plt.legend(['-180 deg line'], loc= 'lower left')
plt.text(Wpc,-170, '({}, {})'.format(round(Wpc, 2),-180))
plt.grid() 


plt.savefig('./figs/ee18btech11038/ee18btech11038_vera.pdf')
plt.savefig('./figs/ee18btech11038/ee18btech11038_vera.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11038/ee18btech11038_vera.pdf"))

#plt.show()