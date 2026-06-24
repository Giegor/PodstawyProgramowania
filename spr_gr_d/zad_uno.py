plik = open('dane.txt')
dane = plik.read().strip()

#1.2.
lista_liczb = []
for i in range(1, len(dane) -1):
    if dane[i].isdigit() and not dane[i - 1].isdigit():
        start = i
    elif dane[i].isdigit() and not dane[i +1].isdigit():
        stop = i
        lista_liczb.append(int(dane[start:stop+1]))
print(max(lista_liczb) ** 2)