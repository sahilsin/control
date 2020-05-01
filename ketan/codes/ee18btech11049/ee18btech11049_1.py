# Released under GNU-GPL
# By B Sai Laxman
# Dt.1st May
import numpy as np
Tp=2
OS = 0.12
zeta = -np.log(OS)/(np.sqrt((np.pi)**2 + (np.log(OS))**2))
phi_m = np.arctan(2*zeta/(np.sqrt(-2*(zeta**2)+np.sqrt(4*(zeta**4)+ 1))))*(180/np.pi);
W_bw =  np.pi/(Tp*np.sqrt(1-(zeta**2)))*np.sqrt(1-2*(zeta**2)+np.sqrt(4*(zeta**4)-4*(zeta**2)+2))
print("Damping ratio = ",zeta)
print("Phase margin(in degrees) = ",phi_m)
print("Closed loop Bandwidth = ", W_bw)