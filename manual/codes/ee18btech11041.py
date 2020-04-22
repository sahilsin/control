import sympy as sy 
import numpy as np

s,R,k2,L,k1,J= sy.symbols("s,R,k2,L,k1,J")



T = sy.Matrix([ [0, 0, -R, 0, 0,-k2],  #transition matrix
[1/L, 0, 0, 0, 0, 0],
[0, 1/s, 0, 0, 0, 0],
[0, 0, k1,0, 0, 0],
[0, 0, 0, 1/J, 0, 0],
[0, 0, 0, 0, 1/s, 0] ]
)
l=T.shape[0]

I=sy.eye(l)

U=sy.Matrix()

U=(I-T)**(-1)  

print("Transfer function:",sy.cancel(sy.simplify(U[l-1,0]))) # U[l-1,0] gives the gain from 0 to l-1 node