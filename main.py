from NKB import plot_NRZ
from manchester import plot_manchester


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
