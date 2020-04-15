import numpy as np
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex
#end if

t=np.linspace(0,5,1000)
H1=np.array([])
H2 = np.array([])
H3 =[]
for i in t:
    h2=(25*i*np.exp(-5*i))*u(i)
    h3 = (30/np.sqrt(35))*u(i)*np.sin((np.sqrt(35)*i)/2)*np.exp(-5*i/2)
    h1 =(35/(2*np.sqrt(46)))*u(i)*(np.exp((-9+np.sqrt(46))*i)-np.exp((-9-np.sqrt(46))*i))
    H1 =np.append(H1,[h1])
    H2 = np.append(H2,[h2])
    H3 = np.append(H3,[h3])
plt.plot(t,(H1),label="overdamped")
plt.plot(t,H2,label="critically damped")
plt.plot(t,H3,label="underdamped")
plt.xlabel("t")
plt.ylabel("Transfer funtion in time domain")
plt.title("DIfferent types of systems")
plt.legend()
#if using termux
plt.savefig('./figs/ee18btech110012.pdf')
plt.savefig('./figs/ee18btech110012.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech110012.pdf"))
#else
#plt.show()
