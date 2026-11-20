import time
import winsound
from Plano import __plano__, numeros


def __merge_sort__(numeros):

    print("\033[2J\033[H", end="")
    __plano__(numeros)

    def ordenar(inicio, fin):

        if inicio >= fin:
            return

        m = (inicio + fin) // 2

        ordenar(inicio, m)
        ordenar(m + 1, fin)

        a = numeros[inicio:m + 1]
        b = numeros[m + 1:fin + 1]

        i = 0
        j = 0
        k = inicio

        while i < len(a) and j < len(b):

            if a[i] < b[j]:
                numeros[k] = a[i]
                i += 1
            else:
                numeros[k] = b[j]
                j += 1

            print("\033[H", end="")
            __plano__(numeros)
            time.sleep(0.2)

            k += 1

        while i < len(a):
            numeros[k] = a[i]
            i += 1

            frecuencia = 200 + (numeros[k] * 50)
            winsound.Beep(frecuencia, 100)

            print("\033[H", end="")
            __plano__(numeros)
            time.sleep(0.2)

            k += 1

        while j < len(b):
            numeros[k] = b[j]
            j += 1

            frecuencia = 200 + (i * 100)
            winsound.Beep(frecuencia, 100)

            print("\033[H", end="")
            __plano__(numeros)
            time.sleep(0.2)

            k += 1

    ordenar(0, len(numeros) - 1)

    return numeros
