class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjailija, sivumaara):
        super().__init__(nimi)
        self.kirjailija = kirjailija
        self.sivumaara = sivumaara
    def tulosta_tiedot(self):
        print(f"{self.nimi}, {self.kirjailija}, {self.sivumaara} sivua.")

class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        super().__init__(nimi)
        self.paatoimittaja = paatoimittaja
    def tulosta_tiedot(self):
        print(f"{self.nimi}, {self.paatoimittaja}.")

julkaisut = []
julkaisut.append(Kirja("Hytti n:o 6", "Rosa Liksom", 200))
julkaisut.append(Lehti("Aku Ankka", "Aki Hyyppä"))

for j in julkaisut:
    j.tulosta_tiedot()