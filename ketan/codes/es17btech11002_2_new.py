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
s = signal.lti([25], [1,6,5,0]) 
#Transfer Function C(s)G(s) = 7.58*10(s+.125)(s+0.279)/s(s+1)(s+5)(s+0.00625)(s+5.590) 
s1 = signal.lti([75,30.3,2.615],[1,11.59625,38.612437,28.190875,0.174688,0])
#signal.bode takes transfer function as input and returns frequency,magnitude and phase arrays
w,mag,phase = signal.bode(s)
w1,mag1,phase1 = signal.bode(s1)

sys = tf([25], [1,6,5,0])
sys1= tf([75,30.3,2.615],[1,11.59625,38.612437,28.190875,0.174688,0])
gm, pm, Wpc, Wgc = control.margin(sys)
gm1, pm1, Wpc1, Wgc1 = control.margin(sys1)
print('----------------------------------------------')
#before compensator
print("Phase Margin=",pm) #Phase margin
print("Gain Margin=",gm) #Gain margin
print("Gain crossover frequency(dB)=",Wgc) #Gain crossover freq.(dB)
print("Phase crossover frequency(dB)=",Wpc) #Phase crossover freq.(dB)
print("-----------------------------------------------")
#after compensator
print("Phase Margin (compensator)=",pm1) #Phase margin
print("Gain Margin (compensator)=",gm1) #Gain margin
print("Gain crossover frequency(dB) (compensator)=",Wgc1) #Gain crossover freq.(dB)
print("Phase crossover frequency(dB) (compensator)=",Wpc1) #Phase crossover freq.(dB)


subplot(2,1,1)
plt.xlabel('Frequency(rad/s)')
plt.ylabel('Magnitude(deg)')
plt.semilogx(w, mag,color = 'c')
plt.semilogx(w1, mag1,color='g') # Bode Magnitude plot
plt.axvline(x = 2.11,ymin=0,color='k',linestyle='dashed')
plt.axhline(y = 0,xmin=0,xmax= 2.11,color = 'r',linestyle='dashed')
plt.plot(2.11,0,'o')
plt.text(2.11,0, '({}, {})'.format(2.11,0))
plt.legend()
#plt.grid() 

subplot(2,1,2)
plt.xlabel('Frequency(rad/s)')
plt.ylabel('Phase(deg)')
#plt.title('Phase plot')
plt.axhline(y = -120,xmin=0,color = 'r',linestyle='dashed')
plt.axvline(x = 2.11,ymin=0,color='k',linestyle='dashed')
plt.plot(2.11,-120,'x')
plt.text(2.11,-120, '({}, {})'.format(2.11,-120))

plt.semilogx(w,phase,color= 'c', label='without compensator') # Bode phase plot
plt.semilogx(w1,phase1,color='g', label='with compensator') 
plt.legend()


# if using termux
plt.savefig('./figs/es17btech11002_2.pdf')
plt.savefig('./figs/es17btech11002_2.eps')
subprocess.run(shlex.split("termux-open ./figs/es17btech11002_2.pdf"))
# else
# plt.show()
