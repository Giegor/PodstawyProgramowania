def p2dec(p, n, liczba):
    w = 0
    pot = 1

    for i in range(n, 0, -1):
        w = w + liczba[i] * pot
        pot = pot * p
    return w

#print(p2dec(10, 5, [0, 1, 0, 0, 1, 1]))

#gotowiec
'''liczba = '10011'
print(int(liczba, 2))'''

p2dec(8, 5, [0, 2, 3, 1, 6, 5])