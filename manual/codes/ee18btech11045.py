import numpy as np 
from numpy import poly1d
import control as ct 
import matplotlib.pyplot as plt 

#if using termux
import subprocess
import shlex
#end if

Gden = poly1d([1,10,100])

Gden = Gden.c
G = ct.tf([100],Gden)

t_end = 2
t = np.linspace(0,t_end,500)

x,y = ct.step_response(G,t)

overshoot = round(max(y),2)
final_value = round(y[len(t)-1],2)

plt.hlines(overshoot, xmin = 0, xmax = t_end, color = 'red')
plt.text(0,overshoot+0.02, overshoot, ha='left', va='center')

plt.hlines(final_value, xmin = 0, xmax = t_end, color = 'red')
plt.text(0,final_value+0.02, final_value, ha='left', va='center')

plt.plot(x,y)
plt.xlabel("$t$")
plt.ylabel("$c(t)$")
plt.grid()

#if using termux
plt.savefig('./figs/ee18btech11045.pdf')
plt.savefig('./figs/ee18btech11045.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11045.pdf"))
#else
#plt.show()


