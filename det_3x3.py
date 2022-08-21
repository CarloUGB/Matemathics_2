from contextlib import nullcontext


def llenado(m,n):
    a=[]
    for i in range(m):
        f=[]
        for j in range(n):
            f.append(int(input(f'Ingrese el elemento {(i+1,j+1)}:')))
        a.append(f)
    
    return a#Retorna la matriz de 3 x 3

def matriz_cofactores(entrada,delta):
    menor = []

    cofactor = "nada"

    return cofactor #Retorna el cofactor de cada entrada

m = int(input("Ingrese el numero de filas de la matriz: "))#3 filas
n = int(input("Ingrese el numero de columnas de la matriz: "))#3 columnas

delta = llenado(m,n) #Llama la función y les manda como paramentros las filas y las colummnas
                     #La matriz de 3 x 3 se almacena en delta. Delta es una matriz de 3 x 3

b= []#Crea una matriz de cofactores

for i in range (len(delta)):# Por cada elemento en la fila m, en un rango del número de elementos de delta
    d= []#Crea una lista de cofactores
    for j in range(len(delta[i])):#y en la columna n, y en un rango del número de elementos de cada elemento de delta
        entrada = delta[i][j]#Almacena cada entrada de delta
        c = matriz_cofactores(entrada,delta)#llama a la función de cofactores, cuyo parametro es la matriz delta y cada entrada de la misma
                                            #Y almacena cada cofactor en la variable c
    d.append(c)#agrega cada cofactor a la lista d
b.append(d)#Agrega cada lista de cofactores como un elemento, a la lisa b, formando una matriz de cofactores.

print("ingrese la matriz de 3x3: ")
print(delta)
