from plot import plot
from helpers import split


def plot_NRZ(ciag):
    bity = split(ciag)

    niski = float(input('Podaj poziom niski: '))
    wysoki = float(input('Podaj poziom wysoki: '))

    NRZ = []
    for bit in bity:
        if int(bit) == 1:
            NRZ.append(wysoki)
        else:
            NRZ.append(niski)

    wart_srednia = sum(NRZ)/len(NRZ)
    print('Srednia wartosc sygnalu:', wart_srednia)
    plot(bity, NRZ, niski, wysoki)


def plot_RZ(ciag):
    bity = split(ciag)

    niski = float(input('Podaj poziom niski: '))
    wysoki = float(input('Podaj poziom wysoki: '))

    RZ = []
    for bit in bity:
        if int(bit) == 1:

            RZ.append(wysoki)
            RZ.append(0)

        else:

            RZ.append(niski)
            RZ.append(0)

    wart_srednia = sum(RZ)/len(RZ)
    print('Srednia wartosc sygnalu:', wart_srednia)
    plot(bity, RZ, niski, wysoki)