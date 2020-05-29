import numpy as np
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex
#end

#Loading the data
data = np.loadtxt( 'ee18btech11030_1.dat' )

#PLotting the data from spice simulation
plt.plot(data[:,0],data[:,1],label = "For K = 0.686")

plt.xlim(0,0.001)
plt.xlabel('time')
plt.ylabel('Vout')
plt.title('Output  for K = 0.686')
plt.grid()

#if using termux
plt.savefig('./figs/ee18btech11030/ee18btech11030_spice_fc4.pdf')
plt.savefig('./figs/ee18btech11030/ee18btech11030_spice_fc4.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11030/ee18btech11030_spice_fc4.pdf"))
#else
#plt.show()
