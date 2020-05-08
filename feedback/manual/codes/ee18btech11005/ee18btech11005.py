#Code by B.Varuni
#2nd May, 2020
#Released under GNU GPL
import numpy as np

#enter the values of resistances of op amp
R_1 = float(input("Enter the value of R_1:"))
R_2 = float(input("Enter the value of R_2:"))
G = float(input("Enter the gain of amplifier:")) #open loop gain
print("----------------")
#Computing open loop gain of amplifier
OLP = G
print("Open Loop gain of given amplifier is :",OLP)

#Computing the feedback factor
H = R_1/(R_1+R_2)
print("The feedback factor is :",H)

#Computing loop gain of amplifier
LP = G*H
print("Loop gain of given amplifier is :",LP)

#Computing closed loop gain
CLP = G/(1+G*H)
print("Closed Loop gain of given amplifier is :",CLP)

#Computing the amount of feedback
AOF = 1+G*H
print("Amount of feedback of given amplifier is :",AOF)
