#Esta es una función principal, no es necesaria para este ejercicio
#pero aprendí que es una buena práctica
def run():
    import numpy as np

    def fill():
        n = int(input('Ingrese el número de filas:'))
        m = int(input('Ingrese el número de columnas: '))
        print('Ingrese los elementos de la matriz, de izquierda a derecha en orden descendente: ')
        list=[]
        for i in range(n*m):
            num = float(input(f'Elemento {i+1}: '))
            list.append(num)
        array = np.array(list)
        array = array.reshape(n,m)
        return array

    print('Ingrese la matriz mensaje:\n ')
    message = fill()
    print('\nIngrese la matriz encriptación (M):\n ')
    crypt_m = fill()
    reverse_m = np.linalg.inv(crypt_m)
    print(f'La matriz invversa de M es:\n {reverse_m}')
    identity = np.dot(crypt_m, reverse_m)
    print(f'La matriz identidad de M por inversa de M es:\n {identity}')
    decrypt_message = np.dot(reverse_m, message)
    print(f'La matriz con el mensaje decodificado es:\n {decrypt_message}')


#Aquí es donde se corre la función, repito, no es necesario pero es una buena práctica
if __name__ == '__main__':
    run()