atlikums = 100
while True:
    print("1 - Atlikums | 2 - Iemaksāt | 3 - Izņemt | 4 - Iziet")
    izvele = input("Izvēlies darbību (1-4): ")
    if izvele == "1":
        print("Konta atlikums:", atlikums)
    elif izvele == "2":
        summa = int(input("Ievadi iemaksas summu: "))
        if summa > 0:
            atlikums += summa
            print("Atlikums:", atlikums)
        else:
            print("Summai jābūt lielākai par 0")
    elif izvele == "3":
        summa = int(input("Ievadi izņemšanas summu: "))
        if summa <= 0:
            print("Summai jābūt lielākai par 0!")
        elif summa > atlikums:
            print("Kļūda: Nepietiek līdzekļu!")
        else:
            atlikums -= summa
            print("Atlikums:", atlikums)
    elif izvele == "4":
        print("Darbs beigts.")
        break
    else:
        print("Nepareiza izvēle! Ievadi skaitli no 1 līdz 4.")