import numpy as np 
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex
#end if
K = np.pi/3
w= np.linspace(pow(10,-1), pow(10,1),10000)

mag = 20*np.log(K/w)
phase = -90 - w*180/np.pi


plt.semilogx(w,mag)
plt.semilogx(w, phase)
plt.semilogx(w,-150*np.ones(10000), color ='purple' , linestyle = 'dashed')
plt.semilogx(w,np.zeros(10000), color ='black' , linestyle = 'dashed')
plt.semilogx((np.pi/3)*np.ones(10000), np.linspace(-200,50, 10000), color = 'red', linestyle ='dashed' )
plt.ylim([-200, 50])
plt.ylabel('phase in degrees & magnitude in dB')
plt.xlabel('frequency in radian')
plt.legend(['Magnitude', 'Phase','-150 degree line', 'dB 0 line', 'pi/3 radian line'], loc='upper right')
#if using termux
plt.savefig('./figs/ee18btech11038/ee18btech11038.pdf')
plt.savefig('./figs/ee18btech11038/ee18btech11038.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11038/ee18btech11038.pdf"))
#else
#plt.show()
