"""

Système d'équations du bloc effet de serre

Auteur : groupe n°1

Date : 9 novembre 2018

Détermine la puissance que la serre doit capter, la température des parois, ainsi que le rayonnement qu'elles émettent

Entrée: température souhaitée de l'air, les flux solaires direct et indirect, coefficient de transfert de chaleur h
Sortie: les températures des parois (2), leur rayonnement propre (2), la puissance à capter

"""

from numpy import *
from scipy.optimize import *
import matplotlib.pyplot as plt

T = float(input('Température souhaitée au sein du séchoir: ', ))
Fd = float(input('Valeur du flux direct: ', ))
Fi = float(input('Valeur du flux indirect: ', ))
h = float(input('Valeur du coefficient de transfert de chaleur: ', ))


def rayonnement(temperature):                                           # Hypothèse du corps noir
    sigma = 5.67 * 10**(-8)                                             # Constante de Stefan-Boltzmann
    F = sigma*(temperature**4)                                          # Expression du rayonnement d'un corps noir en
                                                                        # fonction de sa température
    return F

def syst(inconnues):                                                    # Ecrivons le système comme une fonction, avec
                                                                        # "inconnues" étant le quintuple
                                                                        # (P, Fs, Ts, Fp,Tp)

    eq = empty((5))

    eq[0] = inconnues[0] - h*(inconnues[2] + inconnues[4] - 2 * T)        # La puissance à capter
    eq[1] = Fd + Fi - inconnues[0] - inconnues[3]                         # Bilan global
    eq[2] = Fd + inconnues[3] - inconnues[1] - h*(inconnues[2] - T)       # Bilan local sur le sol
    eq[3] = inconnues[1] - rayonnement(inconnues[2])                      # Le sol est un corps noir
    eq[4] = inconnues[3] - rayonnement(inconnues[4])                      # Le plastique est un corps noir

    return eq

solution_du_systeme = array([1, 1, 1, 1, 1])
sol = fsolve(syst, solution_du_systeme)
print('La puissance à capter est de ', sol[0], ' Watt par mètre carré de surface\n',
      'Le flux émis par le sol est de ', sol[1], ' Watt par mètre carré\n'
      , 'La température atteinte par le sol est de ', sol[2], ' K\n'
      , 'Le flux émis par la paroi en plastique est de ', sol[3], ' W/m^2 \n',
      'La température atteinte par la paroi en plastique est de ', sol[4], ' K')