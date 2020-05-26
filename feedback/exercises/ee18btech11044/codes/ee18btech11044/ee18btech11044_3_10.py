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
Ds = 1
Ys = Ts*(Ds)
y = inverse_laplace_transform(Ys,s,t) 	#inverse laplace transform
R = 10000
C = (16)*(10**(-9))
y_t = y.subs({G: 3.03, k: R*C})
print("Impulse Response  is :",y_t)



