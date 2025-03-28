class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nyt_kerroksessa = alin_kerros
        print(f"Hissi lähtee kerroksesta: {self.nyt_kerroksessa}")

    def siirry_kerrokseen(self, kerros):
        while self.nyt_kerroksessa != kerros:
            if self.nyt_kerroksessa < kerros:
                self.kerros_ylos()
            elif self.nyt_kerroksessa > kerros:
                self.kerros_alas()

    def kerros_ylos(self):
        self.nyt_kerroksessa += 1
        print(self.nyt_kerroksessa)

    def kerros_alas(self):
        self.nyt_kerroksessa -= 1
        print(self.nyt_kerroksessa)

h = Hissi(-2, 4)
h.siirry_kerrokseen(3)
h.siirry_kerrokseen(h.alin_kerros)

print(" ")
print(f"Hissi on nyt kerroksessa: {h.nyt_kerroksessa}")
