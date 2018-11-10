"""

Système d'équations du bloc effet de serre

Auteur : groupe n°1

Date : 9 novembre 2018

Détermine la puissance que la serre doit capter, la température des parois, ainsi que le rayonnement qu'elles émettent

Entrée: température souhaitée de l'air, les flux solaires direct et indirect, coefficient de transfert de chaleur h
Sortie: les températures des parois (2), leur rayonnement propre (2), la puissance à capter

"""

import numpy as np
import scipy.optimize as resol
import scipy.integrate as integr
import matplotlib.pyplot as plt


def rayonnement(temperature):                                           # Hypothèse du corps noir
    sigma = 5.67 * 10**(-8)                                             # Constante de Stefan-Boltzmann
    F = sigma*(temperature**4)                                          # Expression du rayonnement d'un corps noir en
                                                                        # fonction de sa température
    return F

def syst(T, Fd, Fi, h, inconnues):                                      # Ecrivons le système comme une fonction, avec
                                                                        # "inconnues" étant le quintuple
                                                                        # (P, Fs, Ts, Fp,Tp)

    eq1 = inconnues[0] - h*(inconnues[2] + inconnues[4] - 2 * T)        # La puissance à capter
    eq2 = Fd + Fi - inconnues[0] - inconnues[3]                         # Bilan global
    eq3 = Fd + inconnues[3] - inconnues[1] - h*(inconnues[2] - T)       # Bilan local sur le sol
    eq4 = inconnues[1] - rayonnement(inconnues[2])                      # Le sol est un corps noir
    eq5 = inconnues[3] - rayonnement(inconnues[4])                      # Le plastique est un corps noir

    return eq1, eq2, eq3, eq4, eq5

solution_du_systeme = resol.root(syst)
print(solution_du_systeme)