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

    def tulosta_tiedot(self):
        print(f"{'Rekisteritunnus':<20}{'Huippunopeus':<18}{'Tämänhetkinen nopeus':<25}{'Kuljettu matka':<20}.")
        print("-" * 70)
        for auto in autot:
            print(
                f"{auto.rekisteritunnus:<20}{auto.huippunopeus:<20}{auto.tamanhetkinen_nopeus:<20}{auto.kuljettu_matka:<20}")

class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Akkukapasiteetti: {self.akkukapasiteetti} kWh.")

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankki):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankki = bensatankki

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Bensatankin koko: {self.bensatankki} l.")

autot = []

sahkis = Sahkoauto("ABC-15", 180, 52.5)
polttis = Polttomoottoriauto("ACD-123", 165, 32.3)
autot.append(sahkis)
autot.append(polttis)

sahkis.tamanhetkinen_nopeus = 70
polttis.tamanhetkinen_nopeus = 80
sahkis.kulje(3)
polttis.kulje(3)

sahkis.tulosta_tiedot()
polttis.tulosta_tiedot()


