

kokonaisluku = int(input("Anna kokonaisluku: "))


if kokonaisluku > 1:
    for i in range(2, kokonaisluku//2 + 1):
        if kokonaisluku % i == 0:
            print(f"{kokonaisluku} ei ole alkuluku.")
            break
    else:
        print(f"{kokonaisluku} on alkuluku.")

else:
    print(f"{kokonaisluku} ei ole alkuluku.")





    

