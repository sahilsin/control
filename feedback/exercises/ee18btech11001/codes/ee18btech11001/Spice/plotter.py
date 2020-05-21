#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 18:31:09 2020

@author: aayush
"""


import numpy as np
import matplotlib.pyplot as plt


#Spice plot is stored in spice.txt
A = np.genfromtxt("spice.txt")[1:]


plt.figure()
plt.title("Spice Results")
plt.ylabel("y(t)")
plt.xlabel("t")
plt.grid()
plt.plot(A[:,0],A[:,1])
plt.show()

#if using termux
#plt.savefig('./figs/ee18btech11001/ee18btech11001_3.pdf')
#plt.savefig('./figs/ee18btech11001/ee18btech11001_3.eps')
#subprocess.run(shlex.split("termux-open ./figs/ee18btech11001/ee18btech11001_3.pdf"))
