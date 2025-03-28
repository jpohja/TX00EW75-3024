import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, nopeuden_muutos):
        self.tamanhetkinen_nopeus += nopeuden_muutos
        if self.tamanhetkinen_nopeus < 0:
            self.tamanhetkinen_nopeus = 0
        elif self.tamanhetkinen_nopeus > self.huippunopeus:
            self.tamanhetkinen_nopeus = self.huippunopeus


    def kulje(self, tunnit):
        self.kuljettu_matka = self.kuljettu_matka + tunnit * self.tamanhetkinen_nopeus

autot = []

kisa_paattynyt = False

tunnit = 0

voittaja = None

for i in range(10):
    huippunopeus = random.randint(100, 200)
    rekisteritunnus = f"ABC-{i+1}"
    autot.append(Auto(rekisteritunnus, huippunopeus))

#kisa

while not kisa_paattynyt:
    tunnit += 1
    for auto in autot:
        nopeuden_muutos = random.randint(-10, 15)
        auto.kiihdyta(nopeuden_muutos)
        auto.kulje(1)
        if auto.kuljettu_matka >= 10000:
            kisa_paattynyt = True
            voittaja = auto
            break

print(f"Kisa päättyi {tunnit} tunnin jälkeen.")
print(f"{'Rekisteritunnus':<20}{'Huippunopeus':<18}{'Tämänhetkinen nopeus':<25}{'Kuljettu matka':<20}.")
print("-"*70)

for auto in autot:
    print(f"{auto.rekisteritunnus:<20}{auto.huippunopeus:<20}{auto.tamanhetkinen_nopeus:<20}{auto.kuljettu_matka:<20}")
