#Code by Tejaswini
#Date 15 May,2020

import numpy as np
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex
#end

T = 120.344 - 118.734
f = 1/T
print("Frequency is:",f)
print("Amplitude is:",8.89)


#Loading the data
data = np.loadtxt( 'ee18btech11047.dat' )
#PLotting the data from spice simulation
plt.plot(data[:,0],data[:,1])
plt.xlim(117,140)
plt.ylim(-12,12)
plt.plot([117,140],[0,0],'r--',lw=1,label ='0V')
plt.plot(120.344,0,'o')
plt.plot(118.734,0,'o')
plt.legend()
plt.xlabel('time')
plt.ylabel('Vout')
plt.title('Output from spice simulation')

#if using termux
plt.savefig('./figs/ee18btech11047/ee18btech11047_spice2.pdf')
plt.savefig('./figs/ee18btech11047/ee18btech11047_spice2.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11047/ee18btech11047_spice2.pdf"))
#else
#plt.show()
