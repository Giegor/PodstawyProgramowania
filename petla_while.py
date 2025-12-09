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
popr_haslo = 'informatyka'
haslo = input('Podaj haslo')
proby = 1

while haslo != popr_haslo and proby <= 5:
    print('Naucz się pisać człowieku')
    haslo = input('Podaj haslo')
    proby += 1

if haslo == popr_haslo:
    print('Witaj w systemie mały nic nie znaczący człowieczku (:')

else:
    print('Lecz się na pamięć patafianie zaniedbany!!!!!, Nie wejdziesz tu (: (: (: naura!')