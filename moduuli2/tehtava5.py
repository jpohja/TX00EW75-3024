leiviskat = float(input("Anna leiviskät.\n"))
naulat = float(input("Anna naulat.\n"))
luodit = float(input("Anna luodit.\n"))

luoti_grammaa = luodit * 13.3
naula_grammaa = naulat * 425.6
leiviska_grammaa = leiviskat * 8512

summa_grammaa = luoti_grammaa + naula_grammaa + leiviska_grammaa
kilogrammat = int(summa_grammaa // 1000)
grammat = round(summa_grammaa % 1000, 2)

print(f"Massa nykymittojen mukaan:\n{kilogrammat} kilogrammaa ja {grammat} grammaa.")