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


def plot_manchester(ciag):
    niski = float(input('Podaj poziom niski: '))
    wysoki = float(input('Podaj poziom wysoki: '))

    data = np.repeat(bity, 2)
    clock = 1 - np.arange(len(data)) % 2

    logical = np.invert(np.logical_xor(clock, data))
    manchester = []
    for i in range(len(logical)):
        if logical[i]:
            manchester.append(wysoki)
        else:
            manchester.append(niski)

    wart_srednia = sum(manchester) / 2
    print('Srednia wartosc sygnalu:', wart_srednia)

    t = 0.5 * np.arange(len(data))

    my_lines('x', range(len(ciag)), color='.5', linewidth=1, linestyle='-')
    my_lines('y', [niski, 0, wysoki], color='.5', linewidth=1, linestyle='-')
    plt.step(t, manchester, 'r', linewidth=2, where='post')
    plt.ylim([niski-1, wysoki+1])
    plt.xlim(0, len(ciag))

    for tbit, bit in enumerate(bity):
        plt.text(tbit + 0.5, wysoki + 0.5, str(bit))

    plt.show()


ciag = input('Podaj ciag bitow: ').strip().replace(' ', '')
bity = split(ciag)

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
        pass
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
