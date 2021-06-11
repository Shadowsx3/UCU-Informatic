def Calcular(Num):
    suma = 0
    for i in Num:
        suma += int(i)
    return suma == 21


R = Calcular(input('Ingrese un numero para saber si es de la suerte\n'))
print(f'El resultado es {R}')
