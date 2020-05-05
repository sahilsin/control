
from scipy import signal
import matplotlib.pyplot as plt
from pylab import*

#if using termux
import subprocess
import shlex
#end if

#closed loop transfer function
s1 = signal.lti([10],[1,3,2,10])
w, mag, phase = signal.bode(s1)



subplot(2,1,1)
plt.semilogx(w, mag,label='original plot of CLTF')
plt.ylabel('Mag(dB)')
plt.title('Magnitude plot')
plt.grid() 


#data points from intersection
x=[1.59,1.61,1.66,1.68,1.78,1.8,1.82,1.85,1.98,2.07,2.37,2.61,3.17,8.47]
y=[11.84,12.48,13.08,13.64,13.64,13.08,12.48,11.84,7.640,5.153,-0.81,-4.29,-10.17,-40]
plt.plot(x,y,'r',label='plot using M circles')
plt.legend()



subplot(2,1,2)
x=[6.684,7.563,7.673,8.532,9.401,10.011,10.310,10.920,11.360,11.820,12.192,12.828,12.908,12.9185,13.827,14.097,15.046,15.426,16.820,20.450,24.770,34.139,40.910,58.440]
y=[113.49,111.03,111.03,109.02,107.35,105.94,105.94,104.74,104.74,104.74,103.70,103.70,102.80,102.01,102.01,101.30,102.01,101.30,102.80,101.30,102.80,77.73,78.46,73.61]
plt.plot(x,y,'r',label='plot using N circles')
plt.semilogx(w, phase,label='original plot of CLTF')
plt.grid()     # Bode phase plot
plt.xlabel('Frequency(rad/s)')
plt.ylabel('Phase(deg)')
plt.title('Phase plot')
plt.legend()
#if using termux
plt.savefig('./figs/ee18btech11020/ee18btech11020_fig3.pdf')
plt.savefig('./figs/ee18btech11020/ee18btech11020_fig3.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11020/ee18btech11020_fig3.pdf"))

#else
plt.show()


