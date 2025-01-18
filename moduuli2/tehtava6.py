import random

kolmen_koodi = []
n = 3
for i in range(n):
    kolmen_koodi.append(str(random.randint(0, 9)))
kolmen_koodi = int(''.join(kolmen_koodi))
print(kolmen_koodi)

neljan_koodi = []
n = 4
for i in range(n):
    neljan_koodi.append(str(random.randint(1, 6)))
neljan_koodi = int(''.join(neljan_koodi))
print(neljan_koodi)