vuosiluku = int(input("Anna vuosiluku: "))

if (vuosiluku % 4 == 0 and vuosiluku % 100 != 0) or (vuosiluku % 400 == 0):
    print("Karkausvuosi")
else:
    print("Ei ole karkausvuosi")