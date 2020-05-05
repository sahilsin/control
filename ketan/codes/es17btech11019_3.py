import numpy as np
import matplotlib.pyplot as plt
import control
from scipy import signal

#if using termux
import subprocess
import shlex
#end if


t=0.828
k=96
a=3.03

num=[k*t, k]
den=[a*t, (1+12*a*t), (12+44*a*t), (44+48*a*t), 48, 0]
# num=[t,1]
# den=[t*a,1]
sys=control.tf(num,den)
gm, pm, wg, wp = control.margin(sys)
print ("phase margin:",pm)
print ("gain crossover frequency:",wp )
s = signal.lti(num,den)

w, mag, phase =signal.bode(s)
gain_y=np.full((len(w)),0)
phase_y=np.full((len(w)),-180)


plt.subplot(2,1,1)
plt.semilogx(w, mag)
plt.plot(w,gain_y)
plt.plot(wp, 0 ,'ro')
plt.text(wp ,0,'({}, {})'.format(wp, 0))
plt.ylabel("Gain")
plt.xlabel("Frequency")
plt.grid()


plt.subplot(2,1,2)
plt.semilogx(w, phase)
plt.plot(w, phase_y)
plt.plot(wp,-180+pm,'ro')
plt.plot(wp,-180,'ro')
plt.text(wp ,-180+pm,'({}, {})'.format(wp, -180+pm))
plt.text(wp ,-180,'({}, {})'.format(wp, -180))
plt.ylabel("Phase")
plt.xlabel("Frequency")
plt.grid()

##if using termux
plt.savefig('./figs/es17btech11019_2.pdf')
plt.savefig('./figs/es17btech11019_2.eps')
subprocess.run(shlex.split("termux-open ./figs/es17btech11019_2.pdf"))
# else
#
plt.show()