###################################################################

# This is python code for Bode plots.    
# By Moparthi Varun Sankar
# May 13 , 2020 
# Released under GNU GPL

###################################################################

from scipy import signal
import matplotlib.pyplot as plt
from pylab import*


#if using termux
import subprocess
import shlex
#end if
j = 22
s = np.zeros(j,dtype = object)
w = np.zeros(j,dtype = object)
mag = np.zeros(j,dtype = object)
phase = np.zeros(j,dtype = object)
m = 0

#Defining the transfer function 
for k in range (6,j,2):
   m = 1000.00/(2.1000001-k*0.1)
   s[k] = signal.lti([k*0.1,2.1*k*0.1*5,k*0.1*25], [1,(2.1-(k*0.1))*5,25])  #G(s)
    
#signal.bode takes transfer function as input and returns frequency,magnitude and phase arrays
   w[k],mag[k],phase[k] = signal.bode(s[k],n=100000)
   plt.semilogx(20*log(w[k]), mag[k],label = m/1000.00 )   
     

plt.grid()
plt.xlabel('Frequency(rad/s)')
plt.ylabel('Magnitude(db)')
plt.title('Normalised gain for different Q-Factors for RC = 1/5')

plt.legend()



#if using termux
plt.savefig('./figs/ee18btech11030/ee18btech11030_fc.pdf')
plt.savefig('./figs/ee18btech11030/ee18btech11030_fc.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11030/ee18btech11030_fc.pdf"))
#else
#plt.show()
