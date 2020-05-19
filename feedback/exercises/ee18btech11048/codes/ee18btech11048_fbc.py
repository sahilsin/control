# License
'''
Code by Adyasa
May 17,2020
Released under GNU GPL
'''

Vs = 1.0
#Vs = input("Enter Vs value") # Uncomment to enter own value of parameters
R1=1000.0
#R1 = input("Enter R1 value")
R2=1000.0
#R2 = input("Enter R2 value")
RL=1000.0
#RL = input("Enter RL value")
RM=1000.0
#RM = input("Enter RM value")
T =float((R1+R2+RM)/(R1*RM))
print("Value of T",T)
Io = float(Vs*T)
print("Value of Io",Io)
