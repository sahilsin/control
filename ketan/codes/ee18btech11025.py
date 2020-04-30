import control
import matplotlib.pyplot as plt
import numpy

#if using termux
import subprocess
import shlex

num = [100,500]  #numerator of transfer function
den = [1,3,4,12,0]  #denominator of transfer function

#Creating a transfer function G = num/den
G = control.tf(num,den) 
w = numpy.logspace(-3,3,5000)
print(G)

control.nyquist(G,w); # nyquist plot
plt.savefig('./figs/ee18btech11025/nyquist.pdf')
plt.savefig('./figs/ee18btech11025/nyquist.eps') #if using termux
subprocess.run(shlex.split("termux-open ./figs/ee18btech11025/nyquist.pdf"))

p, z = control.pzmap(G); #pole-zero plot
print('poles:', p)
print('zeros:', z)
plt.savefig('./figs/ee18btech11025/polezero.pdf')
plt.savefig('./figs/ee18btech11025/polezero.eps') #if using termux

subprocess.run(shlex.split("termux-open ./figs/ee18btech11025/polezero.pdf")) #if using termux
