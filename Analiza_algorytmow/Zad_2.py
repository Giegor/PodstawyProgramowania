T = [-1, 3, 5, 7, 8, 9, 13, 33, 37, 40, 43]
n = len(T) - 1
x = 7
ile_p = 0
ile_k = 0
ile_w = 0
def F(T, x):
    global ile_p, ile_k, ile_w
    p = 1
    k = n
    while p < k:
        s = (p + k) // 2
        if T[s] == x:
            return True
        else:
            if T[s] < x:
                ile_p += 1
                p = s + 1
            else:
                ile_k += 1
                k = s - 1
    return False

#Zadanie 2.1.

F(T, x)

print(ile_p, ile_k)

#Zadanie 2.2.
#T = list(range(1, 101))
T = [x for x in range(1, 101)]
print(T)
x = 101
n = len(T) - 1

ile_w = 0

F(T, x)

print(ile_w)