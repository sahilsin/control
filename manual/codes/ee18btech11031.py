import sympy as sp
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex
#end if

A = np.array([
	[0,1],
	[-2,-3]
])

B = np.array([
	[0],
	[1]
])

C = np.array([
	[1,0]
])

D = 0
sys = signal.StateSpace(A,B,C,D) #State space to time domain conversion

t1,y1= signal.impulse2(sys) # time and output axis for natural(impulse) response

a,b = signal.ss2tf(A,B,C,D) #Importing Num. and Den. of T.F. from State Space Rep.

#rounding off
num = np.around(a[0],decimals = 0)
den = np.around(b,decimals = 0)
s = sp.symbols('s')
H_s = sp.Poly(num,s)/sp.Poly(den,s) # Getting polynomial expressions

print("THE TRANSFER FUNCTION OF THE SYSTEM ")
print("H(s) =",H_s)
plt.plot(t1,y1,label='impulse response')
plt.legend()
plt.grid()

#if using termux
plt.savefig('./figs/ee18btech11031.pdf')
plt.savefig('./figs/ee18btech11031.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11031.pdf"))
#else
#plt.show()











