import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import signal

#if using termux
import subprocess
import shlex
#end if


omega=np.linspace(-10000,10000,20000)#range of omega values
print("enter no of zeros")
Z=input()#inputting no of zeors
zeros=np.zeros(Z)
if(Z>0):
	print("enter the ZEROS")
	for i in range(0,Z):
		zeros[i]=input()#inputting the zeros
print("enter no of poles:")
P=input()#inputting the no of poles

poles=np.zeros(P)
if(P>0):
	print("enter the POLES")
	for i in range(0,P):
		poles[i]=input()#inputting the poles
s=signal.ZerosPolesGain(zeros,poles,1) #s is transfer function with gain =1
w,H=signal.freqresp(s,w=omega)#frequency response of s
GAIN=(np.pi*np.exp(-0.25*1j*w))#enter the GAIN function here
H=H*GAIN#this gain is multiplied to existing frequency response


	

plt.plot(H.real,H.imag,"b")
plt.grid()

plt.xlim(-2,2)
plt.xlabel("real axis")
plt.ylim(-2,2)
plt.ylabel("imaginary axis")
plt.title("NYQUIST PLOT")

#if using termux
plt.savefig('./figs/ee18btech11007.pdf')
plt.savefig('./figs/ee18btech11007.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11007.pdf"))
#else
#plt.show()
