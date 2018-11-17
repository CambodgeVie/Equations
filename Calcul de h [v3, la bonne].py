"""

Calcul du coefficient de transfert de chaleur h

Auteur : groupe n°1

Date : 9 novembre 2018

Mise en équations des dimensions du séchoir solaire, sous forme de
fonctions afin de déterminer h

Entrée : viscosités dynamique et cinématique, constante g de gravitation,
diffusivité thermique de l'air, longueur et épaisseur de la paroi, différence
de température entre l'intérieur et les parois, conductivité thermique de
l'air , débit d'air, largeur du séchoir

Sortie : la valeur du coefficient h


"""
T = float(input('Température souhaitée au sein du séchoir: ', ))
g = 9.81                                                                     # Accélération de la gravité
deltaT = float(input('Différence entre les températures des parois: ', ))
L = float(input('Longueur caractéristique: ', ))
vc = float(input("Viscosité cinématique: ", ))                                # Viscosité cinématique du fluide (m/s²)
vd = float(input("Viscosité dynamique: ", ))                                  # Viscosité dynamique du fluide
alpha = float(input("Diffusivité thermique: ", ))                             # Diffusivité thermique d'un fluide
ep = float(input("Epaisseur de la paroi: ", ))                                # Épaisseur de la paroi (m)
H = float(input("Hauteur du dispositif: ", ))                                 # Hauteur entre les deux plaques //
long = float(input("Longueur: ", ))                                           # Largeur du séchoir
l = float(input("Conductivité thermique: ', "))                               # Conductivité thermique du fluide
Q = float(input("Débit d'air entrant: ", ))                                   # Débit d'air (minimal ici)
x = float(input('Coefficient relatif à Nu, à definir: , '))                   # À déterminer

def beta(T):                                        # Expression de beta en fonction de la
                                                    # température au sein du séchoir, détaillée
                                                    # dans le rapport
    return 1/T

def grashof(g, T, deltaT, L, vc):                   # Nombre de Grashof
    g = 9.81                                        # m/s² constante de gravitation
    pi_1 = beta(T)*deltaT
    pi_2 = g* (L**3)/(vc)**2
    gr = pi_1 * pi_2                                # Expression du nombre de Grashof
    return gr

def reynlolds(Q, H, long, L, vc):                   # Nombre de Reynolds en fonction de la vitesse
                                                    # du fluide, de l'épaisseur de la paroi, et de
                                                    # la viscosité cinématique
    U =  Q/H*long
    re_L = U*L/vc                                   # Expression du nombre de Reynolds
    return re_L

def convection(g, T, deltaT, L, vc, Q, H, long):    # Détermination du cas de convection
    gr = grashof(g, T, deltaT, L, vc)
    re_L = reynlolds(Q, H, long, L, vc)
    ratio = gr/re_L**2                              # Expression du ratio

    if ratio > 1:                                   # Evaluation de notre cas
        return("Nous sommes ici dans le cas d'une convection naturelle")

    elif ratio < 1:
        return("Nous sommes ici dans le cas d'une convection forcée")

    elif ratio == 1:
        return("Il y a une convection naturelle et forcée sans domination, donc une convection mixte")

def prandtl(vc, alpha):                             # Nombre de Prandtl en fonction de la viscosité cinématique de la
                                                    # diffusivité thermique du fluide
    pr = vc/alpha
    return pr


def rayleigh(vc, alpha, g, T, deltaT, L):           # Nombre de Rayleigh en fonction des nombres de Prandlt et Grashof
    gr = grashof(g, T, deltaT, L, vc)
    pr = vc / alpha
    ray = gr * pr
    return ray



def nu(vc, alpha, g, T, deltaT, L, x):              # Définition du nombre de Nusselt
    ray = rayleigh(vc, alpha, g, T, deltaT, L)
    nusselt = x*ray^(1/4)                           # Expression du nombre de Nusselt
    return nusselt

def coeffh(vd, vc, beta, g, alpha, L, H, deltaT, l, Q, long, x):
    ray = rayleigh(vc, alpha, g, T, deltaT, L)
    h = nu(ray, x) * l/L                           # Expression de h en fonction du nombre
                                                    # de Nusselt, de la longueur caractéristique
                                                    # et de la conductivité thermique de l'air
    return h

print('La valeur du coefficient de transfert de chaleur pour la variation de température de', deltaT,' K est de ',
      coeffh(vd, vc, beta, g, alpha, L, H, deltaT, l, Q, long, x), 'Watts par Kelvins par mètre carré de surface')
