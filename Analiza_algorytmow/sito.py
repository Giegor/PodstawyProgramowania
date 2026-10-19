zakres = 100
SITO = [True] * (zakres + 1)
SITO[0] = False
SITO[1] = False
for i in range(2, len(SITO)):
    if SITO[i] == True:
        for j in range(2 * i, len(SITO), i):
            SITO[j] = False

#Jak sprawdzić, czy 20 jest liczbą pierwszą?
print(SITO[13])