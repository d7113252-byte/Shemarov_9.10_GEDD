skaitli = [5, 2, 8, 1, 4]
n = len(skaitli)
print(f"Sākums: {skaitli}\n")
for i in range(n - 1):
    samainits = False  
    for j in range(n - 1 - i):
        if skaitli[j] > skaitli[j + 1]:
            skaitli[j], skaitli[j + 1] = skaitli[j + 1], skaitli[j]
            samainits = True  
    print(f"Pēc {i + 1}. gājiena: {skaitli}")
    if not samainits:
        print("Saraksts sakārtots pirms laika, cikls tiek pārtraukts.")
        break
print(f"\nGala rezultāts: {skaitli}")