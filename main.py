from menu import __menu__
from Plano import __plano__, numeros
from MergeSort import __merge_sort__

opc = 10

while opc !=0:
    print('-----------------Practica de Ordenamientos-----------------')
    print(f'1.- MergeSort\n2.- SelectionSort\n0.- Salir')
    opc = int(input('Elige ordenamiento a realzar: '))
    __menu__(opc)




