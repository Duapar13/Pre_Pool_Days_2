import math

def calculer_pi():
    somme = 0
    n = 0

    while True:
        terme = ((-1) ** n) / ((2 * n) + 1)
        somme += terme
        n += 1

        if n >= 1000000:  
            break
    pi_estime = 4 * somme
    
    return round(pi_estime, 6)
pi_calculé = calculer_pi()
print(f"La valeur estimée de pi avec la formule donnée est : {pi_calculé}")