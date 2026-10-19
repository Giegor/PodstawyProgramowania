def NWD1(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a - b
        else:
            b = b - a
    if a > 0:
        return a
    else:
        return b

def NWD2(a, b):
    if a >0:
        return a
    else:
        return b

def NWW(a, b):
    return a * b // NWD2(a, b)

print(NWW(12, 18))