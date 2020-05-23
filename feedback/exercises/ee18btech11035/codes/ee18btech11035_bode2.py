# License
'''
Code by Aashrith
May 19th,2020
Released under GNU GPL
'''

from scipy import signal
import matplotlib.pyplot as plt
from pylab import*

s1 = signal.lti([2*np.pi*(10**6)],[1,2*np.pi*10010])

w,mag,phase = signal.bode(s1)

subplot(2,1,1)
plt.ylabel('20log|G(s)|')
plt.title('Magnitude plot')
plt.semilogx(w, mag)        # Bode Magnitude plot
plt.semilogx(w,37*np.ones(len(w))) 
plt.annotate("A(62800,37)",(62800,37))
plt.grid() 

subplot(2,1,2)
plt.xlabel('Frequency(rad/s)')
plt.ylabel('Phase(deg)')
plt.title('Phase plot')
plt.semilogx(w,phase)          # Bode phase plot
plt.grid() 

#if using termux
#plt.savefig('./figs/ee18btech11035/ee18btech11035.pdf')
#plt.savefig('./figs/ee18btech11035/ee18btech11035.eps')
#subprocess.run(shlex.split("termux-open ./figs/ee18btech11035/ee18btech11035_bode2.pdf"))
#else
plt.show()

