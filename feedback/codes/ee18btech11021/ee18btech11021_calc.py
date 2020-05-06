#Coded by J. Prabhath
#1st May, 2020
#Released under GNU GPL

mu = 1e3
Rs = float('inf')
Rid = float('inf')
ro1 = 1e3
R1 = 10e3
R2 = 90e3
gm = 5e-3
ro2 = 20e3

#Calculations

Ri = 1/(1/Rs + 1/Rid + 1/(R1+R2))
print(f"Ri = {(Ri)/10**3:.2f}k\u03A9")
#Ri is in order of kilo-ohms

gm_inv = 1/gm
print(f"1/gm = {gm_inv:.2f}\u03A9")
#1/gm is in order of ohms

G = -mu*(Ri*(R1+R2))/(R1*R2)
print(f"G = {G:.2f}")

H = -R1/(R1+R2)
print(f"H = {H:.2f}")

T = 1/H
print(f"T = {T:.2f}")

Rin = R2/mu
print(f"Rin = {Rin:.2f}\u03A9")
#Rin is in order of ohms

Ro = gm*ro2*R1*R2/(R1+R2)
print(f"Ro = {Ro/10**3:.2f}k\u03A9")
#Ro is in order of kilo-ohms

Rout = (1 + G*H)*Ro
print(f"Rout = {Rout/10**6:.2f}M\u03A9")
#Rout is in order of Mega-ohms
