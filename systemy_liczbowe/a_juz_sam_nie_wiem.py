def dec2p(liczba, p):
    if liczba == 0:
        return [0]
    w = []
    while liczba > 0:
        w.append(liczba % p)
        liczba = liczba // p
    w.reverse()
    return w
print(dec2p(19, 2))