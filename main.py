from NKB import plot_NRZ, plot_RZ
from AMI import plot_AMI
from encoding_2B1Q import plot_2B1Q
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
        plot_RZ(ciag)
    elif wybor == '3':
        plot_AMI(ciag)
    elif wybor == '4':
        plot_manchester(ciag, differential=False)
    elif wybor == '5':
        plot_manchester(ciag, differential=True)
    elif wybor == '6':
        plot_2B1Q(ciag)
    elif wybor == '0':
        to_exit = True
    else:
        pass
