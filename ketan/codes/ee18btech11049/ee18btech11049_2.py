# Released under GNU-GPL
# By B Sai Laxman
# Dt.1st May

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.signal import  step
#if using termux
import subprocess
import shlex
#endif

# open loop T.F's
s1 = signal.lti([48], [1, 5,4,0])# G(s)
s5 = signal.lti([48, 35.184, 4.8],[1,10.7,32.595,23.325,0.38,0])#G_c(s)*G(s)
s4 = signal.lti([1,0.733,0.1],[1,5.7,0.095])#G_c(s)

# Closed loop T.F's
s2 = signal.lti([48], [1,5,4,48])#uncompensated
s3 = signal.lti([48, 35.184, 4.8], [1,10.7,80.6,58.5,5.18])#compensated

w1,mag1,phase1 = signal.bode(s1)
w2,mag2,phase2 = signal.bode(s5)
w3,mag3,phase3 = signal.bode(s4)

fig1,a = plt.subplots(2)

a[0].set_xlabel('Freq (in rad/s)')
a[0].set_ylabel('Mag (in dB)')
a[0].set_title('G(s) ')
a[0].semilogx(w1,mag1,label = 'Uncompensated')
# a[0].scatter(12.48,-12.07)
# a[0].annotate("$(w_{max}$,-12.07dB)",(14,-13))
a[0].legend()
a[0].grid()

a[1].set_xlabel('Freq (in rad/s)')
a[1].set_ylabel('Phase (in deg)')
# a[1].set_title('Phase plot ')
plt.axhline(y = -198.66,xmin=0,xmax= 3.015,color = 'r',linestyle='dashed')
plt.axvline(x = 3.015,ymin=0,ymax =1,color='k',linestyle='dashed')
plt.plot(3.015,-198.66,'o')
a[1].semilogx(w1,phase1,label = 'Uncompensated')
plt.text(3.2,-190.66, '({}, {})'.format(3.015,-198.66))
a[1].legend()
a[1].grid()

#if using termux
fig1.savefig('./figs/ee18btech11049/ee18btech11049_1.pdf')
fig1.savefig('./figs/ee18btech11049/ee18btech11049_1.eps')
#subprocess.run(shlex.split("termux-open ./figs/ee18btech11049/ee18btech11049_1.pdf"))



fig2,b = plt.subplots(2)

b[0].set_xlabel('Freq (in rad/s)')
b[0].set_ylabel('Mag (in dB)')
b[0].set_title('Total Compensated Plot ')
b[0].semilogx(w1,mag1,label = 'Uncompensated')
b[0].semilogx(w2,mag2,label = 'Compensated')
b[0].semilogx(w3,mag3,label = 'Compensator')
b[0].legend()
b[0].grid()


b[1].set_xlabel('Freq (in rad/s)')
b[1].set_ylabel('Phase (in deg)')
# b[1].set_title('Phase plot ')
b[1].semilogx(w1,phase1,label = 'Uncompensated')
b[1].semilogx(w2,phase2,label = 'Compensated')
b[1].semilogx(w3,phase3,label = ' Lead Compensator')
b[1].annotate('', (1.63,-175), (1.63,-120), arrowprops=dict(facecolor='red',arrowstyle='<|-|>',mutation_scale=15))
b[1].annotate('', (2,-10), (2,60), arrowprops=dict(facecolor='red',arrowstyle='<|-|>',mutation_scale=15))
b[1].annotate("Gain in Phase",(2.5,-160))
b[1].annotate("$\phi_{max}$",(3,20))
b[1].legend()
b[1].grid()







# if using termux
plt.savefig('./figs/ee18btech11049/ee18btech11049_3.pdf')
plt.savefig('./figs/ee18btech11049/ee18btech11049_3.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11049/ee18btech11049_3.pdf"))



#else
# plt.show()
