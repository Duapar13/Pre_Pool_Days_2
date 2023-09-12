number = 123434565
digit_sum = 0

while number > 0:
    digit_sum += number % 10
    number //= 10

print("Somme des nombres :", digit_sum)