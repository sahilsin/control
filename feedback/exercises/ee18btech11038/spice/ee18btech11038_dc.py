
import numpy as np
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex
#end

data1 = np.loadtxt( 'ee18btech11038_dcid.data' )
#PLotting the data from spice simulation
time1 = data1[:, 0]*pow(10,6)
value1 = data1[:, 1]*pow(10,3)
#Loading the data
data = np.loadtxt( 'ee18btech11038_dcvin.data' )
#PLotting the data from spice simulation
time  = data[:, 0]*pow(10,6)
value = data[:, 1]


plt.subplot(2,1,1)
plt.plot(time1,value1)


plt.ylabel('Id2(mA)')
plt.title('DC drain current of MOSFET2')
plt.xlim([0,100])




plt.subplot(2,1,2)
plt.plot(time,value)


plt.xlabel('Time(us)')
plt.ylabel('Vin(V)')
plt.title('DC input voltage(VG1)')
plt.xlim([0,100])

plt.subplots_adjust(hspace=0.5)
#if using termux
plt.savefig('./figs/ee18btech11038/ee18btech11038_dc.pdf')
plt.savefig('./figs/ee18btech11038/ee18btech11038_dc.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11038_dc.pdf"))
# 


# plt.show()

