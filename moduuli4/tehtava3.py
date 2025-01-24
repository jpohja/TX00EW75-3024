luku = input("Anna luku: ")
luvut = []
while luku != "":
    luvut.append(luku)
    luvut = [int(item) for item in luvut]
    luku = input("Anna luku: ")

print(f"Pienin syötetty luku on: {min(luvut)}")
print(f"Suurin syötetty luku on: {max(luvut)}")