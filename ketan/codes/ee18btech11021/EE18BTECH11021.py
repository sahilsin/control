#Coded by J. Prabhath
#14th April, 2020
#Released under GNU GPL

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-5,5,100)

#For the given Output function y(t)
def f1(t):
	arr = np.zeros(len(t))
	for i in range(len(t)):
		if(t[i] < 0):
			arr[i] = 0
		else:
			arr[i] = 1 - np.exp(-2*t[i])
	return arr

#For Input i.e Step Function u(t)	
def f2(t):
	arr = np.zeros(len(t))
	for i in range(len(t)):
		if(t[i] < 0):
			arr[i] = 0
		else:
			arr[i] = 1
	return arr

#For impulse response h(t)	
def f3(t):
	arr = np.zeros(len(t))
	for i in range(len(t)):
		if(t[i] < 0):
			arr[i] = 0
		else:
			arr[i] = 2*np.exp(-2*t[i])
	return arr
			
y = f1(t)
x = f2(t)
h = f3(t)
plt.plot(t,y,label = '$y(t) = (1 - e^{-2t})u(t)$')
plt.plot(t,x,label = '$x(t) = u(t)$')
plt.plot(t,h,label = '$h(t) = 2e^{-2t}u(t)$')
plt.xlabel('t')
plt.title('Input, Output and Impulse Response')
plt.grid()
plt.legend()
plt.show()
