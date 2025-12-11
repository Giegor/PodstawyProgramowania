'''n = int(input('Podaj liczbę'))

iloczyn = 1

for x in range(n):
    iloczyn = iloczyn * (x + 1)

    print(iloczyn)'''


'''lista = [4, 12, 8, 1, 5, 6, 3]
kamien = 0

for x in lista:
    for y in lista:
        if x != y and (x + y) % 3 == 0:
            kamien += 1
print(kamien)'''

#Zadanie 3.
n = int(input('Podaj ile będzie napisów'))
max_napis = ''
for x in range(n):
    napis = input('Podaj napis')
    ile_a = napis.count('a')
    max_ile_a = napis.count('a')
    if ile_a > max_ile_a:
        max_napis = napis
print(max_napis)