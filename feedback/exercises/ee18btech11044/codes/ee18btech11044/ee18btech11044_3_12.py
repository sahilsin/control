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
y_t = y.subs({G: 2.5, k: R*C})
print("Step Response is :",y_t)

x = np.linspace(0,0.2,10000)

y = -0.32274*1j*(-0.5 + 1.93649*1j)*(3.75*np.exp(1562.5*x) - 0.9682*1j*np.exp(1562.5*x) + 9.6824583*np.sin(6051.536478*x) - 2.5*1j*np.sin(6051.53647*x))*np.exp(-1562.5*x)*np.heaviside(x,0.5)

#print(y)
plt.xlim(0,0.010)
plt.title('Step response -- Magnified plot -- f=953.84Hz ')
plt.plot(x,y.real)


#if using termux
plt.savefig('./figs/ee18btech11044/ee18btech11044_3_15.pdf')
plt.savefig('./figs/ee18btech11044/ee18btech11044_3_15.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11044_3_15.pdf"))
#plt.show()
