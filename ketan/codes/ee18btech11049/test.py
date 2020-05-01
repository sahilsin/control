# Released under GNU-GPL
# By B Sai Laxman
# Dt.1st May

''
from scipy import signal
import matplotlib.pyplot as plt
from pylab import*
# import control
# from control import tf
#if using termux
import subprocess
import shlex
#endif


s = signal.lti([48, 35.184, 4.8],[1,10.7,32.595,23.325,0.38,0])#G_c(s)*G(s)

w,mag,phase = signal.bode(s)
subplot(2,1,1)
#plt.xlabel('Frequency(rad/s)')
plt.ylabel('Magnitude(deg)')
# plt.title('Magnitude plot')
plt.semilogx(w, mag,'b')        # Bode Magnitude plot
# plt.axhline(y = 0,xmin=0,xmax= .35,color = 'r',linestyle='dashed')
# plt.axvline(x = .22,ymin=0,color='k',linestyle='dashed')

plt.grid() 
plt.axvline(x = 1.49,ymin=0,color='k',linestyle='dashed')
plt.axhline(y =-0.95,xmin=0,color = 'r',linestyle='dashed')
plt.plot(1.49,0,'o')
plt.text(2,4.2, '({}, {})'.format(1.49,0))
plt.title("G(s)G_c(s)")


subplot(2,1,2)
plt.xlabel('Frequency(rad/s)')
plt.ylabel('Phase(deg)')
# plt.title('Phase plot')
plt.semilogx(w,phase)          # Bode phase plot
plt.axhline(y = -120.4,xmin=0,color = 'r',linestyle='dashed')
plt.axvline(x = 1.63,ymin=0,color='k',linestyle='dashed')
plt.plot(1.63,-120.4,'o')
plt.text(2,-110, '({}, {})'.format(1.63,-120.4))
plt.grid() 



# if using termux
plt.savefig('../../figs/ee18btech11049/ee18btech11049_2.pdf')
plt.savefig('../../figs/ee18btech11049/ee18btech11049_2.eps')
subprocess.run(shlex.split("termux-open ../../figs/ee18btech11049/ee18btech11049_2.pdf"))
#else
plt.show()
