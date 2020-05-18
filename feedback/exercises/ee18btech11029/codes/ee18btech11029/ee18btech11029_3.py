#coded by M.Sai Mehar
#Date 16th May 2020
#Released under GNU GPL

from scipy import signal
import matplotlib.pyplot as plt
from pylab import*
import control
from control import tf


#if using termux
import subprocess
import shlex
#end if

#These are the values of poles after compensation
p1 = (2*np.pi*200)
p2 = (2*np.pi*37.95*1e6)
p3 = (2*np.pi*2*1e6)


a=p1+p2+p3
b=p1*p2*p3
c=p1*p2 + p2*p3 + p3*p1


# Numerator and Denominator of Transfer Function
num = [1e4*p1*p2*p3]
den = [1,a,c,b]


s1 = signal.lti(num, den) 
#signal.bode takes transfer function as input and returns frequency,magnitude and phase arrays
w,mag,phase = signal.bode(s1)
#signal.bode takes transfer function as input and returns frequency,magnitude and phase arrays
sys = tf(num, den)
gm, pm, Wpc, Wgc = control.margin(sys)
print('------------------------------------------------')
print("Phase Margin=",pm) #Phase margin
print("Gain Margin=",gm) #Gain margin
print("Gain crossover frequency(dB)=",Wgc) #Gain crossover freq.(dB)
print("Phase crossover frequency(dB)=",Wpc) #Phase crossover freq.(dB)

print("-----------------------------------------------")
subplot(2,1,1)
plt.xlabel('Frequency')
plt.ylabel('Magnitude')
plt.semilogx(w, mag, color='r')
plt.axhline(y = 0,xmin=0,xmax= 6.438,color = 'r',linestyle='dashed')
plt.axvline(x = 1e7,ymin=0,color='k',linestyle='dashed')
plt.title("Compensated system")
plt.grid() 

subplot(2,1,2)
plt.xlabel('Frequency')
plt.ylabel('Phase')
plt.semilogx(w,phase)
plt.axhline(y = -180,xmin=0,xmax= 6.438,color = 'r',linestyle='dashed')
plt.axvline(x = 6e7,ymin=-180,color='k',linestyle='dashed')
plt.grid()

if(pm>0):
	print("Stable system")
elif (pm==0):
	print("Marginally stable system")
else:
	print("Unstable system")
	

# if using termux
plt.savefig('./figs/ee18btech11029/ee18btech11029_3.pdf')
plt.savefig('./figs/ee18btech11029/ee18btech11029_3.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11029/ee18btech11029_3.pdf"))
# else
#plt.show()
