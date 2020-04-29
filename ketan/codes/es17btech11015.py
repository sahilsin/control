import control
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex
#end if


num = [0,0,0,0,1]
den = [1,16,86,176,105]

G = control.tf(num,den) 

#plotting nyquist plot
control.nyquist(G)

plt.scatter(-1,0,s=60,color='r')
plt.annotate("-1",(-1,0))
plt.title('NYQUIST DIAGRAM of L(s)')
plt.xlabel("${Re}\{G(j\omega)H(j\omega)\}$")
plt.ylabel("${Im}\{G(j\omega)H(j\omega)\}$")
plt.grid(color='k',linestyle='--',linewidth=1)
plt.show()


#if using termux
plt.savefig('./figs/es17btech11015.pdf')
plt.savefig('./figs/es17btech11015.eps')
subprocess.run(shlex.split("termux-open ./figs/es17btech11015.pdf"))
#else
#plt.show()