def muunnin_litroiksi(bensa):
    return bensa * 3.785

gallonat = float(input("Anna gallonamäärä: "))

while gallonat >= 0:
    print(f"{gallonat} gallonaa on {muunnin_litroiksi(gallonat):.2f} litraa.")
    gallonat = float(input("Anna gallonamäärä: "))

print("Ohjelma päättynyt.")


