############################################################
#coded by M.Sai Mehar
#Date April 17,2020
#Released under GNU GPL
###########################################################

import numpy as np
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex
#end if

w = np.append(np.linspace(0.01,1,100),np.linspace(1,1000,10000)) #ranging omega

#|G(jw)|
modGjw = ((np.sqrt(1+(w*w)/29*29))*(np.sqrt(1+(w*w)/40*40)))/(w*w*w*(np.sqrt(1+(w*w)/200*200))*(np.sqrt(1+(w*w)/1000*1000)))                                        

# Phase G(jw)
phase = (np.pi/2) + np.arctan(w/29) + np.arctan(w/40) - np.arctan(w/200) - np.arctan(w/1000)                          

#x-coordinate in polar plot is |G(jw)|*cos(Phase)
x = modGjw*np.cos(phase)
#y-coordinate in polar plot is |G(jw)|*sin(Phase)                                      
y = modGjw*np.sin(phase)  

plt.grid()
plt.plot(x,y)
plt.xlim([-5,0])
plt.ylim([0,1000])

#if using termux
plt.savefig('./figs/ee18btech11029.pdf')
plt.savefig('./figs/ee18btech11029.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11029.pdf"))
#else
#plt.show()

