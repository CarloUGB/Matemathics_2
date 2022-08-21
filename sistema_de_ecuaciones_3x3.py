def run():
    print("""Resolver el sistema de ecuaciones de 3x3:
    a11X1 + a12X2 + a13X3 = C1
    a21X2 + a22X2 + a23X2 = C2
    a31X3 + a32X3 + a33X3 = C3""")
    a=[]
    for i in range(3):
        f=[]
        for j in range(4):
            if j == 3:
                f.append(int(input(f'Ingresa el coeficiente c{i+1}: ')))
            else:
                f.append(int(input(f'Ingresa el coeficiente a{i+1}{j+1}: ')))
        a.append(f)

    print(a)

    for i in range(1):
        for j in range(3):
            pass

if __name__ == '__main__':
    run()