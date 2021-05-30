from plot import plot
import numpy as np
from helpers import split


def plot_manchester(ciag):
    bity = split(ciag)
    data = np.repeat(bity, 2)
    clock = 1 - np.arange(len(data)) % 2

    niski = float(input('Podaj poziom niski: '))
    wysoki = float(input('Podaj poziom wysoki: '))

    logical = np.invert(np.logical_xor(clock, data))
    manchester = []
    for i in range(len(logical)):
        if logical[i]:
            manchester.append(wysoki)
        else:
            manchester.append(niski)

    wart_srednia = sum(manchester) / 2
    print('Srednia wartosc sygnalu:', wart_srednia)
    plot(bity, manchester, niski, wysoki)