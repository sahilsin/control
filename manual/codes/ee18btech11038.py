import numpy as np 
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex
#end if
K = np.pi/3
w= np.linspace(pow(10,-1), pow(10,1),10000)

mag = 20*np.log(K/w)
phase = -90 - w*180/np.pi

fig, a = plt.subplots(2)
a[0].semilogx(w,mag)
a[0].semilogx(w,np.zeros(10000), color ='black' , linestyle = 'dashed')
a[0].semilogx((np.pi/3)*np.ones(10000), np.linspace(-50,50, 10000), color = 'red', linestyle ='dashed' )
a[0].set_title('Magnitude Plot')
a[0].set_ylabel('dB', size ='15')
a[0].legend(['_nolengend_', '0 dB line', 'w= pi/3 radian'], loc= 'lower left', prop={'size':10})

a[1].semilogx(w, phase)

a[1].semilogx(w,-150*np.ones(10000), color ='purple' , linestyle = 'dashed')

a[1].semilogx((np.pi/3)*np.ones(10000), np.linspace(-600,0, 10000), color = 'red', linestyle ='dashed' )
a[1].set_title('Phase Plot', x= 0.7)
a[1].set_xlabel('Frequncy in radian', size='15')
a[1].set_ylabel('degree', size= 15)
a[1].legend(['_nolengend_', '-150 degree line', '_nolegend_'], loc= 'lower left', prop={'size':12})

#if using termux
plt.savefig('./figs/ee18btech11038/ee18btech11038.pdf')
plt.savefig('./figs/ee18btech11038/ee18btech11038.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11038/ee18btech11038.pdf"))
#else
#plt.show()
