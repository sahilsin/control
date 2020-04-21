import sympy as sp
import numpy as np
from scipy import signal


A = np.array([
	[1,2],
	[2,0]
])

B = np.array([
	[1],
	[2]
])

C = np.array([
	[1,0]
])

D = 0

sys = signal.StateSpace(A,B,C,D) #State space to time domain conversion
a,b = signal.ss2tf(A,B,C,D) #Importing Num. and Den. of T.F. from State Space Rep.
#rounding off

num = np.around(a[0],decimals = 0)

den = np.around(b,decimals = 0)

s = sp.symbols('s')

H_s = sp.Poly(num,s)/sp.Poly(den,s) # Getting polynomial expressions

print("THE TRANSFER FUNCTION OF THE SYSTEM ")

print("H(s) =",H_s)
