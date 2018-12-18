from math import log
from math import e

a = str(input("Labo ou Cambodge:"))
if a == "Labo":

 def Pression_saturante(T):
    M = 0.01802  # Kg/mol --> masse molaire de l'eau !!! en kg/mol pour rester cohérent au niveau des unités
    Lv = 2.2564 * (10 ** (6)) # J/kg --> chaleur latente de vaporisation de l'eau
    To = 373.15  # K --> temperature d'ébullition de l'eau
    R = 8.31447  # mol.K/(J) --> constante des gazs parfaits
    P = 101325

    i = ((M * Lv)/R ) * (1 / To - 1 / T)
    Psaturante = P * (e ** (i))
    return Psaturante

 def Pression_partielle(HR,Psa):
    Pv = (HR*Psa)/100
    return Pv

 def Trosee(Pv):
    to = 373.15 #en Kelvin
    Po = 101325 #en pascal
    M = 0.01802 #en kg/mol !!!
    Lv = 2.26 * (10 ** (6)) #en J/kg
    R = 8.31447
    a = ((1/to) - ((R / (M * Lv)) * log(Pv/Po) ))
    Tros = a ** (-1)
    return Tros # en kelvin


 Ps = Pression_saturante(294.25)
 print("Ps =",Ps)


 Pp = Pression_partielle(55,Ps)
 print("Pp =", Pp)


 print("Trosée en °C = ", Trosee(Pp) - 273.15)
 print ("Trosée en K = ", Trosee(Pp))

elif a == "Cambodge":

 def Pression_saturante(T, P):
    M = 0.01802  # Kg/mol --> masse molaire de l'eau !!! en kg/mol pour rester cohérent au niveau des unités
    Lv = 2.26 * (10 ** (6))  # J/kg --> chaleur latente de vaporisation de l'eau
    To = 373.15  # K --> temperature d'ébullition de l'eau
    R = 8.31447  # mol.K/(J) --> constante des gazs parfaits

    i = ((M * Lv) / R) * (1 / To - 1 / T)
    Psaturante = P * (e ** (i))
    return Psaturante


 def Pression_partielle(HR, Psa):
    Pv = (HR * Psa) / 100
    return Pv


 def Température_de_rosée(Pv):
    to = 373.15  # en Kelvin
    Po = 101325  # en pascal
    M = 0.01802  # en kg/mol !!!
    Lv = 2.2564 * (10 ** (6))  # en J/kg
    R = 8.31447
    a = ((1 / to) - ((R / (M * Lv)) * log(Pv / Po)))
    Tros = a ** (-1)
    return Tros  # en kelvin
 Ps = Pression_saturante(302.95,101325)
 print("Ps =",Ps)


 Pp = Pression_partielle(48.7,Ps)
 print("Pp =", Pp)


 print("Trosée en °C = ", Température_de_rosée(Pp) - 273.15)
 print ("Trosée en K = ", Température_de_rosée(Pp))