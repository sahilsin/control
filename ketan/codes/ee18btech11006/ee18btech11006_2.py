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
import subprocess
import shlex
w1=[0.1,0.2,0.3,0.7,1.0,1.5,2.0,2.5,4.0,5.0,6.0,9.0,20.0,35.0,50.0,100.0]
H_w=[34,28,24.6,14.2,8,1.5,-3.5,-7.2,-10,-12.5,-14.7,-16.0,-17.5,-17.5,-18,-18.5]
plt.semilogx((w1),H_w,'b',label='Given Frequency response data')
system = signal.lti([1,8.5,15], [1,0.8,0.07])
r = np.linspace(0.1, 100,1001)
w, mag, phase = signal.bode(system, w=r)
plt.semilogx(w,(mag),'g',label='Bode plot of Transfer Function')    # Bode magnitude plot
plt.ylabel("[dB]")
plt.xlabel("[rad/s]")
plt.grid()
plt.legend()

#if using termux
plt.savefig('./figs/ee18btech11006/ee18btech11006_2.pdf')
plt.savefig('./figs/ee18btech11006/ee18btech11006_2.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11006/ee18btech11006_2.pdf"))
#end if
#plt.show()

