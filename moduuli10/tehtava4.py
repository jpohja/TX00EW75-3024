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

class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            nopeuden_muutos = random.randint(-10, 15)
            auto.kiihdyta(nopeuden_muutos)
            auto.kulje(1)

    def tulosta_tilanne(self):
        print("-" * 70)
        print(f"{'Rekisteritunnus':<20}{'Huippunopeus':<18}{'Tämänhetkinen nopeus':<25}{'Kuljettu matka':<20}.")
        print("-" * 70)
        for auto in autot:
            print(
                f"{auto.rekisteritunnus:<20}{auto.huippunopeus:<20}{auto.tamanhetkinen_nopeus:<20}{auto.kuljettu_matka:<20}")

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kuljettu_matka >= 10000:
                return True
        return False

autot = []
tunnit = 0

for i in range(10):
    huippunopeus = random.randint(100, 200)
    rekisteritunnus = f"ABC-{i+1}"
    autot.append(Auto(rekisteritunnus, huippunopeus))

kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

while True:
    kilpailu.tunti_kuluu()
    tunnit += 1
    if tunnit % 10 == 0:
        kilpailu.tulosta_tilanne()
    elif kilpailu.kilpailu_ohi():
        print("-" * 70)
        print("Final scores:")
        kilpailu.tulosta_tilanne()
    if kilpailu.kilpailu_ohi():
        break





