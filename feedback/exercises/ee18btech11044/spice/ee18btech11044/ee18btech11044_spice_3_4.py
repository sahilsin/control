import numpy as np
import matplotlib.pyplot as plt


T = 0.00227823 - 0.00127016
f = 1/T
print(f)

#if using termux
import subprocess
import shlex
#end

#Loading the data
data = np.loadtxt( 'ee18btech11044_3_2.dat' )
#PLotting the data from spice simulation
plt.plot(data[:,0],data[:,1],label='Oscillator output -- R2/R1 = 2')
plt.xlim(0.00,0.01)
plt.ylim(-0.02,0.02)
plt.xlabel('time')
plt.ylabel('Vout')
plt.title('Output from Oscillator')
plt.plot([0.00,0.01],[0.014329,0.014329],'r--',lw=1,label ='0.014329V')
plt.plot(0.00127016,0.014329,'o')
plt.plot(0.00227823,0.014329,'o')
plt.legend()
#if using termux
plt.savefig('./figs/ee18btech11044/ee18btech11044_3_9.pdf')
plt.savefig('./figs/ee18btech11044/ee18btech11044_3_9.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11044_3_9.pdf"))
#plt.show()
