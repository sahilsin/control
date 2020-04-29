from scipy import signal
import matplotlib.pyplot as plt
from pylab import*
import control
from control import tf


#if using termux
import subprocess
import shlex
#end if


#Transfer Function = 25/s(s+1)(s+5) before compensator
s1 = signal.lti([25], [1,6,5,0]) 
#signal.bode takes transfer function as input and returns frequency,magnitude and phase arrays
w,mag,phase = signal.bode(s1)
#signal.bode takes transfer function as input and returns frequency,magnitude and phase arrays
sys = tf([25], [1,6,5,0])
gm, pm, Wpc, Wgc = control.margin(sys)
print('------------------------------------------------')
print("Phase Margin=",pm) #Phase margin
print("Gain Margin=",gm) #Gain margin
print("Gain crossover frequency(dB)=",Wgc) #Gain crossover freq.(dB)
print("Phase crossover frequency(dB)=",Wpc) #Phase crossover freq.(dB)
print("-----------------------------------------------")
subplot(2,1,1)
plt.xlabel('Frequency(rad/s)')
plt.ylabel('Magnitude(deg)')
plt.semilogx(w, mag, color='r')
plt.axhline(y = 0,xmin=0,xmax= 6.438,color = 'r',linestyle='dashed')
plt.axvline(x = 2.03,ymin=0,color='k',linestyle='dashed')
plt.plot(2.03,0,'o')
plt.text(2.03,0, '({}, {})'.format(2.03,0))
plt.grid() 

subplot(2,1,2)
plt.xlabel('Frequency(rad/s)')
plt.ylabel('Phase(deg)')
plt.semilogx(w,phase)
plt.grid()


# if using termux
plt.savefig('./figs/es17btech11002_1.pdf')
plt.savefig('./figs/es17btech11002_1.eps')
subprocess.run(shlex.split("termux-open ./figs/es17btech11002_1.pdf"))
# else
#plt.show()
