import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from matplotlib.pyplot import *

#if using termux
import subprocess
import shlex
#end if

#signal.bode takes transfer function as input and returns frequency,magnitude and phase arrays
Num =[1,0,0] 
Den =[0.004, 0.22, 1]
s1 = signal.lti(Num,Den) 
w, mag, phase = signal.bode(s1)



fig=subplot(2,1,1)
plt.xlabel('Frequency(rad/s)')
plt.ylabel('Magnitude(deg)')
plt.semilogx(w, mag)  
plt.axhline(y = 0,xmin=0,xmax= 4.25226694,linestyle='dashed')
plt.axvline(x = 1.2,ymin=0,linestyle='dashed')
plt.text(4.252,0,'(1.2,0)')
plt.grid()
fig=subplot(2,1,2)
plt.xlabel('Frequency(rad/s)')
plt.ylabel('Phase(deg)')
plt.semilogx(w, phase) 
plt.axhline(y = -180,xmin=0,linestyle='dashed')
plt.grid()
plt.show()


#if using termux
plt.savefig('./figs/es17btech11002/es17btech11002.pdf')
plt.savefig('./figs/es17btech11002/es17btech11002.eps')
subprocess.run(shlex.split("termux-open ./figs/es17btech11002/es17btech11002.pdf"))
#else
#plt.show()
