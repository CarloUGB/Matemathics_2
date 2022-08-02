# import numpy as np

def llenado():
    m = int(input("Ingrese el numero de filas de la matriz: "))
    n = int(input("Ingrese el numero de columnas de la matriz: "))

    A=[]
    for i in range(m):
        f=[]
        for j in range(n):
            f.append(float(input(f'Ingrese el elemento {(i+1,j+1)}:')))
        A.append(f)
    
    return A

def mul_matriz(A, B):
    C=[]
    for i in range(len(A)):
        f=[]
        for j in range(len(B[0])):
            cont=0
            for k in range(len(B)):
                cont=cont+A[i][k]*B[k][j]
            f.append(cont)
        C.append(f)

    return C

def suma(A, B):
    C=[]
    for i in range(len(A)):
        f=[]
        for j in range(len(A[0])):
            cont=0
            cont=cont+A[i][j]+B[i][j]
            f.append(cont)
        C.append(f)
    return C

def imprimir(A):
    for i in range(len(A)):
        print(A[i])


print("LLENADO DE LA MATRIZ A\n\n")
A=llenado()
print("LLENADO DE LA MATRIZ B\n\n")
B=llenado()

if len(A[0]) == len(B):
    C = mul_matriz(A, B)
    print(f'\n\nEl resultado de la multiplicación es: \n')
    imprimir(C)
else:
    print("LAS MATRICES NO PUEDEN MULTIPLICARSE")

if len(A) == len(B) & len(A[0]) == len(B[0]):
    print(f'\n\n El resultado de la suma es: \n')
    imprimir(suma(A,B))
else: 
    print("Las matrices no se pueden sumar")

"""a = np.array(A)
b = np.array(B)

c = np.dot(a ,b)
print(f'La multiplicación es: \n\n{c}')
"""