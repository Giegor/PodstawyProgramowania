#Pęla while - przykłady

'''liczba = 120
licznik = 0

#W pętli while podajemy warunek TRWANIA pętli
while liczba > 0: #tak długo jak liczba jest dodatnia, pętla się wykonuje
    liczba //= 2
    licznik += 1

print(licznik)'''

#Zadanie 1.
'''x = input('Podaj liczbę lub q aby zakończyć, przegrywie życiowy, matka cię nie kocha, a twój stary wolał iść po mleko niż ciebie znać (:\nProszę napisz tutaj liczbę misiaczku: ')
licznik = 0
while x != 'q':
    liczba = int(x)
    if liczba < 2:
        licznik = licznik + 1
    x = input('Podaj liczbę lub q aby zakończyć, przegrywie życiowy, matka cię nie kocha, a twój stary wolał iść po mleko niż ciebie znać (:\nProszę napisz tutaj liczbę misiaczku: ')
print(licznik)'''


#Zadanie 2.
'''popr_haslo = 'informatyka'
haslo = input('Podaj haslo')
proby = 1

while haslo != popr_haslo and proby <= 5:
    print('Naucz się pisać człowieku')
    haslo = input('Podaj haslo')
    proby += 1

if haslo == popr_haslo:
    print('Witaj w systemie mały nic nie znaczący człowieczku (:')

else:
    print('Lecz się na pamięć patafianie zaniedbany!!!!!, Nie wejdziesz tu (: (: (: naura!')'''


#Zadanie 6.
'''import random
import time
wynik1 = 0
wynik2 = 0
akcja = 0

while not ((wynik1 >= 21 or wynik2 >= 21) and abs(wynik1 - wynik2) >= 2): #abs(x) = |x|
    akcja += 1
    print(f'Akcja {akcja}')
    #syfek = int(input('Podaj numer wygranej drużyny'))
    syfek = random.randint(1, 2)
    if syfek == 1:
        wynik1 += 1
    if syfek == 2:
        wynik2 += 1
    print(f'Wynik {wynik1} : {wynik2}')
    time.sleep(1)

if wynik1 > wynik2:
    print('Wygrała drużyna 1')
else:
    print('Wygrała drużyna 2')'''



'''liczba = int(input('Podaj liczbę'))

while liczba > 0:
    cyfra = liczba % 10
    liczba //= 10
    print(cyfra, end = '')
'''


liczba = int(input('Co się lapmisz parówo dęta?! Ludzika z delmy nie widziałeś? A nie czekaj... Podaj liczbę: '))
d = 2
ile_czyn = 0
ile_r_czyn = 0

while liczba > 1:
    if liczba % d == 0:
        ile_r_czyn += 1
    while liczba % d == 0:
        liczba //= d
        ile_czyn += 1
    d += 1
print(ile_czyn)
print(ile_r_czyn)