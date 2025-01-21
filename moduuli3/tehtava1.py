kuha = int(input("Kuhan pituus senttimetreinä:\n"))

alimitta = 37 - kuha

if kuha < 37:
    print(f"Laske kuha takaisin järveen. Alimmasta sallitusta pyyntimitasta puuttuu {alimitta} senttiä.")
