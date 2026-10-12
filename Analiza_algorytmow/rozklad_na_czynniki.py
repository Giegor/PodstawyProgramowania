def rozklad(n):
    wynik = []
    d = 2
    while n > 1:
        while n % d == 0:
            n = n // d
            wynik.append(d)
        d += 1
    return wynik