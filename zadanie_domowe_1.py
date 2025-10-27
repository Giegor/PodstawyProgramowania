'''wynik = int(input('Podaj zdobytą liczbę punktów: '))
punkty = int(input('Podaj maksymalną liczbę punktów: '))
ocena =  int(input('Podaj ocenę z języka: '))

if (wynik / punkty > 0.9) or (ocena >= 5):
    print('grupa zaawansowana')
else:
    print('grupa podstawowa')'''



a = float(input('Podaj liczbę a różną od 0: '))
b = float(input('Podaj liczbę b: '))
c = float(input('Podaj liczbę c: '))

if a == 0:
    print('Współczynnik powinien być różny od 0')

elif b == c == 0:
    print('𝑥0 = 0')

elif b == 0 and c != 0:
    if -(c / a) > 0:
        x1 = (-(c / a) ** 0.5)
        x2 = -(-(c / a) ** 0.5)
        print(f'x1 = {x1} v x2 = {x2}')
    elif -(c / a) < 0:
        print('Nie ma rozwiązań')

elif c == 0 and b != 0:
    x1 = 0
    x2 = -(b / a)
    print(f'x1 = {x1} v x2 = {x2}')

elif b != 0 and c != 0:
    delta = b ** 2 - 4 * a * c
    if delta > 0:
        x1 = (-b + delta ** 0.5) / (2 * a)
        x2 = (-b - delta ** 0.5) / (2 * a)
        print(f'x1 = {x1} v x2 = {x2}')
    elif delta == 0:
        x0 = (-b) / (2 * a)
    elif delta < 0:
        print('Nie ma rozwiązań')

else:
    print('Nie ma rozwiązań')