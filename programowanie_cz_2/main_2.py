class Galeria:
    def __init__(self, kraj, miasto, lokale):
        self.kraj = kraj
        self.miasto = miasto
        self.lokale = lokale
'''galeria1 = Galeria('PL', 'Gdańsk', [(10, 8), (2, 10), (8, 6)])
galeria2 = Galeria('PL', 'Warszawa', [(10, 8), (2, 10), (8, 6)])
galeria3 = Galeria('PL', 'Kraków', [(10, 8), (2, 10), (8, 6)])

print(galeria1.miasto)
print(galeria1.lokale)
print(galeria1.lokale[1][0])'''

plik = open('galerie.txt')
dane = plik.readlines()

galerie = []

for x in dane:
    w = x.split()
    kraj = w[0]
    miasto = w[1]
    lokale = []
    for i in range(2, len(w), 2):
        dlugosc = int(w[i])
        szerokosc = int(w[i+1])
        lokale.append((dlugosc, szerokosc))
    galeria = Galeria(kraj, miasto, lokale)
    galerie.append(galeria)
print(galerie[0].lokale[1][1])