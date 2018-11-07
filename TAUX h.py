T = float(input())
Tinf = float(input()) #T recherchée
beta = 1/Tinf
g = 9.80665 #accel.
vc = float(input("Viscosité cinématique: ")) #viscosité cinématique du fluide (m/s²)
vt = float(input("Viscosité thermique: ")) #viscosité thermique du fluide
alpha = float(input("Diffusivité thermique: "))  #diffusivité thermique d'un fluide
ep = float(input("Epaisseur de la paroi: ")) #épaisseur de la paroi (m)
H = float(input("Hauteur du dispositif: ")) #hauteur
long = float(input("Longueur: ")) #longueur
deltaT = T - Tinf
l = float(input()) #conductivité thermique du fluide

Q = 0.001578 #débit minimale en m^3/s
U = Q/(H*long) #vitesse d'écoulement
PI1 = beta*deltaT
PI2 = g*(ep**3)/(vc**2)

GrL = PI1*PI2 #nombre de Grashof
ReL = U*long/v #nombre de Reynolds
ratio = GrL/ReL**2
Pr = vt/alpha #nombre de Prandtl
RaL = GrL*Pr #nombre de Rayleigh
NuL = 0.678((Pr/(0.952 + Pr))**0.25)*RaL**0.25
h = NuL*L/l #nombre de Nusselt




q = h*deltaT