#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  1 12:38:43 2020

@author: aayush
"""
#if using termux
import subprocess
import shlex

#end if
import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(1e-8,10,100)
y1 = 1 - ((np.exp(-5*t/6)*(np.sin(5*np.sqrt(119)*t/6) + np.sqrt(119)*np.cos(5*np.sqrt(119)*t/6))/np.sqrt(119)))
y2 = ((-0.576+0.185j)*np.exp((-1.334188-1.80535j)*t)*((0.812+0.583j) + np.exp(3.6107j*t))) + 0.152396*np.exp(-0.39829*t)+1
y3 = 666.6666*((0.000215*np.exp(-19.73*t)) - ((0.000182863-0.00023862j)*np.exp((-1-8.15j)*t)) - ((0.000182863+0.00023862j)*np.exp((-1+8.15j)*t)) + (0.00150348))
plt.xlabel("Time")
plt.ylabel("Unit Step Response")

plt.plot(t,np.real(y1),'b')
plt.plot(t,np.real(y2),'red')
plt.legend(("Uncompensated" , "Lag Compensator"))
plt.grid()
plt.show()
#if using termux
plt.savefig('./figs/ee18btech11001/ee18btech11001_3.pdf')
plt.savefig('./figs/ee18btech11001/ee18btech11001_3.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11001/ee18btech11001_3.pdf"))
#end if

plt.xlabel("Time")
plt.ylabel("Unit Step Response")

plt.plot(t,np.real(y1),'b')
plt.plot(t,np.real(y3),'red')
plt.legend(("Uncompensated" , "Lead Compensator"))
plt.grid()
#if using termux
plt.savefig('./figs/ee18btech11001/ee18btech11001_4.pdf')
plt.savefig('./figs/ee18btech11001/ee18btech11001_4.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11001/ee18btech11001_4.pdf"))
#end if