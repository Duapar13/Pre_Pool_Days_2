def calculate_pi(nombre):
    pi = 0
    for i in range(nombre):
        if i % 2 == 0:
            pi += 4 / (2 * i + 1)
        else:
            pi -= 4 / (2 * i + 1)
    return pi
pireduit = calculate_pi(6)
print("Pi : ", round(pireduit, 6))
