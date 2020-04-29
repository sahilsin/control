
import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.patches import ConnectionPatch
import control

#if using termux
import subprocess
import shlex
#end if

f = np.logspace(-3,3,1000)
w = 2*np.pi*f

G = control.TransferFunction([100,600,800],[1,-3,0,0])

mag, phase, omega = control.bode(G,w)


#Magnitutude Plot
plt.subplot(2,1,1)
plt.ylabel('Magnitude(dB)')
plt.semilogx(omega,20*np.log(mag))
plt.plot(5.8,28.1,'o')
plt.text(5.8+0.1,28.1+10, '({}, {})'.format(5.8,28.1))
plt.plot(100,0,'o')
plt.text(100+0.1,0+10, '({}, {})'.format(100,0))
plt.axvline(x=5.8, linestyle='dashed')
plt.axvline(x=100, linestyle='dashed')
plt.axhline(y=0, linestyle='dashed')
plt.axhline(y=26.2, linestyle='dashed')
plt.plot()
plt.grid()

#Phase Plot
plt.subplot(2,1,2)
plt.xlabel('Frequency(rad/sec)')
plt.ylabel('Phase(deg)')
plt.semilogx(omega,phase*57.2958)
plt.plot(5.8,180,'o')
plt.text(5.8+0.1,180+10, '({}, {})'.format(5.8,180))
plt.plot(100,265,'o')
plt.text(100+1,265-25, '({}, {})'.format(100,265))
plt.axvline(x=5.8, linestyle='dashed')
plt.axvline(x=100, linestyle='dashed')
plt.axhline(y=180, linestyle='dashed')
plt.axhline(y=265, linestyle='dashed')
plt.grid()

plt.plot()

#if using termux
plt.savefig('./figs/ee18btech11045/ee18btech11045_bode2.pdf')
plt.savefig('./figs/ee18btech11045/ee18btech11045_bode2.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11045/ee18btech11045_bode2.pdf"))
#else
#plt.show()
