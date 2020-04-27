import numpy as np
import matplotlib.pyplot as plt 

t=np.linspace(-3,100,1000)
undamped=2*np.cos(t)*np.heaviside(t,1)
underdamped=2*np.exp(-(0.05)*t)*np.cos(t)*np.heaviside(t,1)
critical_damped=(np.exp(-0.05*t)+np.exp(-0.05*t))*np.heaviside(t,1)
overdamped=(np.exp(-0.05*t)+np.exp(-0.03*t))*np.heaviside(t,1)

plt.plot(t,undamped,label='$h_1(t) = Undamped(\zeta = 0)$')
plt.plot(t,underdamped,label='$h_2(t) = Underdamped(0<\zeta<1)$')
plt.plot(t,critical_damped,label='$h_3(t) = Critical damped(\zeta = 1)$')
plt.plot(t,overdamped,label='$h_4(t) = Overdamped(\zeta>1)$')
plt.grid()
plt.xlabel('time(sec)')
plt.ylabel('h(t)')
plt.legend()
plt.show()

