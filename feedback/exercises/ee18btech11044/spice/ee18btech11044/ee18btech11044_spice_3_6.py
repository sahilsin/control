import numpy as np
import matplotlib.pyplot as plt


T = 0.00453629 - 0.00270161
f = 1/T
print(f)

#if using termux
import subprocess
import shlex
#end

#Loading the data
data = np.loadtxt( 'ee18btech11044_3_3.dat' )
#PLotting the data from spice simulation
plt.plot(data[:,0],data[:,1],label='Oscillator output -- R2/R1 = 9')
plt.xlim(0.00,0.01)
plt.ylim(-20,20)
plt.xlabel('time')
plt.ylabel('Vout')
plt.title('Output from Oscillator')
plt.plot([0.00,0.01],[0,0],'r--',lw=1,label ='0V')
plt.plot(0.00270161,0,'o')
plt.plot(0.00453629,0,'o')
plt.legend()
#if using termux
#plt.savefig('./figs/ee18btech11044/ee18btech11044_3_13.pdf')
#plt.savefig('./figs/ee18btech11044/ee18btech11044_3_13.eps')
#subprocess.run(shlex.split("termux-open ./figs/ee18btech11044_3_13.pdf"))
plt.show()
