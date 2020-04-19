# code by srikanth
import numpy as np
import matplotlib.pyplot as plt
import control

#values of omega (w)
OMEGA = np.linspace(-20, 20, 2001)

#defining transfer function
s = control.TransferFunction.s
G = 1/(s*(s**2+1))

#Using library getting mag and phase of the transfer function for resp. omegas
MAG, PHASE, W = G.freqresp(OMEGA)
#plotting the polar plot
ax = plt.subplot(111, projection='polar')

ax.plot(PHASE.reshape((2001,))[-995:-800],MAG.reshape((2001,))[-995:-800])
plt.show()
ax1 = plt.subplot(111, projection='polar')
ax1.text(-1,0, '(-1,0)')
plt.plot(-1,0,'x')
ax1.plot(PHASE.reshape((2001,))[-1000:],MAG.reshape((2001,))[-1000:])

plt.title("polar plot")
plt.show()
#plotting magintude versus omega
plt.plot(W, MAG.reshape((2001,)))

plt.title("Magnitude plot")
plt.xlabel("$\omega$")
plt.ylabel("|G(j$\omega$)|")
plt.xlim(-5, 5)
plt.show()

#plotting Phase versus omega
plt.plot(W, PHASE.reshape((2001,)))
plt.title("Phase plot")
plt.xlabel("w")
plt.ylabel("$Phase$")
plt.xlim(-10, 10)
plt.show()
