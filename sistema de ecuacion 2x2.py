from fractions import Fraction

def determinante(A):
    return A[0][0]*A[1][1]-A[0][1]*A[1][0]


print(""" Resolver el sistema de ecuaciones de 2x2\n\na11X1+a12X2=C1\n a21X1+a22X2=C2""")
A=[]
for i in range(2):
    f=[]
    for j in range(3):
        if j == 2:
            f.append(int(input(f'Ingresa el coeficiente c{i+1}: ')))
        else:
            f.append(int(input(f'Ingresa el coeficiente a{i+1}{j+1}: ')))
    A.append(f)

if A[0][0]*A[1][1]-A[0][1]*A[1][0] == 0:
    print("El sistema de ecuaciones no tiene solución o bien tiene infinitas soluciones")
else:
     x= (Fraction(A[0][2]*A[1][1]-A[0][1]*A[1][2],A[0][0]*A[1][1]-A[0][1]*A[1][0]))
     y = (Fraction(A[0][0]*A[1][2]-A[0][2]*A[1][0],A[0][0]*A[1][1]-A[0][1]*A[1][0]))
for i in range(2):
    print(A[i])
print(f'El valor de x es {x} y el valor de y es {y}')

