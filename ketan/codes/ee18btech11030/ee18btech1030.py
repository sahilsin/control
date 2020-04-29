

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

 
s1 = signal.lti([16200,21*16200,110*16200], [11, 18*11 ,99*11,162*11,0]) #Defining the transfer function 

w,mag,phase = signal.bode(s1) #signal.bode takes transfer function as input and returns frequency,magnitude and phase arrays

subplot(2,1,1)
plt.grid()
plt.xlabel('Frequency(rad/s)')
plt.ylabel('Magnitude(db)')

plt.semilogx(w, mag,'b')                              # Bode Magnitude plot
plt.axhline(y = 0,xmin=0,color = 'r',linestyle='dashed')
plt.axvline(x = 38.95,ymin=0,color='k',linestyle='dashed')
plt.plot(38.95,0,'o')
plt.text(38.95,0, '({}, {})'.format(38.95,0))

subplot(2,1,2)
plt.xlabel('Frequency(rad/s)')
plt.ylabel('Phase(deg)')

plt.semilogx(w,phase)                                  # Bode phase plot
plt.axhline(y = -184,xmin=0,color = 'r',linestyle='dashed')
plt.axvline(x = 38.95,ymin=0,color='k',linestyle='dashed')
plt.plot(1.21,-116.83,'o')
plt.text(1.21,-116.83, '({}, {})'.format(1.21,-116.83))
plt.plot(38.95,-184,'o') 
plt.text(38.95,-184, '({}, {})'.format(38.95,-184))
plt.grid() 
#if using termux
plt.savefig('./figs/ee18btech11030/ee18btech11030_1.pdf')
plt.savefig('./figs/ee18btech11030/ee18btech11030_1.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11030/ee18btech11030_1.pdf"))
#else
#plt.show()
