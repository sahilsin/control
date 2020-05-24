import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
#if using termux
import subprocess
import shlex
#end
def constant_function(x):
    return np.full(x.shape, 0)

 
C=1.1*10**-6
L1=R=L2 = 10**-3
print(R,L1,L2)

D = (L1 -C*L1**2)*(C*(L1+L2))
B = (C*L1 - D)/L1
A = C*L1*L2
Con = L1/(L1 + L2)

num = [B,Con]
den = [1,0,1/(C*(L1+L2))]
system = signal.lti(num,den)
num1 = [A,D]
den1 = [L1,C*(L1*L1 + L2*L1)]
system1 = signal.lti(num1,den1)

T, yout = signal.impulse(system)	#oscillating response
T1, yout1 = signal.impulse(system1)

plt.plot(T,yout)
plt.grid()
plt.xlabel("time (t)")
plt.title("Impulse system response ")
plt.savefig('ee18btech11019_5.eps')
# plt.show()
# idx = np.argwhere(np.diff(np.sign(constant_function(yout+yout1) -yout+yout1))).flatten()
# last = 0;
# Tf = (T[idx[len(idx)-2]] - T[idx[len(idx)-3]])*10**-5
# print(T[idx[len(idx)-2]],T[idx[len(idx)-3]])
# print(1/Tf)