import random

heitot = []

def nopanheitto():
    luku = random.randint(1, 6)
    heitot.append(luku)
    return luku

nopan_tulos = 0

while nopan_tulos != 6:
    nopan_tulos = nopanheitto()
    print(nopan_tulos)





