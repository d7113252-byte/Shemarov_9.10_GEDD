try:
    skaits = int(input("Cik skaitļus vēlies ievadīt? "))
    if skaits <= 0:
        print("Kļūda: Skaitļu skaitam jābūt lielākam par 0!")
    else:
        summa = 0
        pozitivi = 0
        negativi = 0
        nulle = 0
        para = 0
        nepara = 0
        for i in range(skaits):
            skaitlis = int(input(f"Ievadi {i + 1}. veselo skaitli: "))
            summa += skaitlis
            if skaitlis > 0:
                pozitivi += 1
            elif skaitlis < 0:
                negativi += 1
            else:
                nulle += 1
            if skaitlis % 2 == 0:
                para += 1
            else:
                nepara += 1
        videjais = summa / skaits
        print(f"Ievadīto skaitļu summa: {summa}")
        print(f"Vidējais aritmētiskais: {videjais:.2f}")
        print(f"Pozitīvo skaitļu skaits: {pozitivi}")
        print(f"Negatīvo skaitļu skaits: {negativi}")
        print(f"Nuļļu skaits: {nulle}")
        print(f"Pāra skaitļu skaits: {para}")
        print(f"Nepāra skaitļu skaits: {nepara}")
except ValueError:
    print("Kļūda: Ievadītā vērtība nav derīgs vesels skaitlis!")