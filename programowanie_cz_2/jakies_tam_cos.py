class CzlowiekRozumny:
    l_ludzi = 0
    def __init__(self, plec, imie, nazwisko, wiek):
        self.plec = plec
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        CzlowiekRozumny.l_ludzi += 1
    def postarz_sie(self, o_ile):
        self.wiek += o_ile
    def zmien_imie(self, nowe_imie):
        self.imie = nowe_imie
    def pokaz_info(self):
        print(self.plec, self.imie, self.nazwisko, self.wiek)

czlowiek1 = CzlowiekRozumny('k', 'Zofia', 'Bajka', 30)
czlowiek2 = CzlowiekRozumny('k', 'Zofia', 'Bajka', 30)
czlowiek3 = CzlowiekRozumny('k', 'Zofia', 'Bajka', 30)
print(CzlowiekRozumny.l_ludzi)
print(czlowiek1.imie, czlowiek1.nazwisko, czlowiek1.wiek)
czlowiek1.pokaz_info()
czlowiek1.postarz_sie(10)
czlowiek1.pokaz_info()