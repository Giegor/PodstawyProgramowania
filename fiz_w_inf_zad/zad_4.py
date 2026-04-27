dane = open('sily.txt').readlines()
for i in range(len(dane)):
    dane[i] = dane[i].split()
    dane[i] = [float(dane[i][0]), float(dane[i][1])]
print(dane)

