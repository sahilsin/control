import numpy as np
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex
#end

data = np.loadtxt( 'ee18btech11038_rout.data' )
#PLotting the data from spice simulation
Vx = data[:, 0]
Ix = data[:, 1]*pow(10,6)
i=10
plt.plot(Ix, Vx)
plt.ylabel('Vx (volts)')
plt.xlabel('Ix (uA)')
plt.title('Vx vs Ix(slope = Ro)')
plt.plot(Ix[i], Vx[i],'o')
plt.text(Ix[i]+0.5, Vx[i], '({},{})'.format(Ix[i].round(3), Vx[i]))
plt.xlim([0, 16])
plt.ylim([0, 5])
print('Ro = Slope = ', Vx[10]/Ix[10]*pow(10,6), 'ohms')
plt.savefig('./ee18btech11038_rout.pdf')
plt.savefig('./ee18btech11038_rout.eps')
#if using termux
plt.savefig('./figs/ee18btech11038/ee18btech11038_rout.pdf')
plt.savefig('./figs/ee18btech11038/ee18btech11038_rout.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11038_rout.pdf"))

# plt.show()

