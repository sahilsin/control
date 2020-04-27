#import numpy as np
import matplotlib.pyplot as plt
import control as cnt

#if using termux
import subprocess
import shlex
#end if

G1 = cnt.tf([1],[1,4,3,0])
cnt.rlocus(G1, xlim = (-4,1), ylim = (-3,3))
plt.xlabel('real part of s')
plt.ylabel('imaginary part of s')
plt.grid()
plt.savefig('ee18btech11050.pdf')
plt.savefig('ee18btech11050.eps')

#if using termux
plt.savefig('./figs/ee18btech11050.pdf')
plt.savefig('./figs/ee18btech11050.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11050.pdf"))
#else
#plt.show()
