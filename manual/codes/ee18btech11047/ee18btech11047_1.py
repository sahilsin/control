
# Code by Tejaswini
# Transfer function from state space model with non-zero initial conditions

import sympy as sp
import numpy as np
from sympy.abc import s,t
from scipy import signal
import matplotlib.pyplot as plt


def H(A,B,C,D,x_0):  #function to find transfer H(s) from state space model with non-zero initial conditions.
    n = len(A)
    I = sp.eye(n)
    p = len(B[0])
    U_s = int(np.ones((p,1)))
    U_s = U_s*1/s
    H_s = s*((((C*((s*I - A)**-1)*B)+(D))*U_s)+(C*((s*I - A)**-1)*x_0))
    return H_s
    
A = np.array([[0,1],
             [0,-2]])   # state or system matrix A
B = np.array([[0],
              [1]])     # Input matrix B
C = np.array([[1,0]])   # Output matrix C
D = np.array([[0]])     # feedthrough (or feedforward) matrix D
x_0 = np.array([[1],
                [0]])   # Input initial conditions

H_S = H(A,B,C,D,x_0)    # transfer function H(s)

print('H(s) = ',np.array(H_S))

