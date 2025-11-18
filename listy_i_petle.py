# #Jak nie programowaćwielokrotnie powtarzanych czynności
#
# '''a = float(input('Podaj liczbę patafianie'))
# b = float(input('Podaj liczbę patafianie'))
# c = float(input('Podaj liczbę patafianie'))
# d = float(input('Podaj liczbę patafianie'))
# e = float(input('Podaj liczbę patafianie'))
#
# suma = (a + b + c + d + e)
#
# print(suma)'''
#
# '''liczba = 0
# suma = 0
#
# for u in range(5):
#     liczba = float(input('Podaj liczbę'))
#     suma = suma + liczba
#
# print(suma)'''
#
# #1. Listy
# lista = ['qwerty', 56, [6, 7], 4.56, [[5,8], 1]]
# print(lista[2][1])
# print(lista[4][0][1])
# #2. Listy i pętle
# lista2 = ['kot', 'pies', 'owca', 'lama']
#
# #Pętla for:
# #-> wyciąga dane z listy (jedna po drugiej)
# #-> wykonuje siętyle razy ile elementów ma lista
# for z in lista2:
#     print(z)
#
# #Pętla która wykona się 3 razy
# lista3 = [1410, 15, 7]
#
# for i in lista3:
#     print('OK')
#
# #Pętla, która wykonuje się 1000 razy
# '''lista4 = [[0] * 10 for i in range(10)]
#
# for i in lista4:
#     print('Cześć')'''
# lista4 = [0] * 10
# for i in lista4:
#     print('Cześć')
#
# #3. Generatory i pętle
# przedzial = range(1, 10) #{1, 2, 3, 4, 5, 6, 7, 8, 9}
#
# for i in przedzial:
#     print(i)
#
# #Pętla, która wykona się 10 razy
# for i in range(10): #range(0,10), 10 - liczba powtórzeń
#     print(i)

'''lista5 = [0]
lista5.append(5)
print(lista5)'''

'''lista = [0]

for i in lista:
    print('ERROR 303!!!' * 18)
    lista.append(0)'''

#4. Pętla while

liczba = 5

while liczba > 0:
    print(liczba)
    liczba = liczba - 1
