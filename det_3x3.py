def llenado():
    m = int(input("Ingrese el numero de filas de la matriz: "))
    n = int(input("Ingrese el numero de columnas de la matriz: "))

    A=[]
    for i in range(m):
        f=[]
        for j in range(n):
            f.append(int(input(f'Ingrese el elemento {(i+1,j+1)}:')))
        A.append(f)
    
    return A

def determinate():
    pass


print("ingrese la matriz de 3x4: ")
print(llenado())
