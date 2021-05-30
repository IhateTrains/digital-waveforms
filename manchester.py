from plot import plot
import numpy as np
from helpers import split, srednia_wartosc_sygnalu

def manchester(bity, niski, wysoki):
    data = np.repeat(bity, 2)
    clock = 1 - np.arange(len(data)) % 2
    logical = np.invert(np.logical_xor(clock, data))
    output = []
    for i in range(len(logical)):
        if logical[i]:
            output.append(wysoki)
        else:
            output.append(niski)
    return output


def plot_manchester(ciag):    
    bity = split(ciag)
    niski = float(input('Podaj poziom niski: '))
    wysoki = float(input('Podaj poziom wysoki: '))
    output = manchester(bity, niski, wysoki)

    wart_srednia = srednia_wartosc_sygnalu(output)
    print('Srednia wartosc sygnalu:', wart_srednia)
    plot(bity, output, niski, wysoki)
