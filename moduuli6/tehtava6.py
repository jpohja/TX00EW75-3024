import math

def pizzan_neliohinta(halkaisija, hinta):
    sade = halkaisija / 2
    pinta_ala = math.pi * (sade ** 2)
    neliohinta = hinta / (pinta_ala / 1000)
    return neliohinta

pizza1 = float(input("Anna pizzan halkaisija (cm): "))
hinta1 = float(input("Anna pizzan hinta (€): "))
pizza2 = float(input("Anna toisen pizzan halkaisija (cm): "))
hinta2 = float(input("Anna toisen pizzan hinta (€): "))

pizza1_neliohinta = pizzan_neliohinta(pizza1, hinta1)
pizza2_neliohinta = pizzan_neliohinta(pizza2, hinta2)

print(f"pizza1_neliohinta = {pizza1_neliohinta: <.2f}")
print(f"pizza2_neliohinta = {pizza2_neliohinta: <.2f}")

if pizza1_neliohinta < pizza2_neliohinta:
    print(f"Pizza 1 antaa paremman vastineen rahalle.")
elif pizza1_neliohinta > pizza2_neliohinta:
    print(f"Pizza 2 antaa paremman vastineen rahalle.")
else:
    print("Pizzat ovat samanhintaiset.")
