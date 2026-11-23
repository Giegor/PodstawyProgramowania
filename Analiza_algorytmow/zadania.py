plik = open('dane_ulamki.txt')
dane = plik.readlines()

for i in range(len(dane)):
    dane[i] = [int(dane[i].split()[0]), int(dane[i].split()[1])]

#Zadanie 1.
min_licznik = 1
min_mianownik = 1
for u in dane:
    licznik = u[0]
    mianownik = u[1]
    if licznik * min_mianownik < mianownik * min_licznik:
        min_licznik = licznik
        min_mianownik = mianownik
    elif licznik * min_mianownik == mianownik * min_licznik:
        if mianownik < min_mianownik:+
            min_licznik = licznik
            min_mianownik = mianownik

print(min_licznik, min_mianownik)
