Cantidad = int(input('Ingrese la cantidad de numeros a leer\n'))
Tipos = [0, 0, 0]
x = 0
for i in range(0, Cantidad):
    Num = int(input('Ingrese un numero\n'))
    if Num < 0:
        x = 0
    elif Num == 0:
        x = 1
    else:
        x = 2
    Tipos[x] += 1
print('La cantidades son\nNegativos :', Tipos[0], '\nCeros :', Tipos[1], '\nPositivos : ', Tipos[2])