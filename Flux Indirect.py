def Flux_Indirect(Tr):
    Fi = sigma * (Tr)**4
    return Fi
sigma = 5.67*10**(-8)
b = str(input("Labo ou Cambodge:"))
if b == "Labo":
    print("Flux Indirect = ",Flux_Indirect(284.0485210168791))
elif b == "Cambodge":
    print("Flux Indirect = ",Flux_Indirect(290.04286228445363))




