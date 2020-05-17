###################################################################

# This is python code for time response.    
# By Harsh kabra
# 12 may , 2020 
# Released under GNU GPL

###################################################################

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.signal import  step

#if using termux
import subprocess
import shlex
#endif

#closed loop TF's
sig1 = signal.lti([1], [5/6, 10/9 ,6 ,4/3,1])              
sig2 = signal.lti([13.2,100,132],
[5/6,10/9+13.2,6+100,4/3+132])
 
ans =0;
plt.figure()
t2,s2 = step(sig2)
for i in range(1,len(s2)-1):
	if s2[i] > s2[i-1] and s2[i] > s2[i+1]:
		ans = max(ans,s2[i])
print("Peak overshoot: ",ans)		
t1,s1 = step(sig1)
plt.subplot(2,1,1)
plt.title("Time responses")
plt.plot(t1,s1,label = "original")
plt.grid()
plt.legend()

plt.subplot(2,1,2)
plt.plot(t2,s2,label = "Controlled")
plt.grid()
plt.legend()
plt.savefig('ee18btech11019_7.eps')
plt.show()
print("steady state output", s2[len(s2)-1])

#if using termux
plt.savefig('./figs/ee18btech11019_7.pdf')
plt.savefig('./figs/ee18btech11019_7.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11019_7.pdf"))
#else
#plt.show()