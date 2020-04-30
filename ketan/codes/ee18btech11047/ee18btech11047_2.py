#Code by Tejaswini
#Date 28 April,2020
#Released under GNU GPL

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import matplotlib.pyplot as plt


#if using termux
import subprocess
import shlex
#end if

gain = [50]
poles=[0,-2,-4,-6]
zeros=[-3,-5]
system = signal.lti(zeros,poles,gain)
w , mag, phase = signal.bode(system)

plt.subplot(2,1,1)
plt.xlabel('Frequency(rad/sec)')	# Bode Magnitude plot
plt.ylabel('Mag')
plt.title('Magnitude plot')
plt.semilogx(w, mag,'b')        
plt.axhline(y = 0,xmin=0,xmax= 0.68,color = 'r',linestyle='dashed')
plt.axvline(x = 6.43,ymax=0.4,color='k',linestyle='dashed')
plt.plot(6.43,0,'o')
plt.text(6.45,2, '({}, {})'.format(6.43,0))
plt.axhline(y = -7,xmin=0,xmax= 0.72,color = 'r',linestyle='dashed')
plt.axvline(x = 10.1,ymax=0.38,color='k',linestyle='dashed')
plt.plot(10.1,-7,'o')
plt.text(10.4,-7.4, '({}, {})'.format(10.1,-7))
plt.grid()

plt.subplots_adjust(hspace=0.5)

plt.subplot(2,1,2)
plt.xlabel('Frequency(rad/s)')		# Bode phase plot
plt.ylabel('Phase(deg)')
plt.title('Phase plot')
plt.semilogx(w,phase)          
plt.axhline(y = -150.7,xmin=0,xmax= 0.68,color = 'r',linestyle='dashed')
plt.axvline(x = 6.43,ymax=0.35,color='k',linestyle='dashed')
plt.plot(6.43,-150.7,'o')
plt.text(6.45,-152, '({}, {})'.format(6.43,-150.7))
plt.grid()

#if using termux
plt.savefig('./figs/ee18btech11047/ee18btech11047_2.pdf')
plt.savefig('./figs/ee18btech11047/ee18btech11047_2.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11047/ee18btech11047_2.pdf"))
#else
#plt.show()
