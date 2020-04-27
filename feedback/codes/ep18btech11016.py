import numpy as np
import control.matlab as ml
import matplotlib.pyplot as plt

# If using termux
import subprocess
import shlex
#end if

# num is the numerator of the trasfer function which is (2s)
# dem is the denominator of the transfer function which is (0.25s + 1)(0.25s + 1)(0.5s + 1)
num = np.array([2, 0])
den = np.polymul(np.array([0.5, 1]), np.array([0.25, 1]))
den = np.polymul(den, np.array([0.25, 1]))

# Generating the transfer function
g = ml.tf(num, den)
print("The transfer function is: ", g)
print("The poles of the above function are ", ml.pole(g))
print("The zeros of the above function are ", ml.zero(g))

# Generating the bode plot as well as plotting it
mag, phase, w = ml.bode(g)

# If using termux
plt.savefig("./figs/ep18btech11016_plot.pdf")
plt.savefig("./figs/ep18btech11016_plot.eps")
subprocess.run(shlex.split("termux-open ./figs/ep18btech11016_plot.pdf"))
# else
plt.show()
