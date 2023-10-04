#LIFO andmestruktuur

taldrikud = ["taldrik_must", "taldrik_valge", "taldrik_sinine", "taldrik_punane"]

tegevus = int(input("Sisesta vastav number1 - Lisa taldrik hunikkusse\n2 - Võta taldrik hunnikust ära\n"))

if tegevus == 1:
    varv = str(input("Mis värvi taldrik on?: "))
    taldrikud.append("taldrik_" + varv)
    print(taldrikud)

elif tegevus == 2:
    taldrikud.pop()
    print(taldrikud)
