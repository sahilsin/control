
import numpy as np
from matplotlib import pyplot as plt 
import control
from matplotlib.pyplot import style

#if using termux
import subprocess
import shlex
#end if

# style.use('seaborn')

G = control.TransferFunction((25.05, 100.2), (1, 8, 16.05, 28.2))

rlist, klist = control.rlocus(G)


plt.annotate("Pole, P1", (-6.13, -2))
plt.annotate("Pole, P2", (-1, 3))
plt.annotate("Pole, P3", (-1, -3))
plt.annotate("Zero, Z1", (-4, 1))
plt.legend()

#if using termux
plt.savefig('./figs/ee18btech11052.pdf')
plt.savefig('./figs/ee18btech11052.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11052.pdf"))
#else
#plt.show()
