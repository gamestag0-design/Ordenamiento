import time
import os
from Plano import __plano__,numeros

def __merge_sort__(numeros):
    if len(numeros) <= 1:
        return numeros
    m = len(numeros) // 2
    a = __merge_sort__(numeros[:m])
    b = __merge_sort__(numeros[m:])
    r = []
    while a and b:
        if a[0] < b[0]:
            r.append(a.pop(0))
        else:
            r.append(b.pop(0))
    os.system('cls')
    __plano__(r + a + b)
    time.sleep(0.5)
    
    return r + a + b


    