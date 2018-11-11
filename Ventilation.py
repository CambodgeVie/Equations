"""

Système d'équations du bloc effet de serre

Auteur : groupe n°1

Date : 9 novembre 2018

Entrée: la masse de poivre (banane) à sécher, les humidités initiale et finale du produit (cf. cahier des charges), la
 durée de séchage, la température de l'air entrant, les chaleurs latentes massique (Lk) et molaire (Lm) de vaporisation de l'air, la capacité calorifique
 massique de l'air

Sortie : le débit minimal d'air à fournir pour que le séchage soit bien effectué

"""
from math import e

Lm = 40770                                  # Chaleur latente molaire de vaporisation de l'eau,     unités : J/mol
Lk = 2.265 * 10**6                           # Chaleur latente massique de vaporisation de l'eau,    unités : J/kg
cp = 1005                                   # Capacité calorifique massique de l'air sec,           unités : J/(K*kg)
R = 8.314                                   # Constante des gazs parfaits,                          unités :J/(K*mol)
Pref = 101325                               # Pression de référence, ici = Patm,                    unités : Pa
Tref = 373.15                               # Température de référence, ici = air à 100°C,          unités : K
Me = 18                                     # Masse molaire de l'eau (arrondie),                    unités : kg/mol
Ma = 29                                     # Masse molaire de l'air sec (arrondie),                unités : kg/mol
Ts = 65 + 273.15                            # Température (souhaitée de l'air ambiant),             unités : K
Mp = float(input('Masse à sécher: ', ))      # Masse de poivre (banane à sécher),                    unités : kg
x0 = float(input('Humidité initiale: ', ))   # Humidité initiale du produit,                         unités : kg.e/kg m.s
xf = float(input('Humidité finale: ', ))    # Humidité finale du produit,                           unités : kg.e/kg m.s
ts = float(input('Durée de séchage: ' , ))   # Durée du séchage,                                     unités : s


def Psat(T) :                                               # Pression de saturation de l'air à une température T
    P = Pref * e**(-Lm/R * (1/T - 1/Tref))                          # Expression de la pression
    return P

def Ysat(T):                                                # Humidité de l'air saturé en eau à la température T
    Ysat = Me/Ma * (Psat(T)/Pref)/(1 - Psat(T)/Pref)                  # Expression de l'humidité
    return Ysat

def deltaT(T) :                                             # Différence entre les températures de l'air entrant et
                                                            # sortant
    deltaT = Ts - T
    return deltaT

def Q1(dT) :                                                 # Première fonction du delta T (dT) pour le débit Q
    Masse_eau_a_evaporer = Mp/(1+x0) * (x0 - xf)
    Q1 = 10 * Masse_eau_a_evaporer * (1/ts) * 1/(Ysat(Ts - dT))
    return Q1

def Q2(dT):                                                 # Deuxième fonction du delta T (dT) pour le débit Q
    Masse_eau_a_evaporer = Mp / (1 + x0) * (x0 - xf)
    Q2 = (1/dT) * (1/cp) * Masse_eau_a_evaporer * Lk/ts
    return Q2


# pour trouver delta T #
d = 1
while Q1(d) < Q2(d):
    d += 1
if Q1(d) >= Q2(d):
    print ("La différence des températures entre l'air entrant et l'air sortant est de ", d, " degrés.")


print("La pression de saturation à la température de l'air sortant est ",  Psat(Ts-d), ' Pa')
print("L'humidité de l'air saturé en eau à la température de l'air sortant est de ", Ysat(Ts-d), " kg eau/ kg air sec.")
print("Le débit minimal d'air à fournir par le ventilateur est de ", Q1(d), " mètres cubes par seconde d'air sec "
                                                                            "à 65°C")
print("La valeur donnée par la fonction Q2 donne une valeur approchée car nous n'avons considéré que les naturels. "
      "La deuxième fonction donne un débit d'air de ", Q2(d), " mètres cube par seconde d'air sec à 65°C.")