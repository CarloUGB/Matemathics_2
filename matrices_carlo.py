def run():

    def fill():
        m = int(input('INGRESE EL NUMERO DE FILAS:'))
        n = int(input('INGRESE EL NUMERO DE COLUMNAS:'))
        a = []
        for i in range(m):
            b = []
            for j in range(n):
                 b.append(int(input(f'Ingrese el elemento {(i+1,j+1)}:')))
            a.append(b)
        return a

    def determinant_m():
        pass


    print('INGRESE LA MATRIZ CON MENSAJE ENCRIPTADO:')
    crypt_message = fill()
    print(crypt_message)
    print('INGRESE LA MATRIZ DE DESENCRIPTADO (M):')
    decrypt = fill()
    print(decrypt)
    # print('INGRESE LA MATRIZ IDENTIDAD DE M:')
    # identity: fill()
    
    
if __name__ == '__main__':
    run()