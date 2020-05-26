import numpy as np
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex
#end

#Loading the data
data = np.loadtxt( 'ee18btech11044_3_1.dat' )
#PLotting the data from spice simulation
plt.plot(data[:,0],data[:,1])
plt.xlim(0,0.09)
plt.xlabel('time')
plt.ylabel('Vout')
plt.title('Output from Oscillator')

#if using termux
plt.savefig('./figs/ee18btech11044/ee18btech11044_3_4.pdf')
plt.savefig('./figs/ee18btech11044/ee18btech11044_3_4.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11044_3_4.pdf"))
#plt.show()
