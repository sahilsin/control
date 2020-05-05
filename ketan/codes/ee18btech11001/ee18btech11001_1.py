#if using termux
import subprocess
import shlex

#end if
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
s1 = signal.lti([250], [3,5,0]) 
#Transfer function is(1/(s^2+ 202s + 400))
w, mag, phase = signal.bode(s1)
plt.figure()
plt.xlabel('w')
plt.ylabel('magnitude')
plt.semilogx(w, mag)    # Bode magnitude plot
plt.grid()
plt.show()
plt.figure()
plt.xlabel('w')
plt.ylabel('phase')
plt.semilogx(w, phase)  # Bode phase plot
plt.grid()
plt.show()
Phi_m = 45
GWc = 8.78
for i in range(len(phase)):
    if abs(phase[i] - Phi_m +180) < 2:
        p1 = (w[i] , phase[i])
        p2 = (w[i] , mag[i])
    if abs(mag[i] - 10) <0.2:
        p3 = (w[i] , mag[i])

plt.title("Magnitude plot of G(s)")   
plt.xlabel('w')
plt.ylabel('magnitude')
plt.semilogx(w, mag)
plt.plot(p2[0], p2[1], 'r.' , markersize=12)
plt.annotate("( %.2f, %.2f)" % (p2[0] , p2[1]) , p2)
plt.plot(p3[0], p3[1], 'r.' , markersize=12)
plt.annotate("( %.2f, %.2f)" % (p3[0] , p3[1]) , p3, xytext=(p3[0]-4, p3[0]-3))
plt.grid()
plt.show()

#if using termux
plt.savefig('./figs/ee18btech11001/ee18btech11001_1.pdf')
plt.savefig('./figs/ee18btech11001/ee18btech11001_1.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11001/ee18btech11001_1.pdf"))
#end if
plt.title("Phase plot of G(s)")  
plt.semilogx(w, phase)
plt.xlabel('w')
plt.ylabel('phase')
plt.plot(p1[0], p1[1], 'r.' , markersize=12)
plt.annotate("( %.2f, %.2f)" % (p1[0] , p1[1]) , p1)
plt.grid()
plt.show()
#if using termux
plt.savefig('./figs/ee18btech11001/ee18btech11001_2.pdf')
plt.savefig('./figs/ee18btech11001/ee18btech11001_2.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11001/ee18btech11001_2.pdf"))
#end if
