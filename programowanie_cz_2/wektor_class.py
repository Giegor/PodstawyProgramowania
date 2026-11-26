class Wektor:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    '''def __str__(self):
        return f'[{self.x}, {self.y}, {self.z}]'''

    def __str__(self):
        return str(list(vars(self).values()))

    def __add__(self, other):
        return Wektor(self.x + other.x, self.y + other.y, self.z + other.z)

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y and self.z == other.z:
            return True
        else:
            return False

w1 = Wektor(2, 4, 7)
w2 = Wektor(-3, 9, 1)
'''w3 = w1 + w2
print(w1 + w2)'''

print(w1 == w2)