#####################################################

# This is python code for the plot and energy of signal
# By M.Sai Mehar
# April 17 ,2020
# Released under GNU GPL




import numpy as np
import matplotlib.pyplot as plt

def u(t):
	y=np.heaviside(t,1)
	return y
	
T=np.linspace(-2.0001,2,10000)
Y=(2*u(T+2))-(3*u(T+1))+(u(T-2))
fig,ax=plt.subplots()
plt.plot(T,Y)


Ts=(2-(-2))/10000 
Eg=0 
k=0
for x in Y:
	k=(abs(x))**2
	Eg=Eg+k
Eg=Ts*(Eg) 
print("Value of Energy is : ",Eg)
	
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
plt.xlabel("t")
plt.ylabel("y(t)")
plt.show()
	
