import numpy as np
import matplotlib.pyplot as plt
from sympy.abc import s,t
from sympy.integrals import inverse_laplace_transform
import sympy as sy
import math
import cmath

#if using termux
import subprocess
import shlex
#end if

G, k = sy.symbols('G ,k', real=True)

Ts = (G*((k)**2)*(s**2) + G*(3*k)*s + G)/(((k**2)*(s**2))+ ((3-G)*k*s) + 1)	#transfer function
Us = 1/s
Ys = Ts*(Us)
y = inverse_laplace_transform(Ys,s,t) 	#inverse laplace transform
R = 10000
C = (16)*(10**(-9))
y_t = y.subs({G: 3.03, k: R*C})
#print("Step Response is :",y_t)

x = np.linspace(0,0.2,10000)

y = -0.37879*1j*(0.0298 + 1.99974*1j)*(12.11863*np.sin(6249.2968*x) + 0.18179*1j*np.sin(6249.2968*x) + 3.9991*np.exp(-93.74994*x) + 0.059993*1j*np.exp(-93.7494*x))*np.exp(93.7494*x)*np.heaviside(x,0.5)

#print(y)
plt.xlim(0.180,0.2)
plt.title('Step response -- Magnified plot -- f = 953.28Hz')
plt.plot(x,y.real)

#if using termux
plt.savefig('./figs/ee18btech11044/ee18btech11044_3_3.pdf')
plt.savefig('./figs/ee18btech11044/ee18btech11044_3_3.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11044_3_3.pdf"))
#plt.show()
