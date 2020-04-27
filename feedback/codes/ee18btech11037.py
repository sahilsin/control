import matplotlib.pyplot as plt
import numpy as np
import math
#if using termux
import subprocess
import shlex
#end if

w = np.linspace(0,1000,100000)

#given bode phase plot 
y1 = []
for i in w:
	if i <= 0.01:
		y1.append(0)
	if i > 0.01 and i <0.1:
		y1.append(-90-45*(math.log10(i))) #eqn of straight line
	if i >= 0.1 and i <10:
		y1.append(-135-90*(math.log10(i))) #eqn of straight line
	if i >= 10 and i <100:
		y1.append(-180-45*(math.log10(i))) #eqn of straight line
	if i >= 100:
		y1.append(-270)


#bode phase plot for poles  0.1 and 10 only
y2 = []
for i in w:
	if i <= 0.01:
		y2.append(0)
	if i > 0.01 and i <100:
		y2.append(-45*(math.log10(i)+2)) #eqn of straight line
	if i >= 100:
		y2.append(-180)

#print(len(y1))
#print(len(y2))
		
plt.semilogx(w,y1,label='$\phi(\omega)$')
plt.axvline(x=0.1,dashes=[5, 5, 5, 5], color = 'c')
plt.axhline(y=-45,dashes=[5, 5, 5, 5], color = 'c')
plt.semilogx(w,y2,label='$\phi_2(\omega)$')
plt.title("Phase Plot")
plt.legend()
plt.grid()

#if using termux
plt.savefig('./figs/ee18btech11037/ee18btech11037_2.pdf')
plt.savefig('./figs/ee18btech11037/ee18btech11037_2.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11037/ee18btech11037_2.pdf"))
#else
#plt.show()
