#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 14:05:42 2020

@author: Piyush Kumar Uttam
Released under GNU-GPL
"""

import numpy as np
import matplotlib.pyplot as plt
import control
from scipy import signal

#if using termux
import subprocess
import shlex
#end if

k=96
b=0.69
t=0.82
z=1/t
p=1/(b*t)
# num=[k*t, k]
# den=[b*t, (1+12*b*t), (12+44*b*t), (44+48*b*t), 48, 0]
num=[1,z]
den=[1,p]
sys=control.tf(num,den)
gm, pm, wg, wp = control.margin(sys)
print ("phase margin:",pm)
print ("gain crossover frequency:",wp )
s = signal.lti(num,den)

w, mag, phase =signal.bode(s)
gain_y=np.full((len(w)),0)
phase_y=np.full((len(w)),-180)


plt.subplot(2,1,1)
plt.semilogx(w, mag) 


plt.ylabel("Gain")
plt.xlabel("Frequency")
plt.grid()


plt.subplot(2,1,2)
plt.semilogx(w, phase)

plt.ylabel("Phase")
plt.xlabel("Frequency")
plt.grid()
#if using termux
plt.savefig('./figs/ee18btech11036_4.pdf')
plt.savefig('./figs/ee18btech11036_4.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11036_4.pdf"))
#else
#plt.show()
