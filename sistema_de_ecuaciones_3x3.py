from fractions import Fraction
#no uso Fraction porque muestra número muy grandes en las fracciones
#si quieres usarlo, solo agregalo en x,y, z

def run():
    def llenado():
        m = int(input("Ingrese el numero de filas de la matriz: "))
        print("_______________________________________________")
        n = int(input("Ingrese el numero de columnas de la matriz: "))
        print("_______________________________________________")
        a=[]
        for i in range(m):
            f=[]
            for j in range(n):
                f.append(float(input(f'Ingrese el elemento {(i+1,j+1)}:')))
                print("_______________________________________________")
            a.append(f)   
        return a

    def determinante(matriz):
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

    print("""Resolver el sistema de ecuaciones de 3x3:
    a11X1 + a12X2 + a13X3 = C1
    a21X2 + a22X2 + a23X2 = C2
    a31X3 + a32X3 + a33X3 = C3""")
    print("_______________________________________________")


    print("Ingrese la matriz de coeficientes (a11, a12, a13, a21 ...): ")
    print("_______________________________________________") 
    delta = llenado()
    det_delta = determinante(delta)

    print("Ingrese la matriz para la incógnita 1 (x): ")
    print("_______________________________________________")
    delta_x = llenado()
    det_delta_x = determinante(delta_x)

    print("Ingrese la matriz para la incógnita 2 (y) : ")
    print("_______________________________________________")
    delta_y = llenado()
    det_delta_y = determinante(delta_y)
    
    print("Ingrese la matriz para la incógnita 3 (z) : ")
    print("_______________________________________________")
    delta_z = llenado()
    det_delta_z = determinante(delta_z)

    x = det_delta_x / det_delta
    y = det_delta_y / det_delta
    z = det_delta_z / det_delta

    print(f'X es igual a {x}; Y es igual a {y}; Z es igual a {z}')

if __name__ == '__main__':
    run()