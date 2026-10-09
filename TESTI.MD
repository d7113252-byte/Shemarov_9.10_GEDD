Algoritmu pamatu ĢEDD

1. uzdevums
Faila nosaukums: summa_lidz_n.py
Ievade: Vesels pozitīvs skaitlis n
Sagaidāmais rezultāts: Visu veselo skaitļu summa no 1 līdz n (ieskaitot n) vai kļūdas paziņojums nederīgas ievades gadījumā.
Algoritma darbība: Programma nolasa lietotāja ievadīto vērtību un ar try...except pārbauda, vai tā ir vesels skaitlis. Ja skaitlis ir lielāks par 0, programma ar for ciklu no 1 līdz n saskaita visus skaitļus un izvada rezultātu.

2. uzdevums

Solis| Nosacījums   | Mainīgie pirms         | Veiktā darbība                            | Mainīgie pēc           | Izvade ekrānā                      |
0    |—             | —                      |Sāku pildīt programmu                      | —                      | —                                  |
1    |—             | nav                    |Ievada 3, konvertē uz int                  | n = 3                  | "Ievadi veselu pozitīvu skaitli n:"|
2    |n<= 0(False)  | n = 3                  |Pārbauda nosacījumu, pāriet uz else zaru   | n = 3                  | —                                  |
3    |— n = 3       | n=3                    |Piešķir sākuma vērtību summa = 0           |n = 3, summa = 0        | —                                  |
4    |i = 1 (1 <= 3)| n = 3, summa = 0       |Izpilda ciklu: summa += 1                  | n = 3, summa = 1, i = 1| —                                  |
5    |i = 2 (2 <= 3)| n = 3, summa = 1, i = 1|Izpilda ciklu: summa += 2                  | n = 3, summa = 3, i = 2| —                                  |
6    |i = 3 (3 <= 3)| n = 3, summa = 3, i = 2|Izpilda ciklu: summa += 3                  | n = 3, summa = 6, i = 3| —                                  |
7    |i = 4 (4 > 3) |n = 3, summa = 6, i = 3 |Cikla nosacījums nav spēkā, iziet no cikla | n = 3, summa = 6       | —                                  |
8    |—             |n = 3, summa = 6        |Izvada gala paziņojumu ar aprēķināto summu | n = 3, summa = 6       | "Skaitļu summa no 1 līdz 3 ir 6."  |

3. uzdevums

Testa veids              |Ievade| Sagaidāmais rezultāts                              | Faktiskais rezultāts                               | Tests izturēts?|
Tipisks                  | 5    |Skaitļu summa no 1 līdz 5 ir 15.                    | Skaitļu summa no 1 līdz 5 ir 15.                   | Jā             |
Robežgadījums            | 1    |Skaitļu summa no 1 līdz 1 ir 1.                     | Skaitļu summa no 1 līdz 1 ir 1.                    | Jā             |
Tukša vai nederīga ievade| abc  | Kļūda: Ievadītā vērtība nav derīgs vesels skaitlis!| Kļūda: Ievadītā vērtība nav derīgs vesels skaitlis!| Jā             |
Papildu tests            | -4   | Kļūda: Skaitlim jābūt pozitīvam un lielākam par 0! | Kļūda: Skaitlim jābūt pozitīvam un lielākam par 0! | Jā             |

4. uzdevums 
Kura ievade radītu kļūdu bez pārbaudēm:
Ja programmā netiktu izmantots try...except bloks, ievadot tekstu (piemēram, "desmit") vai desmitdaļskaitli ("2.5"), Python izmestu ValueError kļūdu un programma beigtos. Savukārt, ja netiktu pārbaudīts if n <= 0, ievadot 0 vai negatīvu skaitli (piemēram, -5), cikls nemaz neizpildītos un izvadītu summu 0, kas matemātiski nav korekts rezultāts šim uzdevumam. 
Risinājums: Programmai ir pievienota pilna ievades validācija, kas pasargā no avārijām un nodrošina korektus ziņojumus lietotājam.   