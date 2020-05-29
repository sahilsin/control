import numpy as np
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex
#end

#Loading the data
data = np.loadtxt( 'ee18btech11030.dat' )
#PLotting the data from spice simulation
plt.plot(data[:,0],data[:,1])
plt.xlim(0,0.1)
plt.xlabel('time')
plt.ylabel('Vout')
plt.title('Output  for K = 2.1')
plt.grid()

#if using termux
plt.savefig('./figs/ee18btech11030/ee18btech11030_spice_fc3.pdf')
plt.savefig('./figs/ee18btech11030/ee18btech11030_spice_fc3.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11030/ee18btech11030_spice_fc3.pdf"))
#else
#plt.show()
