from plot import plot, plot1
from helpers import split


def plot_2B1Q(ciag):

    bity = ciag
    level = float(input('Podaj poziom (Jeżeli nie wiesz/nie masz podane wpisz 1): '))

    napiecia = []

    flag = False
    a = ""
    b1q = []
    temp = []
    b = 0
    for bit in bity:
        a += bit
        b += 1
        if b == 2:
            b = 0
            b1q.append(a)
            a = ""

    for i in range(0,len(b1q)):
        if b1q[i] == '00':
            napiecia.append((-3*level))
            ostatni = -3*level
        elif b1q[i] == '01':
            napiecia.append((-1*level))
            ostatni = -1*level
        elif b1q[i] == '10':
            napiecia.append((3*level))
            ostatni = 3*level
        elif b1q[i] == '11':
            napiecia.append((1*level))
            ostatni = 1*level


    napiecia.append(ostatni)
    
    wart_srednia = sum(napiecia)/len(napiecia)
    print('Srednia wartosc sygnalu:', wart_srednia)

    plot1(bity,napiecia,level)


