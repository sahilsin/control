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
num=[k]
den=[1, 12, 44, 48, 0]
sys=control.tf(num,den)
gm, pm, wg, wp = control.margin(sys)
s = signal.lti(num,den)

w, mag, phase =signal.bode(s)
gain_y=np.full((len(w)),-4.81)
phase_y=np.full((len(w)),-180)

idx = np.argwhere(np.diff(np.sign(mag - gain_y))).flatten()
print ("The Freqency of intersection:",w[idx])
plt.figure()
plt.semilogx(w, mag) 
plt.plot(w,gain_y)
plt.plot(2.06, -4.81 ,'ro')
plt.ylabel("Gain")
plt.xlabel("Frequency")
plt.grid()

#if using termux
plt.savefig('./figs/ee18btech11036_3.pdf')
plt.savefig('./figs/ee18btech11036_3.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11036_3.pdf"))
#else
#plt.show()

