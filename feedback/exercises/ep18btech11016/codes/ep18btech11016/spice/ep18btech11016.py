import numpy as np  
from matplotlib import pyplot as plt  

#if using termux
import subprocess
import shlex
#end if

data1 = np.loadtxt('ep18btech11016_ol_gain.dat')  
plt.plot(data1[:,0],data1[:,1])  
plt.grid()
plt.xlabel("Time")
plt.ylabel("Gain")
plt.title('Open loop gain')

# if using termux
plt.savefig('./figs/ep18btech11016/ep18btech11016_ol_gain.pdf')
plt.savefig('./figs/ep18btech11016/ep18btech11016_ol_gain.eps')
subprocess.run(shlex.split("termux-open ./figs/ep18btech11016/ep18btech11016_ol_gain.pdf"))
# else
#plt.show()

data2 = np.loadtxt('ep18btech11016_feed_gain.dat')  
plt.plot(data2[:,0],data2[:,1])  
plt.grid()
plt.xlabel("Time")
plt.ylabel("Gain")
plt.title('Feedback gain')

# if using termux
plt.savefig('./figs/ep18btech11016/ep18btech11016_feed_gain.pdf')
plt.savefig('./figs/ep18btech11016/ep18btech11016_feed_gain.eps')
subprocess.run(shlex.split("termux-open ./figs/ep18btech11016/ep18btech11016_feed_gain.pdf"))
# else
#plt.show()

data3=np.loadtxt('ep18btech11016_cl_gain.dat')  
plt.plot(data3[:,0],data3[:,1])  
plt.grid()
plt.xlabel("Time")
plt.ylabel("Gain")
plt.title('Closed loop gain')

# if using termux
plt.savefig('./figs/ep18btech11016/ep18btech11016_cl_gain.pdf')
plt.savefig('./figs/ep18btech11016/ep18btech11016_cl_gain.eps')
subprocess.run(shlex.split("termux-open ./figs/ep18btech11016/ep18btech11016_cl_gain.pdf"))
# else
#plt.show()


