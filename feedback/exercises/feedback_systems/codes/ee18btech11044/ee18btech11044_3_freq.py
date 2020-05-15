import numpy as np
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex
#end

T = 0.0856452 - 0.0846361
f = 1/T
print(f)


#Loading the data
data = np.loadtxt( 'plot.dat' )
#PLotting the data from spice simulation
plt.plot(data[:,0],data[:,1],label='Oscillator output')
plt.xlim(0.08,0.09)
plt.ylim(-20,20)
plt.xlabel('time')
plt.ylabel('Vout')
plt.title('Output from Oscillator')
plt.plot([0.08,0.09],[0,0],'r--',lw=1,label ='0V')
plt.plot(0.0846361,0,'o')
plt.plot(0.0856452,0,'o')
plt.legend()
#if using termux
plt.savefig('./figs/ee18btech11044/ee18btech11044_3_3.pdf')
plt.savefig('./figs/ee18btech11044/ee18btech11044_3_3.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11044_3_1.pdf"))
#plt.show()
