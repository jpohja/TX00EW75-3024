nimet = set()
anna_nimi = input("Anna nimi: ")

while anna_nimi != "":
        if anna_nimi in nimet:
            print("Aiemmin syötetty nimi")
        else:
            print("Uusi nimi")
        nimet.add(anna_nimi)
        anna_nimi = input("Anna nimi: ")
else:
    print(nimet)