import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import subprocess
import shlex
#Open Loop Transfer function
A = 1e5
zeros = []
poles = [-100,-1e4,-1e4]
s1 = signal.lti(zeros,poles,A) 
w, mag, phase = signal.bode(s1)
plt.figure()
plt.title("Open Loop Gain")
plt.ylabel("20log|G(s)|")
plt.xlabel("w")
plt.grid()
plt.semilogx(w, mag)    # Bode magnitude plot
plt.show()

#if using termux
#plt.savefig('./figs/ee18btech11001/ee18btech11001_1.pdf')
#plt.savefig('./figs/ee18btech11001/ee18btech11001_1.eps')
#subprocess.run(shlex.split("termux-open ./figs/ee18btech11001/ee18btech11001_1.pdf"))

#Closed Loop Transfer function
Num = np.poly(zeros)
if len(zeros)==0:
    Num = np.array([Num])
Num = Num*(10**5)/Num[-1]
Den = np.poly(poles)
Den = Den/Den[-1]
Num1 = np.append(np.zeros(len(Den)-len(Num)) , Num)
Den = 0.002*Num1 + Den
H = signal.lti(Num , Den)
w1,mag1,phase1 = signal.bode(H,w)
plt.figure()
plt.title("Closed Loop Gain")
plt.ylabel("20log|H(s)|")
plt.xlabel("w")
plt.grid()
plt.semilogx(w1, mag1)    # Bode magnitude plot
plt.plot(w[0] , mag1[0], 'r.' , markersize=12)
plt.annotate("( %.2f, %.2f) \n  |H(s)| = %.2f" % (w[0] , mag1[0] , 10**(mag1[0]/20)) , (1.4,mag1[0]-10))
plt.show()

#if using termux
#plt.savefig('./figs/ee18btech11001/ee18btech11001_2.pdf')
#plt.savefig('./figs/ee18btech11001/ee18btech11001_2.eps')
#subprocess.run(shlex.split("termux-open ./figs/ee18btech11001/ee18btech11001_2.pdf"))


#Step Response
t = np.linspace(0,0.03,1000)
y = 500*(1 - np.exp(-200*t))
plt.figure()
plt.title("Step Response")
plt.ylabel("y(t)")
plt.xlabel("t")
plt.grid()
plt.plot(t,np.real(y))
plt.show()

#if using termux
#plt.savefig('./figs/ee18btech11001/ee18btech11001_3.pdf')
#plt.savefig('./figs/ee18btech11001/ee18btech11001_3.eps')
#subprocess.run(shlex.split("termux-open ./figs/ee18btech11001/ee18btech11001_3.pdf"))
