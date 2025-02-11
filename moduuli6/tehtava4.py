def lukujen_summa(luvut):
    summa = 0
    for luku in luvut:
        summa += luku
    return summa

luvut = [1, 5, 6, 11, 6, 9]

summa = lukujen_summa(luvut)

print(f"Summa on {summa}.")