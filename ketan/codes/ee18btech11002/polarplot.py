# Code by Abhishek Shetkar
# 16/04/2020
# Released under GNU GPL
import numpy as np
import matplotlib.pyplot as plt
import control
#if using termux
import subprocess
import shlex
#end if

w = np.linspace(-20,20,2001) #ranging omega

#G(s)
s = control.TransferFunction.s
G = 1/((s)*(1+s)*(1+s))                                       

Mag, Ph, W = G.freqresp(w)

#Plotiing polar plot

ax = plt.subplot(111, projection='polar')

ax.plot(Ph.reshape((2001,))[-995:-800],Mag.reshape((2001,))[-995:-800])

#if using termux
plt.savefig('./figs/ee18btech11002/ee18btech11002.pdf')
plt.savefig('./figs/ee18btech11002/ee18btech11002.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11002/ee18btech11002.pdf"))
#else
#plt.show()


#inverse polar plot G(s) ie. polar plot of 1/G(s)

s = control.TransferFunction.s
iG = (s)*(1+s)*(1+s)                                       

iMag, iPh, iW = iG.freqresp(w)

#Plotiing inverse polar plot

ax = plt.subplot(111, projection='polar')

ax.plot(iPh.reshape((2001,))[-995:-800],iMag.reshape((2001,))[-995:-800])

#if using termux
plt.savefig('./figs/ee18btech11002/ee18btech11002_1.pdf')
plt.savefig('./figs/ee18btech11002/ee18btech11002_1.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11002/ee18btech11002_1.pdf"))
#else
#plt.show()
