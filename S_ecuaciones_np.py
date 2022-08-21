import numpy as np
from fractions import Fraction

def run ():
    
    def fill():
        n = int(input('Ingrese el número de ecuaciones (filas):'))
        m = int(input('Ingrese el número de incógnitas/soluciones (columnas): '))
        
        list=[]
        print('Ingrese los números: ')
        for i in range(n):
            for j in range(m):
                num = int(input(f'Número {i+1},{j+1}: '))
                list.append(num)
        array = np.array(list)
        array = array.reshape(n,m)
        #Le da la forma deseada a la matriz
        return array

    print('Ingrese la matriz de coeficientes del sistema de ecuaciones: ')
    coeficientes = fill()

    print('Ingrese la matriz de soluciones del sistema de ecuaciones: ')
    soluciones = fill()

    incógnitas = np.linalg.solve(coeficientes, soluciones)
    print(incógnitas)
    incógnitas = incógnitas.ravel().flatten().tolist()
    for i in range(len(incógnitas)):
        if i == 0:
            print('X es igual a:', Fraction(incógnitas[i]))
        elif i == 1:
            print('Y es igual a:', Fraction(incógnitas[i]))
        elif i == 2:
            print('Z es igual a:', Fraction(incógnitas[i]))
        

if __name__ == '__main__':
    run()