import random

heitot = []

tahkot = int(input("Anna nopan maksimisilmäluku: "))

def nopanheitto(tahkot):
    luku = random.randint(1, tahkot)
    heitot.append(luku)
    return luku

nopan_tulos = 0

while nopan_tulos != 6:
    nopan_tulos = nopanheitto(tahkot)
    print(nopan_tulos)