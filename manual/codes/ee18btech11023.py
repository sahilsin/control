#Coded by SRIKANTH
#15th April, 2020
#Released under GNU GPL

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import ss2tf

A = [[-4, -1.5], [4, 0]]
B = [[4], [0]]  # 2-dimensional column vector
C = [[1.5, 0.625]]    # 2-dimensional row vector
D = [[0]]
ss2tf(A, B, C, D)
sys = ss2tf(A,B,C,D)
print(sys)
