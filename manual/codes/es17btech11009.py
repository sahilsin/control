import control
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex
#end if

num = [0,0,1,3]
den = [1,-3,0,0]

#Transfer function GH = num/den
G = control.tf(num,den) 
control.nyquist(G)
plt.grid(True)
plt.scatter(-1,0,s=40)
plt.annotate("-1+0j",(-1,0))
plt.title('Nyquist Diagram of G(s)H(s)')
plt.xlabel('Re(s)')
plt.ylabel('Im(s)')
plt.show()

#if using termux
plt.savefig('./figs/es17btech11009.pdf')
plt.savefig('./figs/es17btech11009.eps')
subprocess.run(shlex.split("termux-open ./figs/es17btech11009.pdf"))
#else
#plt.show()
