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
        #Le da la forma deseada a la matriz
        return array

    print('Ingrese la matriz mensaje:\n ')
    message = fill()
    print('\nIngrese la matriz encriptación (M):\n ')
    crypt_m = fill()
    reverse_m = np.linalg.inv(crypt_m)
    np.set_printoptions(suppress=True)
    #Los números muy pequeños los convierte de notación científica a decimal
    decrypt_message = np.dot(reverse_m, message)
    print(f'La matriz con el mensaje decodificado es:\n {decrypt_message}')


#Aquí es donde se corre la función, repito, no es necesario pero es una buena práctica
if __name__ == '__main__':
    run()