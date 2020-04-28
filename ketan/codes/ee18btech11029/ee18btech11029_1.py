###############################################
#Code by M.Sai Mehar
# April 28,2020
#Released under GNU GPL
##############################################



import control
import matplotlib.pyplot as plt
import numpy as np

#if using termux
import subprocess
import shlex
#end if

num1 = [81]  
den1 = [1,18,103,198,121]
num2 = [100]  
den2 = [1,18,101,180,100]
num3 = [121]  
den3 = [1,18,99,162,81]


#Creating a transfer function G = num/den
G1 = control.tf(num1,den1) 
G2 = control.tf(num2,den2) 
G3 = control.tf(num3,den3) 
w = np.logspace(-3,3,5000)

#Plotting the Nyquist plot
control.nyquist(G1,w,label='k=-9'); 
control.nyquist(G2,w,label='k=-10');
control.nyquist(G3,w,label='k=-11');
plt.plot(1,0,'o')
plt.annotate("(1,0)", (1, 0))
plt.legend()

#if using termux
plt.savefig('./figs/ee18btech11029/ee18btech11029_1.pdf')
plt.savefig('./figs/ee18btech11029/ee18btech11029_1.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11029/ee18btech11029_1.pdf"))
#else
#plt.show()




