#Code by Tejaswini
#Date 28 April,2020
#Released under GNU GPL

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex
#end if


gain = 15				# higher order transfer function
num = [1,5]
char_eq = [1,16,115,75]
zeros=np.roots(num)
poles=np.roots(char_eq)


gain_2 = abs(poles[2])	# second order approximated transfer function
num_2 = [1]
zeros_2=np.roots(num_2)
poles_2=np.array(poles[2])

system = signal.lti(zeros,poles,np.array([gain]))
system_2 = signal.lti(zeros_2,poles_2,np.array([gain_2]))

T, yout = signal.step(system)			# step response without approximation
T_2, yout_2 = signal.step(system_2)		# step response with approximation

plt.plot(T,yout,label="Without approximation")
plt.plot(T_2,yout_2,'g',label="With approximation")
plt.grid()
plt.title("Step response")
plt.xlabel("Time")
plt.ylabel("y(t)")
plt.legend()
#if using termux
plt.savefig('./figs/ee18btech11047/ee18btech11047_4.pdf')
plt.savefig('./figs/ee18btech11047/ee18btech11047_4.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11047/ee18btech11047_4.pdf"))
#else
#plt.show()
