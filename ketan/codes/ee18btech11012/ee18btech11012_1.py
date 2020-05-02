from scipy import signal
import matplotlib.pyplot as plt
from pylab import*

#if using termux
import subprocess
import shlex
#end if

 
s1 = signal.lti([75000,75000*7], [7, 20*7 ,75*7,0]) #Defining the transfer function 

w,mag,phase = signal.bode(s1) #signal.bode takes transfer function as input and returns frequency,magnitude and phase arrays

subplot(2,1,1)
plt.grid()
plt.xlabel('Frequency(rad/s)')
plt.ylabel('Magnitude(db)')
plt.semilogx(w,mag,label='Uncompensated')                              # Bode Magnitude plot
plt.axhline(y = 0,xmin=0,color = 'r',linestyle='dashed')
plt.legend()


subplot(2,1,2)
plt.xlabel('Frequency(rad/s)')
plt.ylabel('Phase(deg)')
plt.semilogx(w,phase,label = 'Uncompensated')                                  # Bode phase plot

plt.legend()
plt.grid()

#if using termux
plt.savefig('./figs/ee18btech11012/ee18btech11012.pdf')
plt.savefig('./figs/ee18btech11012/ee18btech11012.eps')
sssubprocess.run(shlex.split("termux-open ./figs/ee18btech11012/ee18btech11012.pdf"))
#else

plt.show()
