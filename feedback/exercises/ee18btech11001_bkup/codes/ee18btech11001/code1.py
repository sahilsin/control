#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 12:45:15 2020

@author: aayush
"""
import numpy as np
from scipy import signal

#Closed Loop Transfer Function
A = 1e5
zeros = []
poles = [-100,-1e4,-1e4]
Den = np.poly(poles)
Den = Den/Den[-1]
Num = np.poly(zeros)
if len(zeros)==0:
    Num = np.array([Num])
Num = Num/Num[-1]
w = np.linspace(2,5,2000)
w = 10**w
s1 = signal.lti(A*Num, Den) 
w, mag, phase = signal.bode(s1,w)

#Calculating the frequency at which total face shift is 180
for i in range(len(w)):
    if abs(phase[i]+180) < 1e-1:
        w_180 = w[i]
        Gain = 10**(mag[i]/20)

#Calculating feedbackfactor for unity gain at w_180
beta = 1/Gain
Num1 = np.append(np.zeros(len(Den)-len(Num)) , Num)*A

Den2 = beta*Num1 + Den

#Closed Loop transfer function and its gain at low frequencies
H = signal.lti(Num*A , Den2)
w1 = np.array([1])
w1,mag1,phase1 = signal.bode(H,w1)
Af = 10**(mag1/20)[0]

print("Frequency for 180 degree phase shift :", w_180)
print("Loop Gain is unity for feedback factor :" , beta)
print("Closed loop gain at low frequencies : " ,Af)
