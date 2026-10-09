
skaitli = [4, 7, 2, 9, 7, 1]
try:
    meklejamais = int(input("Ievadi meklējamo skaitli: "))
    atrasts_indekss = -1
    for i in range(len(skaitli)):
        if skaitli[i] == meklejamais:
            atrasts_indekss = i + 1
            break
    if atrasts_indekss != -1:
        print(f"Pirmais indekss, kurā skaitlis atrasts: {atrasts_indekss}")
    else:
        print("Nav atrasts")
except ValueError:
    print("Kļūda: Ievadītā vērtība nav derīgs vesels skaitlis!")