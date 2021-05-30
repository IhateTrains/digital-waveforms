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