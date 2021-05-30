# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np


def my_lines(ax, pos, *args, **kwargs):
    if ax == 'x':
        for p in pos:
            plt.axvline(p, *args, **kwargs)
    else:
        for p in pos:
            plt.axhline(p, *args, **kwargs)


def split(word):
    return [int(char) for char in word]

def plot(bity, napiecia, niski, wysoki):
    dlugosc = len(bity)
    t = dlugosc/len(napiecia) * np.arange(len(napiecia))
    my_lines('x', range(dlugosc), color='.5', linewidth=1, linestyle='--')
    my_lines('y', [niski, 0, wysoki], color='.5', linewidth=1, linestyle='--')
    plt.step(t, napiecia, 'r', linewidth=2, where='post')
    plt.ylim([niski-1, wysoki+1])
    plt.xlim(0, dlugosc)

    for tbit, bit in enumerate(bity):
        plt.text(tbit + 0.5, wysoki + 0.5, str(bit))

    plt.show()


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


ciag = input('Podaj ciag bitow: ').strip().replace(' ', '')

to_exit = False

while not to_exit:
    print('')
    print('Podaj kod')
    print('1 - NKB NRZ')
    print('2 - NKB RZ')
    print('3 - AMI')
    print('4 - Manchester')
    print('5 - roznicowy Manchester')
    print('6 - 2B1Q')
    print('0 - wyjdz')

    wybor = input()
    if wybor == '1':
        plot_NRZ(ciag)
    elif wybor == '2':
        pass
    elif wybor == '3':
        pass
    elif wybor == '4':
        plot_manchester(ciag)
    elif wybor == '5':
        pass
    elif wybor == '6':
        pass
    elif wybor == '0':
        to_exit = True
    else:
        pass
