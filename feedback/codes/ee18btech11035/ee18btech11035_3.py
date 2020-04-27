import numpy as np
import matplotlib.pyplot as plt 

t=np.linspace(-3,10,1000)
f=(1-np.exp(-t)-t*np.exp(-t))*np.heaviside(t,1)
plt.plot(t,f,label='$y(t) = 1-e^{-t}-te^{-t}$')
plt.grid()
plt.xlabel('time(sec)')
plt.ylabel('y(t)')
plt.legend()
plt.show()
