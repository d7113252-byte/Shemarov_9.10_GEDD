try:
    n = int(input("Ievadi veselu pozitīvu skaitli: "))
    if n <= 0:
        print("Kļūda: Skaitlim jābūt pozitīvam un lielākam par 0")
    else:
        summa = 0
        for i in range(1, n + 1):
            summa += i
        print(f"Skaitļu summa no 1 līdz {n} ir {summa}.")
except ValueError:
    print("Kļūda: Ievadītā vērtība nav derīgs vesels skaitlis!")