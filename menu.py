import os
import time
import sys
from MergeSort import __merge_sort__
from Plano import numeros, __plano__


def __menu__(opc):
    if opc == 1:
        __merge_sort__(numeros)
    if opc == '0':
        print('Programa terminado')
        sys.exit()
