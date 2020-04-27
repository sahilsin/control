import numpy as np
import matplotlib.pyplot as plt 

t=np.linspace(-3,10,1000)
f=t*(np.exp(-t))*np.heaviside(t,1)
plt.plot(t,f,label='$h(t) = te^{-t}$')
plt.grid()
plt.xlabel('time(sec)')
plt.ylabel('h(t)')
plt.legend()
plt.show()

