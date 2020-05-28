
import numpy as np
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex
#end

data1 = np.loadtxt( 'ee18btech11038_clgin.data' )
#PLotting the data from spice simulation
time1 = data1[:, 0]*pow(10,6)
# value1 = data1[:, 1]*pow(10,6)
#Loading the data
data = np.loadtxt( 'ee18btech11038_clgout.data' )
#PLotting the data from spice simulation
time  = data[:, 0]*pow(10,6)
value = data[:, 1]*pow(10,6)


plt.subplot(2,1,1)
plt.plot(time1,value1)

plt.xticks([10*x for x in range(0, 11)])
plt.yticks([x/2 for x in range(-2,3)])

plt.ylabel('Is(uA)')
plt.title('Small Signal Input')
plt.xlim([0,100])

plt.axhline(y= value1[0], color='r', linestyle='--')
print('Input Oscillation Amplitude = ', max(value1) - value1[0], 'uA')
plt.annotate(s='', xy=(time1[np.argmax(value1)], max(value1)), xytext=(time1[np.argmax(value1)],value1[0]), arrowprops=dict(arrowstyle='<->'))
plt.text(time1[np.argmax(value1)]+ 1, (max(value1) + value1[0])/2, 'Amp=1uA' )


plt.subplot(2,1,2)
plt.plot(time,value)
# plt.xlim(0,0.09)
plt.xticks([10*x for x in range(0, 11)])
plt.yticks([x for x in range(191, 203)])

plt.xlabel('Time(us)')
plt.ylabel('Io(uA)')
plt.title('Output from Amplifier')
plt.xlim([0,100])
# print(time[0])
plt.axhline(y= value[0], color='r', linestyle='--')
print('Output Oscillation Amplitude = ', max(value) - value[0], 'uA')
plt.annotate(s='', xy=(time[np.argmax(value)], max(value)), xytext=(time[np.argmax(value)],value[0]), arrowprops=dict(arrowstyle='<->'))
plt.text(time[np.argmax(value)]+ 1, (max(value) + value[0])/2, 'Amp=4.96uA')
print('Closed Loop Gain = ', -(max(value)-value[0]))
plt.subplots_adjust(hspace=0.5)
#if using termux
plt.savefig('./figs/ee18btech11038/ee18btech11038_clgain.pdf')
plt.savefig('./figs/ee18btech11038/ee18btech11038_clgain.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11038_clgain.pdf"))
# plt.savefig('./ee18btech11038_clgain.pdf')
# plt.savefig('./ee18btech11038_clgain.eps')

# plt.show()

