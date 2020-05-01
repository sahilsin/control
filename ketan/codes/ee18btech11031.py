# License
'''
Code by Neil
April 25,2020
Released under GNU GPL
'''


from scipy import signal
import matplotlib.pyplot as plt
from pylab import*
import control
from control import tf

#if using termux
import subprocess
import shlex
#end if

#Defining the transfer function 
s1 = signal.lti([50,400,750], [1,12,44,48,0]) #Transfer Function = 75(1+0.2s)/s(s^2+16s+100)

#signal.bode takes transfer function as input and returns frequency,magnitude and phase arrays
w,mag,phase = signal.bode(s1)
sys = tf([50,400,750], [1,12,44,48,0])
gm, pm, Wpc, Wgc = control.margin(sys)

print("Phase Margin=",pm) #Phase margin
print("Gain Margin=",gm) #Gain margin
print("Gain crossover frequency(dB)=",Wgc) #Gain crossover freq.(dB)
print("Phase crossover frequency(dB)=",Wpc) #Phase crossover freq.(dB)

subplot(2,1,1)
#plt.xlabel('Frequency(rad/s)')
plt.ylabel('Magnitude(deg)')
#plt.title('Magnitude plot')
plt.semilogx(w, mag,'b')        # Bode Magnitude plot
plt.axhline(y = 0,xmin=0,xmax= 6.438,color = 'r',linestyle='dashed')
plt.axvline(x = 6.438,ymin=0,color='k',linestyle='dashed')
plt.plot(6.438,0,'o')
plt.text(6.43785,0, '({}, {})'.format(6.438,0))
plt.grid() 

subplot(2,1,2)
plt.xlabel('Frequency(rad/s)')
plt.ylabel('Phase(deg)')
#plt.title('Phase plot')
plt.semilogx(w,phase)          # Bode phase plot
plt.axvline(x = 6.438,ymin=0,color='k',linestyle='dashed')
plt.axhline(y = -180,xmin=0,color = 'r',linestyle='dashed')
plt.plot(6.438,-150.7,'x')
plt.text(6.43785,-150.7, '({}, {})'.format(6.438,-150.7))
plt.grid()

#if using termux
plt.savefig('./figs/ee18btech11031/ee18btech11031_2.pdf')
plt.savefig('./figs/ee18btech11031/ee18btech11031_2.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11031/ee18btech11031_2.pdf"))
#else
#plt.show()

