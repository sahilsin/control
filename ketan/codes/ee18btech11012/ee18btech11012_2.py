from scipy import signal
import matplotlib.pyplot as plt
from pylab import*


#if using termux
import subprocess
import shlex
#end if

#Defining the transfer function 
s1 = signal.lti([75000,75000*7], [7, 20*7 ,75*7,0])  #G(s)
s2 = signal.lti([1,36.983,226.62], [1,206.802,226.68])  #Gc(s)
s3 = signal.lti([75000,75000*43.983,75000*485.501,75000*1586.34],[7,7*226.802,7*4211.04,7*20043.75,7*17001,0])  #G(s)*Gc(s)

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

plt.legend()

plt.subplot(2,1,2)
plt.grid()
plt.xlabel('Frequency(rad/s)')
plt.ylabel('Phase(degree)')
plt.semilogx(w1, phase1,label='Uncompensated')     # Phase plot for G(s)
plt.semilogx(w2, phase2,label='Compensator')       # Phase plot for Gc(s)
plt.semilogx(w3, phase3,label='Compensated')       # Phase plot for G(s)*Gc(s)


plt.legend()

#if using termux
plt.savefig('./figs/ee18btech11012/ee18btech11012_2.pdf')
plt.savefig('./figs/ee18btech11012/ee18btech11012_2.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11012/ee18btech11012_2.pdf"))
#else

plt.show()
