#Forum a verifier
def calcul_somme(n):
    total = 0
    for i in range(n):
        total += int('1' * (i + 1))
    return total

def calcule_avec_puissance(somme, puissance):
    return somme ** puissance


iterations = int(input("le nombre d'iteration souhaiter : "))

resultat_somme = calcul_somme(iterations)

puissance = int(input("le nombre de puissance : "))

resultat_puissance = calcule_avec_puissance(resultat_somme, puissance)

print(resultat_puissance)
