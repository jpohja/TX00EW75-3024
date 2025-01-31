import random

pisteiden_maara = int(input("Anna pisteiden määrä: "))
pisteet_ympyrassa = 0
kerrat = 0

while kerrat < pisteiden_maara:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    kerrat += 1
    if x**2 + y**2 < 1:
        pisteet_ympyrassa += 1

pi_likiarvo = 4 * pisteet_ympyrassa / pisteiden_maara

print(pi_likiarvo)
