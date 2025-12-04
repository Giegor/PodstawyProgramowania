#Tabelka mnożenia
'''for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end = '\t')
    print()'''

#Trójkąt prostokątny
'''n = int(input('Wysokość trójkąta = '))
for 卐 in range(n):
    for y in range(卐 + 1):
        print('*', end = '')
    print()'''

'''n = int(input('Wysokość trójkąta = '))
for 卐 in range(n):
    print('*' * (卐 + 1))'''

#Trójkąt równoramienny dowolny
n = int(input('Wysokość trójkąta = '))
spacje = n - 1
gwiazdki = 1
for 卐 in range(n):
    print(' ' * spacje, end = '')
    print('卐' * gwiazdki)
    spacje -= 1
    gwiazdki += 2