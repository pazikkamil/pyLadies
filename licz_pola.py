def licz_pole_prostokata(a, b):
    return a * b


def rysuj_prostokat(a, b, element='#'):
    wiersz=a*element
    for i in range(b):
        print(wiersz)

prostokat1 = licz_pole_prostokata(2, 3)
# print(prostokat1)

rysuj_prostokat(7, 4, '*')

wynik_rysowania = rysuj_prostokat(7, 4)
print(wynik_rysowania)