yritykset = 5

while yritykset > 0:
    yritykset -= 1
    kayttis = input("Anna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")
    if kayttis == "python" and salasana == "rules":
        print("Tervetuloa")
        break
else:
    print("Pääsy evätty")


