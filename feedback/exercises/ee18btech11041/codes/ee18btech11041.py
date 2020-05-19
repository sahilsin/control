gm = 1e-3
R1=100
R3=100
ro=50e3
T=0.1


R2= T*R1*R3 -(R1+R3)
print('R2=', R2)

H=R1*R3/(R1+R2+R3)
print("H=",H)
H=9
G=1000/H
print ("G=",G)


par=((R2+R3)*R1/(R1+R2+R3))


mu=G*(ro+((1+gm*ro)*par))/(gm*ro)
print('mu=',mu)

Ro=ro+gm*ro*par+par
print("Ro = ",Ro)

Rout=Ro*(1+G*H)
print("Rout = ",Rout)

