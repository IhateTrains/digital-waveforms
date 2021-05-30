import matplotlib.pyplot as plt
import numpy as np


def my_lines(ax, pos, *args, **kwargs):
    if ax == 'x':
        for p in pos:
            plt.axvline(p, *args, **kwargs)
    else:
        for p in pos:
            plt.axhline(p, *args, **kwargs)

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

def plot1(bity, napiecia, poziom):
    dlugosc = len(bity) + 2
    t = dlugosc/len(napiecia) * np.arange(len(napiecia))
    #t = len(napiecia)
    my_lines('x', range(dlugosc), color='.5', linewidth=1, linestyle='--')
    my_lines('y', [(-3*poziom),0,(3*poziom)], color='.5', linewidth=1, linestyle='--')
    plt.step(t, napiecia, 'r', linewidth=2, where='post')
    plt.ylim([(-3*poziom)-1,(3*poziom)+1])
    plt.xlim(0, dlugosc)

    for tbit, bit in enumerate(bity):
        plt.text(tbit + 0.5, poziom + 0.5, str(bit))

    plt.show()