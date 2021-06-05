from plot import plot
from helpers import split, split_into_chars, srednia_wartosc_sygnalu
from manchester_coding.manchester import Manchester



def manchester(bity, niski, wysoki, differential=False):
    logical = split(Manchester(differential).encode(bity))
    print(logical)
    output = []
    for i in range(len(logical)):
        if logical[i]:
            output.append(wysoki)
        else:
            output.append(niski)
    return output


def plot_manchester(ciag, differential=False):    
    bity = split_into_chars(ciag)
    niski = float(input('Podaj poziom niski: '))
    wysoki = float(input('Podaj poziom wysoki: '))
    output = manchester(bity, niski, wysoki, differential)

    wart_srednia = srednia_wartosc_sygnalu(output)
    print('Srednia wartosc sygnalu:', wart_srednia)
    plot(bity, output, niski, wysoki)