# lista = [10, 56, 89, 59]

#1. Chdzenie bezpośrednio po elementach listy
#Do zmiennej b trafiają bezpośredio elementy listy, tzn. 10, 56, 89, 59
# '''for b in lista:
#     print(b)'''

#2. Chodzenie po liście z użyciem indeksów
#2.1. Co to jest indeks?
# lista[2]
# 2 - indeks
# lista[2] - elementznajdujący się pod indeksem 2 = 89

#2.2.
# '''for k in range(4): #range(0, 4)
#     print(lista[k])'''
#
# for k in range(len(lista)):
#     print(lista[k])


lista = [7]

'''for i in lista:
    liczba = float(input('Podaj liczbę patafianie'))
    print(liczba)
    if liczba != 0:
        lista.append(11)'''

for i in lista:
    print(i)
    lista.append(i + 1)