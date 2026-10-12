#algorytm łopatologiczny
def czy_pierwsza(n):
    dzielniki = 0
    for i in range(1, n + 1):
        if n % i == 0: #czy liczba jest podzielna przez i
            dzielniki += 1
    #Jeśli są dokłądnie dwa dzielniki to liczba n jest pierwsza
    if dzielniki == 2:
        return True
    else:
        return False

def czy_pierwsza2(n):
    if n == 1:
        return False
    else:
        for d in range(2, int(n ** 0.5) + 1):
            if n % d == 0:
                return False
        return True