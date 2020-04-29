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
# num=[40]
# den=[1, 1, 0]
sys=control.tf(num,den)
gm, pm, wg, wp = control.margin(sys)
print ("phase margin:",pm)
print ("gain crossover frequency:",wp )
s = signal.lti(num,den)

w, mag, phase =signal.bode(s)
gain_y=np.full((len(w)),-4.81)
phase_y=np.full((len(w)),-180)


plt.subplot(2,1,1)
plt.semilogx(w, mag) 
plt.plot(w,gain_y)
plt.plot(2.06, -4.81 ,'ro')
#plt.text(wp ,0,'({}, {})'.format(wp, 0))
plt.ylabel("Gain")
plt.xlabel("Frequency")
plt.grid()


plt.subplot(2,1,2)
plt.semilogx(w, phase)
plt.plot(w, phase_y)
plt.plot(wp,-180+pm,'ro')
plt.plot(wp,-180,'ro')
plt.text(wp ,-180+pm,'({}, {})'.format(wp, -180+pm))
plt.text(wp ,-180,'({}, {})'.format(wp, -180))
plt.ylabel("Phase")
plt.xlabel("Frequency")
plt.grid()

#if using termux
plt.savefig('./figs/ee18btech11036_1.pdf')
plt.savefig('./figs/ee18btech11036_1.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11036_1.pdf"))
#else
#plt.show()
