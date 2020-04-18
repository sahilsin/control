# Code by Abhishek Shetkar
# 16/04/2020
# Released under GNU GPL
import numpy as np
import matplotlib.pyplot as plt

w = 0
c = 0
y = 0

# defining a function whose solution of f=0 will give us the value of w for which |G(jw)| = 1
def s(w):									
	v = w*(1+w*w) - 1
	return v

#loop starts at w = 0, checks wether function is +ve, if not, then increases t by 0.001
while c == 0:				
	y = s(w) 						
	if y < 0:
		c = 0
		w = w+0.001

	else:
		c = 1				


#approx. the curve as a straight line, we find the crossing point by weighted mean of the two succesive values
w1 = ((w-0.001)*(-s(w-0.001)) + w*s(w))/(-s(w-0.001) + s(w)) 

print(w1)
phase = -(np.pi/2) - 2*np.arctan(w1)
print(phase)
