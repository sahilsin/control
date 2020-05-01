from scipy import signal
import matplotlib.pyplot as plt
from pylab import*

# If using termux
import subprocess
import shlex
#end if

#Transfer Function before compensator
s1= signal.lti([218.6], [1,16,55,0]) 
#Transfer Function after compensator
s2 = signal.lti([4430, 70.7471],[1, 64.921, 593.185, 0.59312, 0])

#signal.bode takes transfer function as input and returns frequency, magnitude and phase arrays
w1, mag1, phase1 = signal.bode(s1)
w2, mag2, phase2 = signal.bode(s2)

subplot(2,1,1)
plt.xlabel('Frequency(rad/s)')
plt.ylabel('Magnitude(deg)')
plt.semilogx(w1, mag1, color= 'c')
plt.semilogx(w2, mag2, color='g') # Bode Magnitude plot
plt.grid()

subplot(2,1,2)
plt.xlabel('Frequency(rad/s)')
plt.ylabel('Phase(deg)')
plt.semilogx(w1,phase1, color='c', label='without compensator') # Bode phase plot
plt.semilogx(w2,phase2, color='g', label='with compensator') 
plt.legend()
plt.grid()

# If using termux
plt.savefig('./figs/ep18btech11016/ep18btech11016_fig3.pdf')
plt.savefig('./figs/ep18btech11016/ep18btech11016_fig3.eps')
subprocess.run(shlex.split("termux-open ./figs/ep18btech11016/ep18btech11016_fig3.pdf"))
# else
#plt.show()
