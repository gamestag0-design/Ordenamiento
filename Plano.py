with open('prueba.txt') as archivo:
    numeros = [int(x.strip()) for x in archivo]
    
def __plano__(numeros):

        maximo = max(numeros)
        
        for nivel in range(maximo, 0, -1):
            for valor in numeros:
                if valor >= nivel:
                    print('██', end='  ')
                else: 
                    print('  ', end='  ')
            print()
            
        for i in range(len(numeros)):
            print('-   ', end='')
        print()

        for i in range(len(numeros)):
            print(i + 1 % 10, end='   ')
        print()
                

    