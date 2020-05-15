#Code by B.Varuni
#Date 15 May,2020
#Released Under GNU GPL

import numpy as np

#if using termux
import subprocess
import shlex
#end if

G_o = 1000                    #open loop gain
H = 0.099                     #feedback factor
p1 = 2*np.pi*10**3            #Dominating pole
p2_1 = (p1/4)*(np.sqrt(2*(H*G_o+1))+ np.sqrt(2*(H*G_o+1)-4))**2
p2_2 = (p1/4)*(np.sqrt(2*(H*G_o+1))- np.sqrt(2*(H*G_o+1)-4))**2

print('The values of p2 possible are {0} and {1}'.format(p2_1,p2_2))
