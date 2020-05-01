'''
Code by C Shruti
April 27,2020
Released under GNU GPL
'''

import numpy as np
import math as mp
import matplotlib.pyplot as plt
from scipy import signal
import control
from control import tf
#if using termux
import subprocess
import shlex
#end if
w=[0.1,0.2,0.3,0.7,1.0,1.5,2.0,2.5,4.0,5.0,6.0,9.0,20.0,35.0,50.0,100.0]
H_w=[34,28,24.6,14.2,8,1.5,-3.5,-7.2,-10,-12.5,-14.7,-16.0,-17.5,-17.5,-18,-18.5]
plt.semilogx((w),H_w)
plt.grid()
#if using termux
plt.savefig('./figs/ee18btech11006/ee18btech11006_1.pdf')
plt.savefig('./figs/ee18btech11006/ee18btech11006_1.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11006/ee18btech11006_1.pdf"))
#end if
#plt.show()
