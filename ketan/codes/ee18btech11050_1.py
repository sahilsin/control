#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 21:06:20 2020

@author: krati
"""
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np


#if using termux
import subprocess
import shlex
#end if

zeros = []
poles = [0,-3,-6]

s1 = signal.ZerosPolesGain(zeros, poles, [50])
omega= np.linspace(-100, 100,20000)

w, H = signal.freqresp(s1, w=omega)

plt.figure()
plt.plot(H.real, H.imag, )
plt.plot(-1,0, 'ro')
plt.text(-1,0, "(-1,0)")
plt.plot(-0.3, 0, 'bo')
plt.text(-0.3, 0, "(-0.3,0)")
plt.ylabel("${Im}\{G(s)\}$")
plt.title("NYQUIST PLOT")
plt.xlabel("${Re}\{G(s)\}$")
plt.grid()
plt.xlim(-1.3, 0.2)
plt.ylim(-1, 1)

#if using termux
plt.savefig('./figs/ee18btech11050_1.eps')
plt.savefig('./figs/ee18btech11050_1.pdf')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11050_1.pdf"))
#else
#plt.show()
