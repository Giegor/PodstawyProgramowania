def f(x):
    return 2 * (x + 3) * (x - 2) * (x - 6) * (x - 7)

#3.3.
przedzial = [-3.00, -2.99, -2.98, -2.97]

def czy_rosnaca_w_przedziale(przedzial):
    for i in range(1, len(przedzial)):
        x2 = przedzial[i]
        x1 = przedzial[i - 1]
        if f(x2) <= f(x1):
            return False
        return True