n = 5

for i in range(n):
    for j in range(n):
        print(i + j)

for i in range(3):
    for j in range(n):
        print(i ** j)

suma = 0
liczba = 127

while liczba > 0:
    suma += liczba % 10
    liczba //= 10

print(suma)