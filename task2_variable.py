def calcule_avec_puissance(somme, puissance):
    return somme ** puissance
iterations = int(input("le nombre d'iteration souhaiter : "))
puissance = int(input("le nombre de puissance : "))
resultat_puissance = calcule_avec_puissance(iterations, puissance)
print(resultat_puissance)
