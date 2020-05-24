import numpy as np
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex
#end
def constant_function(x):
    return np.full(x.shape, 0)

 


#Loading the data
data = np.loadtxt( 'ee18btech11019.dat' )
#PLotting the data from spice simulation
plt.plot(data[:,0],data[:,1])
plt.xlim(0.54,0.55)
plt.xlabel('time')
plt.ylabel('Vout')
plt.title('Output from Oscillator')
idx = np.argwhere(np.diff(np.sign(constant_function(data[:,1]) -data[:,1]))).flatten()
T = (data[idx[len(idx)-1],0] - data[idx[len(idx)-2],0])

print("Frequency is: ",1/(2*T))
#if using termux
plt.savefig('./figs/ee18btech11019_6.pdf')
plt.savefig('./figsee18btech11019_6.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11019_6.pdf"))
#plt.show()
