
vecums = int(input("Cik Tev ir gadi?"))
if vecums <=0:
    print("Lūdzu, ievadi derīgu vecumu.")
elif vecums < 10:
    print("Tu esi bērns.")
elif vecums < 18:
    print("Tu esi pusaudzis.")
elif vecums < 60:
    print("Tu esi pieaugušais.")
else:
    print("Tu esi seniors")