from fractions import Fraction

def run():
    def llenado():
        m = int(input("Ingrese el numero de filas de la matriz: "))
        n = int(input("Ingrese el numero de columnas de la matriz: "))
        a=[]
        for i in range(m):
            f=[]
            for j in range(n):
                f.append(float(input(f'Ingrese el elemento {(i+1,j+1)}:')))
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

    print("Ingrese la matriz de incógnitas (a11, a12, a13, a21 ...): ")
    delta = llenado()
    det_delta = determinante(delta)

    print("Ingrese la matriz para la incógnita 1 (x): ")
    delta_x = llenado()
    det_delta_x = determinante(delta_x)

    print("Ingrese la matriz para la incógnita 2 (y) : ")
    delta_y = llenado()
    det_delta_y = determinante(delta_y)
    
    print("Ingrese la matriz para la incógnita 3 (z) : ")
    delta_z = llenado()
    det_delta_z = determinante(delta_z)

    x = Fraction(det_delta_x / det_delta)
    y = Fraction(det_delta_y / det_delta)
    z = Fraction(det_delta_z / det_delta)

    print(f'X es igual a {x}; Y es igual a {y}; Z es igual a {z}')

if __name__ == '__main__':
    run()