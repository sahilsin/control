'''Code by Kuntal Kokate
April 24th,2020
Released under GNU GPL
'''
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import signal

#if using termux
import subprocess
import shlex
#end if


omega= np.linspace(-100, 100,20000)
zeros=[]#a this list contains zeros of G(s)
poles=[0, -6, -9]#a this list contains poles of G(s)
H_s=signal.ZerosPolesGain(zeros,poles,1) # feed zeros and poles as inputs to this function to get
w, H=signal.freqresp(H_s,w=omega)#feed H_s and omega values as inputs to this funtion it will return frequency response H of H_s and w the range of omega values of H
GAIN=1#enter the GAIN function which could be either constant or variable
H=H*GAIN#we multiply GAIN function with H(jw) to get our  desired final transfer functions frequency response
#finally H is the frequency response of our desired Transfer Function

#Plotting the Nyquist plot
plt.plot(H.real, H.imag)
plt.plot(-0.00123, 0, 'ro')
plt.text(-0.00123, -0.005, "(-1/810, 0)")
plt.ylabel("${Im}\{G(j\omega)\}$")
plt.title("NYQUIST PLOT")
plt.xlabel("${Re}\{G(j\omega)\}$")
plt.grid()
plt.xlim(-0.0051, 0.0051)
plt.ylim(-0.02, 0.02)


# plot the zoomed portion
X_detail = H.real[4000:9500]
Y_detail = H.imag[4000:9500]
sub_axes = plt.axes([.6, .6, .25, .25])
sub_axes.grid()
sub_axes.plot(X_detail, Y_detail,c='k')
sub_axes.plot(-0.00123, 0, 'ro')
sub_axes.text(-0.00123, -0.0005, "(-1/810, 0)")
sub_axes.plot(H.real[-9500:-4000], H.imag[-9500:-4000], c='k')
sub_axes.set_xticks([])
sub_axes.set_yticks([])


#if using termux
plt.savefig('./figs/ee18btech11028_1.pdf')
plt.savefig('./figs/ee18btech11028_1.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11028_1.pdf"))
#else

plt.show()
