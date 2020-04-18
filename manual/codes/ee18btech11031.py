import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

A = np.array([
	[0.0,1.0],
	[-2.0,-3.0]
])

B = np.array([
	[0.0],
	[1.0]
])

C = np.array([
	[1.0,0.0]
])

D = 0.0

sys = signal.StateSpace(A,B,C,D)

t1,y1= signal.impulse2(sys)
s = symbols('s')
a = ss2tf(A,B,C,D)[0][0][0]
b =  ss2tf(A,B,C,D)[0][0][1]
c = ss2tf(A,B,C,D)[0][0][2]
d = ss2tf(A,B,C,D)[1][0]
e = ss2tf(A,B,C,D)[1][1]
f = ss2tf(A,B,C,D)[1][2]
H_s = (a*s**2+b*s+c)/(d*s**2+e*s+f)
print("THE TRANSFER FUNCTION OF THE SYSTEM ")
print("H(s) =",H_s)
plt.plot(t1,y1,label='impulse response')
plt.legend()
plt.grid()
plt.show()
