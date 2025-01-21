sukupuoli = input("Ilmoita sukupuolesi (nainen/mies): ")
hemoglobiiniarvo = int(input("Ilmoita hemoglobiiniarvosi: "))

if sukupuoli == "nainen" and hemoglobiiniarvo >= 117 and hemoglobiiniarvo <= 175:
    print("Hemoglobiini on normaali.")
elif sukupuoli == "nainen" and hemoglobiiniarvo < 117:
    print("Hemoglobiini on alhainen.")
elif sukupuoli == "nainen" and hemoglobiiniarvo > 175:
    print("Hemoglobiini on korkea.")
elif sukupuoli == "mies" and hemoglobiiniarvo >= 134 and hemoglobiiniarvo <= 195:
    print("Hemoglobiini on normaali.")
elif sukupuoli == "mies" and hemoglobiiniarvo < 134:
    print("Hemoglobiini on alhainen.")
elif sukupuoli == "mies" and hemoglobiiniarvo > 195:
    print("Hemoglobiini on korkea.")