"""

Système d'équations du bloc effet de serre

Auteur : groupe n°1

Date : 9 novembre 2018

Détermine la puissance que la serre doit capter, la température des parois, ainsi que le rayonnement qu'elles émettent

Entrée: température souhaitée de l'air, les flux solaires direct et indirect
Sortie: les températures des parois (2), leur rayonnement propre (2), la puissance à capter

"""

import numpy as np
import scipy.optimize as resol
import scipy.integrate as integr



def rayonnement(temperature):                   # Hypothèse du corps noir
    sigma = 5.67 * 10**(-8)                     # Constante de Stefan-Boltzmann
    F = sigma*(temperature**4)                  # Expression du rayonnement d'un corps noir en fonction
                                                # de sa température
