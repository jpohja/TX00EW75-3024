class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nyt_kerroksessa = alin_kerros

    def siirry_kerrokseen(self, kerros):
        print(f"Hissi lähtee kerroksesta: {self.nyt_kerroksessa}")
        while self.nyt_kerroksessa != kerros:
            if self.nyt_kerroksessa < kerros:
                self.kerros_ylos()
            elif self.nyt_kerroksessa > kerros:
                self.kerros_alas()
        print(f"Hissi on kerroksessa: {self.nyt_kerroksessa}")

    def kerros_ylos(self):
        self.nyt_kerroksessa += 1
        print(self.nyt_kerroksessa)

    def kerros_alas(self):
        self.nyt_kerroksessa -= 1
        print(self.nyt_kerroksessa)

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_maara):
        self.hissit = []
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        for i in range(hissien_maara):
            self.hissit.append(Hissi(alin_kerros, ylin_kerros))


    def aja_hissia(self, hissin_num, kerros):
        (self
         .hissit[hissin_num]
         .siirry_kerrokseen(kerros))

    def palohalytys(self):
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(self.alin_kerros)

talo = Talo(-2, 8, 3)
talo.aja_hissia(1, 4)
talo.palohalytys()
