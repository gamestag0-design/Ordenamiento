import time
import os
from menu import __menu__
from Plano import __plano__, numeros
from MergeSort import __merge_sort__


print('-----------------Elige ordenamiento a realizar-----------------')
print(f'1.- MergeSort\n0.- Salir')
opc = int(input('Elige ordenamiento a realzar: '))

__menu__(opc)

