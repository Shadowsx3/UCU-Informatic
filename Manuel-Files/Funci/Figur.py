def Calcul(Car, Num):
    Datos = Car.split(' ')
    Cantidad = Num.split(' ')
    New = 0
    if not int(Datos[1]) == 0:
        New = int(max(Cantidad))
    for i in Cantidad:
        print(' '*(New-int(i))*len(Datos[0])+Datos[0]*int(i))


Calcul(input('Ingrese el caracter seguido de 1 para izquierda o 0 para derecha\n'),
       input('Ingrese la cantidad de caracteres por linea separados por espacios\n'))
