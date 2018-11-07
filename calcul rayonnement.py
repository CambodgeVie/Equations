sigma = 5.67*10**(-8)
n = int(input("Nombre de rayonnement à calculer: "))
for i in range(n):
    x = input("Flux: ")
    T = float(input("T: "))
    F = sigma*T**4
    print("Rayonnement",x ,": ",F)
