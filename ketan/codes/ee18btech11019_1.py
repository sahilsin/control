
###################################################################

# This is python code for plots.    
# By Harsh kabra
# 12 may , 2020 
# Released under GNU GPL

###################################################################

from scipy import signal
import matplotlib.pyplot as plt
from pylab import*
import numpy as np

#if using termux
import subprocess
import shlex
#end if

def constant_function(x):
    return np.full(x.shape, 0)

 

s1 = signal.lti([13.2,100,132],
[5/6,10/9,6,4/3])
s2 = signal.lti([132],[5/6,10/9,6,4/3])
w,mag,phase = signal.bode(s1) 
w2,mag2,phase2 = signal.bode(s2)

subplot(2,1,1)
plt.grid()
plt.xlabel('Frequency(rad/s)')
plt.ylabel('Magnitude(db)')

plt.semilogx(w, mag,'b',label = 'With Controller')     
plt.semilogx(w, constant_function(mag),'b') 


idx = np.argwhere(np.diff(np.sign(constant_function(mag) - mag))).flatten()
plt.plot(w[idx],mag[idx],'o')
plt.text(w[idx],mag[idx],f'({round(float(w[idx]),1)},{round(float(mag[idx]),1)})')

plt.semilogx(w2, mag2,'b',color='orange',label = 'Without Controller')     
plt.semilogx(w2, constant_function(mag2),'b') 

idx2 = np.argwhere(np.diff(np.sign(constant_function(mag2) - mag2))).flatten()
plt.plot(w2[idx2],mag2[idx2],'o')
plt.text(w2[idx2],mag2[idx2],f'({round(float(w2[idx2]),1)},{round(float(mag2[idx2]),1)})',horizontalalignment='right')

plt.legend()

subplot(2,1,2)
plt.xlabel('Frequency(rad/s)')
plt.ylabel('Phase(deg)')

plt.semilogx(w,phase,label = 'With Controller') 
plt.plot(w[idx],phase[idx],'o')
plt.text(w[idx],phase[idx],f'({round(float(w[idx]),1)},{round(float(phase[idx]),1)})')

plt.semilogx(w2,phase2,color = 'orange',label = 'Without Controller') 
plt.plot(w2[idx2],phase2[idx2],'o')
plt.text(w2[idx2],phase2[idx2],f'({round(float(w2[idx2]),1)},{round(float(phase2[idx2]),1)})')
plt.grid() 
plt.legend()


#if using termux
plt.savefig('./figs/ee18btech11019_6.pdf')
plt.savefig('./figs/ee18btech11019_6.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11019_6.pdf"))
#else
#plt.show()