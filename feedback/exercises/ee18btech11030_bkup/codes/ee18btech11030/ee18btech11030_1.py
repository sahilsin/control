###################################################################

# This is python code for Bode plots.    
# By Moparthi Varun Sankar
# May 13 , 2020 
# Released under GNU GPL

###################################################################

import numpy as np
import matplotlib.pyplot as plt
import control

#if using termux
import subprocess
import shlex
#end if
j = 22
num = np.zeros(j, dtype = object)
den = np.zeros(j,dtype = object)
ans1 = np.zeros(j,dtype = object)
ans2 = np.zeros(j,dtype = object)
X2 = np.zeros(j,dtype = object)
Y2 = np.zeros(j,dtype = object)
X1 = np.zeros(j,dtype = object)
Y1 = np.zeros(j,dtype = object)
for k in range (0,j):
   num[k] = [k*2.5,0.000000000001]         # Coefficients of Numerator of Tranfer Function
   den[k] = [1,(2.1-(k*0.1))*25,625]       # Coefficients of Denominator of Tranfer Function
   
   ans1[k] = np.roots(num[k])   # Zeros of Transfer Fuunction
   ans2[k] = np.roots(den[k])

   X2[k] = [x.real for x in ans2[k]]
   Y2[k] = [x.imag for x in ans2[k]]
   plt.scatter(X2[k],Y2[k] ,marker = 'x',color = 'blue')  # Plotting poles of 
   X1[k] = [x.real for x in ans1[k]]
   Y1[k] = [x.imag for x in ans1[k]]
   plt.scatter(X1[k],Y1[k], color='orange')  # Plotting zeros of Transfer Function
plt.xlabel('Real axis')
plt.ylabel('Imaginary axis')
plt.text(-17.67,16.67,'({}, {})'.format(-17.67,17.67))
plt.text(-17.67,-17.67,'({}, {})'.format(-17.67,-17.67))
plt.text(-17.67,14.67,'Q factor = 0.707')
plt.text(-17.67,12.67,'K=0.686 ')
plt.text(0,25,'({}, {})'.format(0,25))
plt.text(0,-25,'({}, {})'.format(0,-25))
plt.text(0,23,'Q factor = infi,K=2.1 ')
plt.text(0,21,'K=2.1 ')
plt.text(-25,0,'({}, {})'.format(-25,0))
plt.text(-25,-2,'Q factor = 0.5')
plt.text(-25,-4,'K=0.1')
plt.text(-34.2,0,'   ({}, {})'.format(-34.2,0))
plt.text(-18.2,0,'   ({}, {})'.format(-18.2,0))
plt.text(-34.2,-2,'Q factor= 0.476' )
plt.text(-34.2,-4,'K=0' )


plt.title('Pole-Zero Plot for varying K (RC = 1/25)')
plt.legend()
plt.grid()

#if using termux
plt.savefig('./figs/ee18btech11030/ee18btech11030_fc1.pdf')
plt.savefig('./figs/ee18btech11030/ee18btech11030_fc1.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11030/ee18btech11030_fc1.pdf"))
#else
#plt.show()
