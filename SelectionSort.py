import time
import winsound
from colores import __colores__
from Plano import __plano__,numeros

Amarillo, Verde, Reset, Rojo = __colores__()


def __selection_sort__(numeros):

    ordenados = []

    print("\033[2J\033[H", end="")
    __plano__(numeros, ordenados=ordenados)

    minimo = range(0, len(numeros) -1)
    for i in minimo:
        minimo = i 

        for j in range(i + 1, len(numeros)):

            print("\033[2J\033[H", end="")
            __plano__(numeros, minimo, j, Amarillo, ordenados, minimo)
            time.sleep(0.20)

            if numeros[j] < numeros[minimo]:    
                minimo = j

            print("\033[2J\033[H", end="")
            __plano__(numeros, minimo, j, Verde, ordenados)
            time.sleep(0.20)

        if minimo != i:
            numeros[minimo], numeros[i] = numeros[i], numeros[minimo]
        
        ordenados.append(i)


        frecuencia = 200 + (i * 100)
        winsound.Beep(frecuencia, 100)

    print("\033[H", end="")
    __plano__(numeros, ordenados=ordenados)
    time.sleep(0.2)

    return numeros

