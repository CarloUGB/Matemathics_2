#Esta es una función principal, no es necesaria para este ejercicio
#pero aprendí que es una buena práctica
def run():
    import numpy as np

    def rows():
         n = int(input('Ingrese el número de filas:'))
         return n

    def columns():
        m = int(input('Ingrese el número de columnas: '))
        return m


    def fill(n,m):
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
    n_1 = rows()
    m_1 = columns()
    message = fill(n_1,m_1)
    print('\nIngrese la matriz encriptación (M):\n ')
    n_2 = rows()
    m_2 = columns()
    crypt_m = fill(n_2,m_2)

    reverse_m = np.linalg.inv(crypt_m)
    np.set_printoptions(suppress=True)
    #Los números muy pequeños los convierte de notación científica a decimal
    decrypt_message = np.dot(reverse_m, message)
    dm_T = decrypt_message.T
    #Transpuesta de la matriz
    dm_Trow = dm_T.ravel()
    #Aplana la transpuesta, formando una matriz renglón
    print(f'La matriz con el mensaje decodificado es:\n {dm_Trow}')
    

#Aquí es donde se corre la función, repito, no es necesario pero es una buena práctica
if __name__ == '__main__':
    run()