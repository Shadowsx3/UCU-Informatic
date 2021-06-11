"""
Realizar un programa que lea n números enteros positivos del teclado y que calcule cuantos son pares y cuantos son
 impares. El programa debe detenerse cuando se ingrese un cero.
Entrada: n pasa saber cuantos leera - numeros
Salida:Cantidad de pares e impares
El tipo[0] serán pares, el tipo[1] serán impares
"""
tipo = [0, 0]
n = int(input("Ingrese cuantos numeros se leeran\n"))
for i in range(0, n):
    num = int(input("Ingrese un número\n"))
    if num == 0:
        break
    tipo[num % 2] += 1
print(f'Hay {tipo[0]} números pares y {tipo[1]} números impares')
