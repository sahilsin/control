import matplotlib.pyplot as plt
import numpy as np
import control

#if using termux
import subprocess
import shlex
#end if
#values of omega (w)
OMEGA = np.linspace(-20, 20, 2001)


#defining transfer function
s = control.TransferFunction.s
G = 1/((s+1)*(2*s+1))
#Using library getting mag and phase of the transfer function for resp. omegas
MAG, PHASE, W = G.freqresp(OMEGA)
#plotting the polar plot
axes = plt.subplot(111, projection='polar')
axes.plot(PHASE.reshape((2001,))[-1000:],MAG.reshape((2001,))[-1000:])
plt.title("polar plot")
plt.polar(-3.14,1,marker='o',color='blue')
plt.polar(-3.14,0.5,marker='o',color='blue')
print(MAG)
print(PHASE)
#if using termux
plt.savefig('./figs/ee18btech11012.pdf')
plt.savefig('./figs/ee18btech11012.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11012.pdf"))
#else
#plt.show()


