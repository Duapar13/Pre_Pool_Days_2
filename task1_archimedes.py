incr = 1
pi = 0
i = 0
while i < 1000000:
    pi += ((-1) ** i)/(2 * i + 1)
    i += 1
pi *= 4
print(f"{pi:.6f}")