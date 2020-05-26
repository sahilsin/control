import numpy as np
import matplotlib.pyplot as plt
from sympy.abc import s,t
from sympy.integrals import inverse_laplace_transform
import sympy as sy
import math

#if using termux
import subprocess
import shlex
#end if

G, k = sy.symbols('G ,k', real=True)

Ts = (G*((k)**2)*(s**2) + G*(3*k)*s + G)/(((k**2)*(s**2))+ ((3-G)*k*s) + 1)	#transfer function
Ds = 1
Ys = Ts*(Ds)
y = inverse_laplace_transform(Ys,s,t) 	#inverse laplace transform
R = 10000
C = (16)*(10**(-9))
y_t = y.subs({G: 3, k: R*C})
#print("step response is :",y_t)

i = np.linspace(0,0.2,10000)
y =[]
for j in i:
    y.append(3*(12*np.sin(6250.0*j) + 4)*(np.heaviside(j,0.5)/4))

#print(y)
plt.xlim(0,0.02)

plt.plot(i,y)
plt.plot(0.0133468,11.9143,'o')
plt.plot(0.0123387,11.9143,'o')

plt.title("Impulse system response -- R2/R1 = 2 -- f=991.965Hz ")
#if using termux
plt.savefig('./figs/ee18btech11044/ee18btech11044_3_6.pdf')
plt.savefig('./figs/ee18btech11044/ee18btech11044_3_6.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11044_3_6.pdf"))
#plt.show()
