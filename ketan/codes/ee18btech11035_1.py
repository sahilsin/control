#Code by  P.Aashrith
#April 28, 2020
#Released under GNU GPL
import numpy as np
import matplotlib.pyplot as plt
#if using termux
import subprocess
import shlex
#end if

x=np.linspace(-1.4,1.4,10000)
y=(x**6)+5*(x**4)+4*(x**2)-16

plt.plot(x,y,label='$\omega^{6}+5\omega^{4}+4\omega^{2}-16=0$')
plt.xlabel('$\omega$')
plt.ylabel('$\omega^{6}+5\omega^{4}+4\omega^{2}-16=0$')
plt.grid()	
plt.annotate("A(-1.1432,0)",(-1.1432,0))
plt.annotate("B(1.1432,0)",(1.1432,0))
plt.legend()
#if using termux
plt.savefig('./figs/ee18btech11035.pdf')
plt.savefig('./figs/ee18btech11035.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11035.pdf"))
#else
#plt.show()
