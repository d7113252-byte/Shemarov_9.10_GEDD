try:
    skaits = int(input("Cik skaitļus tu gribi ievadīt? "))
    if skaits <= 0:
        print("Kļūda! Skaitļu skaitam ir jābūt lielākam par 0.")
    else:
        for i in range(skaits):
            skaitlis = int(input(f"Ievadi {i + 1}. skaitli: "))
            if i == 0:
                mazakais = skaitlis
                lielakais = skaitlis
            else:
                if skaitlis < mazakais:
                    mazakais = skaitlis
                if skaitlis > lielakais:
                    lielakais = skaitlis
    print(f"Mazākais skaitlis: {mazakais}")
    print(f"Lielākais skaitlis: {lielakais}")
except ValueError:
    print("Kļūda: Ievadītā vērtība nav derīgs vesels skaitlis!")