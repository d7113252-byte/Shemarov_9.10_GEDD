parole = "1234567"
meginajumi = 3

while meginajumi > 0:
    ievadita_parole = input("Ievadi paroli: ")
    
    if ievadita_parole == parole:
        print("Piekļuve atļauta")
        break
    else:
        meginajumi -= 1
        if meginajumi > 0:
            print(f"Nepareiza parole! Atlikuši {meginajumi} mēģinājumi.")
        else:
            print("Piekļuve bloķēta")