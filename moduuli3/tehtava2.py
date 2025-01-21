hyttiluokka = input("Hyttiluokka: ")
hyttiluokka_pienella = hyttiluokka.lower()

if hyttiluokka_pienella == "lux":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif hyttiluokka_pienella == "a":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif hyttiluokka_pienella == "b":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif hyttiluokka_pienella == "c":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka.")
