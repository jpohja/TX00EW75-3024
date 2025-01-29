import random

arpakuutiot = int(input("Anna arpakuutioden lukumäärä: "))

arvotut_luvut = []

for n in range(arpakuutiot):
    luku = random.randint(1, 6)
    arvotut_luvut.append(luku)

print(sum(arvotut_luvut))
