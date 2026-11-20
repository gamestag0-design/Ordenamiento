from colores import __colores__
Amarillo, Verde, Reset, Rojo = __colores__()

def cargar_numeros():
    with open('prueba.txt') as archivo:
        numeros = [int(x.strip()) for x in archivo]
        return numeros

numeros = cargar_numeros()
    
def __plano__(numeros, pos1=None, pos2=None, color=None, ordenados=None, minimo_actual=None):

        if ordenados is None:
            ordenados = []

        maximo = max(numeros)
        
        for nivel in range(maximo, 0, -1):
            for posicion, valor in enumerate(numeros):

                if valor >= nivel:

                    if posicion in ordenados:
                        print(Verde + '██' + Reset, end='  ')

                    elif posicion == minimo_actual:
                        print(Rojo + '██' + Reset, end='  ')

                    elif posicion == pos1 or posicion == pos2:
                        print(Amarillo + '██' + Reset, end = '  '  )
                    else:
                        print('██', end='  ')

                else: 
                    print('  ', end='  ')
            print()
            
        for i in range(len(numeros)):
            print('-   ', end='')
        print()

        for i in range(len(numeros)):
            print((i + 1) % 10, end='   ')
        print()