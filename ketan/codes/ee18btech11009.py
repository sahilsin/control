import numpy as np
import math

#if using termux
import subprocess
import shlex
#end if

#Function to  calculate the poles and zeros
#from the slopes in the Bode Plot
def CalculatePolesAndZeros(Slopes):
	dSlopes = Slopes[1:]-Slopes[:-1]
	Nz=0
	Np=0
	for i in dSlopes:
		if i%20!=0:
			return None
		if i>=0 :
			Nz+=i//20
		else:
			Np -= i//20
	return Np, Nz


Slopes = np.array([0,-20,-40,-60])
#Find the poles and Zeros
Np,Nz = CalculatePolesAndZeros(Slopes)

print("Number of Poles : " , Np)
print("Number of Zeros : " , Nz)

def getDenominatorFunction(Slopes):
    dSlopes = Slopes[1:]-Slopes[:-1]
    Den = []
    for i in range(len(dSlopes)):
            
        if dSlopes[i]%20!=0:
            return None
            
        if i == 0:
            Den = [0]

        else:
            Den += [-1*20**(i-1)]*(-dSlopes[i]//20)
            #print(Den)
        
    
    return np.array(Den)
Den =  getDenominatorFunction(Slopes)

def getNumeratorFunction(Den):
    Num = []
    product = 1
    for i in Den:
        a = np.sqrt(10**2 + i**2)
        product = product * a
    Num.append(product)
    
    return np.array(Num)

Num =  getNumeratorFunction(Den)
#print(Num)

print("poles are",Den)

    
num = Num
den = np.poly(Den)

print("Numerator is",num)
print("Denominator is",den)

from scipy import signal
import matplotlib.pyplot as plt
s1 = signal.lti(num, den) 

w, mag, phase = signal.bode(s1)

plt.figure()
plt.xlabel("$f$")
plt.xlim(0.1,40)

plt.ylabel("$|G(j\omega)|$")
plt.title("Bode Plot")
plt.semilogx(w, mag)    # Bode magnitude plot

x = np.array([0.1,1,20,40])
y = []
for i in x:
    k1 = Num[0]
    #k+=Slopes[i]
    k = 20* math.log10(k1)-20* math.log10(np.sqrt(i**2))-20* math.log10(np.sqrt(1**2 + i**2))-20* math.log10(np.sqrt(20**2 + i**2))
    y.append(k)

plt.plot(x,y)
plt.legend(["Calculated Bode Plot" , "Line Plot"])   
plt.grid()

#if using termux
plt.savefig('./figs/ee18btech11009/ee18btech11009.pdf')
plt.savefig('./figs/ee18btech11009/ee18btech11009.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11009/ee18btech11009.pdf"))
#else
#plt.show()
