#Este programa sólo funciona con matrices encripatadas de dos filas
#Dará error si el mensaje encripatdo o el descencriptado lleva un cero
def run():
    import numpy as np
    import string

    num2alpha =dict(zip(range(1,27),string.ascii_letters))
    #Crea un diccionario con la enumarción ascii en inglés. El cero no lo toma en cuenta, por eso no
    #lo pude colocar en la matriz del documento de word, espero se entienda.

    def fill():
        n = int(input('Ingrese el número de filas:'))
        m = int(input('Ingrese el número de columnas: '))
        
        list=[]
        print('Ingrese los elementos de la matriz: ')
        for i in range(n):
            for j in range(m):
                num = float(input(f'Elemento {i+1},{j+1}: '))
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
    #Me enteré de que no todas las matrices cuadradas tienen inversa
    decrypt_message = np.dot(reverse_m, message)
    dm_T = decrypt_message.T
    #Transpuesta de la matriz
    dm_Trow = dm_T.ravel()
    #Aplana la transpuesta, formando una matriz renglón
    dm_Trowlist = dm_Trow.flatten().tolist()
    # Lo convierte en texto, y luego en lista python
    print("EL MENSAJE DECIFRADO DICE: ")
    for num in dm_Trowlist:
        print(num2alpha[num])   
     
if __name__ == '__main__':
    run()