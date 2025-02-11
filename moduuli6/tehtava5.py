luvut = [2, 4, 8, 6, 1, 9, 4, 4, 5]
uusi_lista = []

def poista_parittomat(lista):
    for luku in lista:
        if luku % 2 == 0:
            uusi_lista.append(luku)
    return uusi_lista

print(luvut)
print(poista_parittomat(luvut))