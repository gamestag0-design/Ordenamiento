import sys
from SelectionSort import __selection_sort__
from MergeSort import __merge_sort__
from Plano import __plano__ , cargar_numeros


def __menu__(opc):
    if opc == 1:
        numeros = cargar_numeros()
        print()
        print('----------Ordenamiento MergeSort----------')
        __merge_sort__(numeros)

    if opc == 2:
        numeros = cargar_numeros()
        print()
        print('----------Ordenamiento SelectionSort----------')
        __selection_sort__(numeros)
    
    if opc == 0:
        print('Programa terminado')
        sys.exit()
