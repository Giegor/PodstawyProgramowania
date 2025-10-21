#Symbole logiczne

#Koniunkcja
print(2 == 3 and 3 > 1)

#Alternatywa
login = 'qwerty'
haslo = 'uiop'
print(login == 'admin' or haslo == 'uiop')

#Zaprzecznie
print(not(login == 'admin' or haslo == 'uiop'))

#Alternatywa wykluczająca
fryzjer = True
murarz = False

print(fryzjer == True ^ murarz == True)

#Priorytety operatorów logicznych
print(2 == 3 and 3 > 1 or 2 < 6)

#Operatory standardowe
print(2 + 3)
print(2 - 3)
print(2 * 3)
print(2 / 5)

#Potęgowanie
print(2 ** 5)

#Pierwiastkowanie
print(36 ** 0.5)
print(125 ** (1/3))

#Dzielenie całkowite (div) - dzielimy i zaokrąglamy zawsze w dół do liczby całkowitej
print(12 // 5)

#Reszta z dzielenia liczby a przez liczbę b
print(12 % 5)