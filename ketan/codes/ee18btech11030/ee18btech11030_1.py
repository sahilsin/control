###################################################################

# This is python code for Bode plots.    
# By Moparthi Varun Sankar
# April 28 , 2020 
# Released under GNU GPL

###################################################################

from scipy import signal
import matplotlib.pyplot as plt
from pylab import*


#if using termux
import subprocess
import shlex
#end if

#Defining the transfer function 
s1 = signal.lti([16200,21*16200,110*16200], [11, 18*11 ,99*11,162*11,0])  #G(s)
s2 = signal.lti([1,0.121], [754.223*1,754.223*0.0001604])                 #Gc(s)
s3 = signal.lti([16200,342160.2,1823164.2,215622],[8296.2,149333,821522,1344116.2,215.6,0])  #G(s)*Gc(s)

#signal.bode takes transfer function as input and returns frequency,magnitude and phase arrays
w1,mag1,phase1 = signal.bode(s1,n=1000)
w2,mag2,phase2 = signal.bode(s2,n=1000)
w3,mag3,phase3 = signal.bode(s3,n=1000)

plt.figure()
plt.subplot(2,1,1)
plt.grid()
plt.xlabel('Frequency(rad/s)')
plt.ylabel('Magnitude(db)')
plt.semilogx(w1, mag1,label='Uncompensated')      # Magnitude plot for G(s)
plt.semilogx(w2, mag2,label='Compensator')        # Magnitude plot for Gc(s)
plt.semilogx(w3, mag3,label='Compensated')        # Magnitude plot for G(s)*Gc(s)
plt.plot(38.95,0,'o')
plt.text(38.95,0, '({}, {})'.format(38.95,0))
plt.plot(0.0001604,0,'o')
plt.text(0.0001604,0, '({}, {})'.format(0.0001604,0))
plt.plot(0.121,-57.55,'o')
plt.text(0.121,-57.55, '({}, {})'.format(0.121,-57.55))
plt.plot(1.21,0,'o')
plt.text(1.21,0, '({}, {})'.format(1.21,0))
plt.legend()

plt.subplot(2,1,2)
plt.grid()
plt.xlabel('Frequency(rad/s)')
plt.ylabel('Phase(degree)')
plt.semilogx(w1, phase1,label='Uncompensated')     # Phase plot for G(s)
plt.semilogx(w2, phase2,label='Compensator')       # Phase plot for Gc(s)
plt.semilogx(w3, phase3,label='Compensated')       # Phase plot for G(s)*Gc(s)
plt.annotate('', (1.21,-117), (1.21,-127), arrowprops=dict(facecolor='red',arrowstyle='<|-|>',mutation_scale=15))
plt.annotate("Lag in Phase",(1.21,-117))
plt.plot(38.95,-184,'o') 
plt.text(38.95,-184, '({}, {})'.format(38.95,-184))
plt.legend()

#if using termux
plt.savefig('./figs/ee18btech11030/ee18btech11030_2.pdf')
plt.savefig('./figs/ee18btech11030/ee18btech11030_2.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11030/ee18btech11030_2.pdf"))
#else
#plt.show()
