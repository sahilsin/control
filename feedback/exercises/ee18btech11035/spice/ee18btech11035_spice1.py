# License
'''
Code by Aashrith
May 19th,2020
Released under GNU GPL
'''
import numpy as np  
import matplotlib.pyplot as plt


#if using termux
import subprocess
import shlex
#end if

data=np.loadtxt('ee18btech11035_spice1.dat')  
plt.plot(data[:,0],data[:,1])  
plt.grid()
plt.xlabel("time(sec)")
plt.ylabel("Open loop Ciruit magnitude response")
plt.title('Spice simulation for Open-loop System')

#if using termux
#plt.savefig('./figs/ee18btech11035/ee18btech11035_spice_result1.pdf')
#plt.savefig('./figs/ee18btech11035/ee18btech11035_spice_result1.eps')
#subprocess.run(shlex.split("termux-open ./figs/ee18btech11035/ee18btech11035_spice1.pdf"))
#else
plt.show()
