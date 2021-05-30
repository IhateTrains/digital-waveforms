from plot import plot
from helpers import split


def plot_AMI(ciag):

    bity = split(ciag)

    niski = float(input('Podaj poziom niski: '))
    wysoki = float(input('Podaj poziom wysoki: '))

    flag = False

    AMI = []
    for bit in bity:
        if int(bit) == 1 and flag is False:

            AMI.append(wysoki)
            flag = True

        elif int(bit) == 1 and flag is True:

            AMI.append(niski)
            flag = False

        else:
            AMI.append(0.0)

    bity.append(0)
    AMI.append(0.0)
    wart_srednia = sum(AMI)/len(AMI)
    print('Srednia wartosc sygnalu:', wart_srednia)
    plot(bity, AMI, niski, wysoki)