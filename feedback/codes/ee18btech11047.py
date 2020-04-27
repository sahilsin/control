
# Code by Tejaswini
# output from state space model with non-zero initial conditions

import sympy as sp
import numpy as np
from sympy.abc import s,t
from scipy import signal
from sympy.integrals import inverse_laplace_transform
import matplotlib.pyplot as plt


def Y(A,B,C,D,x_0):  #function to find output Y(s) from state space model with non-zero initial conditions.
    n = len(A)
    I = sp.eye(n)
    p = len(B[0])
    U_s = int(np.ones((p,1)))
    U_s = U_s*1/s
    Y_s = ((((C*((s*I - A)**-1)*B)+(D))*U_s)+(C*((s*I - A)**-1)*x_0))
    return Y_s
    
A = np.array([[0,1],
             [0,-2]])   # state or system matrix A
B = np.array([[0],
              [1]])     # Input matrix B
C = np.array([[1,0]])   # Output matrix C
D = np.array([[0]])     # feedthrough (or feedforward) matrix D
x_0 = np.array([[1],
                [0]])   # Input initial conditions

Y_S = Y(A,B,C,D,x_0)    # output Y(s)

def y(t):			# function to find output y(t) i.e. in time domain
	y = inverse_laplace_transform(Y_S[0],s,t)
	return y
	
print('Y(s) = ',np.array(Y_S))
print("y(t) = ",y(t)) # Heaviside(t) = u(t) i.e. unit step function
print("The value of y(t) at t = 1 sec is ", y(1)) #required answer



