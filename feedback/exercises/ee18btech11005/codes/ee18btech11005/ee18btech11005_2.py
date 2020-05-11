#Code by B.Varuni
#Date 3 May,2020
#Released Under GNU GPL
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import matplotlib.pyplot as plt
import cmath

#if using termux
import subprocess
import shlex
#end if

gain = [7.816*10**12]
poles=[1,125*10**4,7.816*10**11]
zeros=[]
system = signal.lti(zeros,poles,gain)
w , mag, phase = signal.bode(system)

plt.figure(1)
plt.xlabel('Frequency(rad/sec)')	# Bode Magnitude plot
plt.ylabel('Mag')
plt.title('Magnitude plot')
plt.semilogx(w, mag,'b')        
plt.grid()

#if using termux
#plt.savefig('./figs/ee18btech11005/ee18btech11005_1.pdf')
#plt.savefig('./figs/ee18btech11005/ee18btech11005_1.eps')
subprocess.run(shlex.split("termux-open./figs/ee18btech11005/ee18btech11005_1.pdf"))
#else
plt.show()
