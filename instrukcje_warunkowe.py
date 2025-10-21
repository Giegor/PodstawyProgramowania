#Instrukcja warunkowa if

#Przykład 1
'''liczba = int(input('Podaj liczbę od 1 do 3'))

if liczba == 1:
    print('jeden')
if liczba == 2:
    print('dwa')
if liczba == 3:
    print('trzy')'''

#Przykład 2

'''liczba = int(input('Podaj liczbę od 1 do 3'))

if liczba == 1:
    print('jeden')
elif liczba == 2:
    print('dwa')
elif liczba == 3:
    print('trzy')'''

#Przykaład 3 - może być użyty tylko if
'''liczba = int(input('Podaj liczbę całkowitą dodatnią'))

if liczba % 2 == 0:
    print('parzysta')
if liczba % 3 == 0:
    print('podzielna przez 3')
if liczba > 0:
    print('dodatnia')'''

#Przykład 4
liczba = int(input('Podaj liczbę od 1 do 3'))

if liczba == 1:
    print('jeden')
elif liczba == 2:
    print('dwa')
elif liczba == 3:
    print('trzy')
else:
    print('Umiesz czytać imbecylu?!\nNapisz to poprawnie, proszę cię człowieku.')