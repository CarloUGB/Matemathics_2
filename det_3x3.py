import numpy as np

def fill():
    n = int(input('Ingrese el número de filas:'))
    m = int(input('Ingrese el número de columnas: '))
        
    list=[]
    print('Ingrese los elementos de la matriz: ')
    for i in range(n):
        for j in range(m):
            num = int(input(f'Elemento {i+1},{j+1}: '))
            list.append(num)
    array = np.array(list)
    array = array.reshape(n,m)
    #Le da la forma deseada a la matriz
    return array

def determinante():
    acum = 0
    x = 0

    for i in range(len(matriz)):
        if i == 0:
            acum = acum + matriz[x][i] * ((matriz[1][1] * matriz[2][2]) - (matriz[2][1] * matriz[1][2]))
        elif i == 1:
            acum = acum + (-matriz[x][i]) * ((matriz[1][0] * matriz[2][2]) - (matriz[2][0] * matriz[1][2]))
        elif i == 2:
            acum = acum + matriz[x][i] * ((matriz[1][0]* matriz[2][1]) - (matriz[2][0] * matriz[1][1]))
    return acum

print("ingrese la matriz de 3x3: ")
matriz = fill()
print(matriz)
print ("El determinante de la matriz es: ", determinante())
