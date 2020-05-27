import numpy as np
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex
#end

#Loading the data
data = np.loadtxt( 'ee18btech11044_3_4.dat' )
#PLotting the data from spice simulation
plt.plot(data[:,0],data[:,1])
#plt.xlim(0,0.05)
plt.xlabel('time')
plt.ylabel('Vout')
plt.title('Output from Oscillator -- R2/R1 = 1.5')

#if using termux
plt.savefig('./figs/ee18btech11044/ee18btech11044_3_16.pdf')
plt.savefig('./figs/ee18btech11044/ee18btech11044_3_16.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11044_3_16.pdf"))
#plt.show()
