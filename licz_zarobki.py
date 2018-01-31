studenci = {
    'Alicja': {'wiek': 21, 'kierunek': 'informatyka', 'ocena': 4},
    'Kasia': {'wiek': 23, 'kierunek': 'ekonomia', 'ocena': 4},
    'Gosia': {'wiek': 23, 'kierunek': 'finanse', 'ocena': 3},
    'Tomek': {'wiek': 25, 'ocena': 2}
}


def licz_srednia_zarobkow(*args):
    suma = 0
    for kwota in args:
        suma += kwota
    return suma / len(args)


def licz_mediane_zarobkow(*args):
    if not args:
        return None
    posortowane = sorted(args)
    ilosc_zarobkow = len(posortowane)

    mediana = None
    if ilosc_zarobkow % 2:
        polowa = ilosc_zarobkow // 2
        mediana = posortowane[polowa]
    else:
        polowa = len(posortowane) // 2
        mediana = (posortowane[polowa] + posortowane[polowa-1]) / 2
    return mediana


def licz_mediane(*args):
    posortowane = sorted(args)
    ilosc_ocen = len(posortowane)

    mediana = None
    if ilosc_ocen % 2:
        polowa = ilosc_ocen // 2
        mediana = posortowane[polowa]
    else:
        polowa = len(posortowane) // 2
        mediana = (posortowane[polowa] + posortowane[polowa - 1]) / 2
    return mediana


def licz_mediane_ocen(**kwargs):
    if not kwargs:
        return None
    oceny = [element['ocena'] for element in kwargs.values()]
    return licz_mediane(*oceny)


def licz_srednia_ocen(**kwargs):
    suma = 0
    for element in kwargs.values():
        suma += element['ocena']
    return suma / len(kwargs)


def studenci_bez_kierunku(**kwargs):
    bez_kierunku = []
    for klucz, wartosc in kwargs.items():
        if not wartosc.get('kierunek'):
            bez_kierunku.append(klucz)
    return bez_kierunku


def raport_studentow(**kwargs):
    print("studenci bez kierunku: " + str(studenci_bez_kierunku(**kwargs)))
    print("srednia ocen: " + str(licz_srednia_ocen(**kwargs)))
    print("mediana ocen: " + str(licz_mediane_ocen(**kwargs)))


raport_studentow(**studenci)
# print(studenci_bez_kierunku(**studenci))