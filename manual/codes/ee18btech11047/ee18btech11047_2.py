
# Code by Tejaswini
# Unit step response 


import numpy as np
import sympy as sp
from sympy.abc import s,t
from sympy.integrals import inverse_laplace_transform
from scipy import signal
import matplotlib.pyplot as plt


A = np.array([[0,1],
             [0,-2]])   # state or system matrix A
B = np.array([[0],
              [1]])     # Input matrix B
C = np.array([[1,0]])   # Output matrix C
D = np.array([[0]])     # feedthrough (or feedforward) matrix D
x_0 = np.array([[1],
                [0]])   # Input initial conditions


Hs = (s**3 + 2*(s**2) + s)/(s**3 + 2*(s**2)) 

Us = 1/s

Ys = Hs * Us

#print(Ys)
def y(t):     #unit step response
	y = inverse_laplace_transform(Ys,s,t)
	return y

t1=np.linspace(0.1,3,10)
y2=0
Y1=np.array([])
for T in t1:
	y2=y(T)
	Y1= np.append(Y1,[y2])

print("Unit step response (y(t)) =",y(t)) # Note: "Heaviside(t)" is nothing but u(t):unit step
print("y(t) at t = 1 sec is :",float(y(1)))      #required answer
plt.plot(t1,Y1,label='Unit step response')
plt.xlabel('$t$')
plt.ylabel('$y(t)$')
plt.legend()
plt.grid()
plt.show()
