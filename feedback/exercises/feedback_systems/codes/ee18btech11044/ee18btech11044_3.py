import numpy as np
import matplotlib.pyplot as plt


#if using termux
import subprocess
import shlex
#end


w = 1
x1 = []
y1 = []
x2 = []
y2 = []
for i in np.arange(-10,10,0.0001):
    if(i != 0):
        Q = 1/(2-i)
        x = w/Q
        if((x**2 - 4*(w**2))>= 0 ): 
            p1 = (-(x) + np.sqrt(x**2 - 4*(w**2)))/2
            p2 = (-(x) - np.sqrt(x**2 - 4*(w**2)))/2
            x1.append(p1)
            y1.append(0)
            x2.append(p2)
            y2.append(0)
        elif((x**2 - 4*(w**2))< 0 ):
            p1r = (-x)/2
            p1i = np.sqrt(4*(w**2)-x**2 )/2
            p2r = (-x)/2
            p2i = -np.sqrt(4*(w**2)-x**2 )/2
            x1.append(p1r)
            y1.append(p1i)
            x2.append(p2r)
            y2.append(p2i)


            



plt.plot([0,0],[-2,2],'r--',lineWidth=1,label='R2/R1 = 2')
plt.plot(x1,y1,label='pole-1')
plt.plot(x2,y2,label='pole-2')
plt.title('Z-plane')
plt.xlabel('Real part')
plt.ylabel('Imaginery part')
plt.legend()
plt.grid()
#if using termux
plt.savefig('./figs/ee18btech11044/ee18btech11044_3_1.pdf')
plt.savefig('./figs/ee18btech11044/ee18btech11044_3_1.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11044_3_1.pdf"))
#plt.show()
