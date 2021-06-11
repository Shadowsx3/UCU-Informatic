"""Hacer un programa que lea un número N, entero y positivo, de cualquier número de
dígitos, que calcule la suma de sus dígitos y que la imprima en pantalla, junto con
el número leído. Ej.: n = 53471, entonces la suma de sus dígitos es Suma = 20."""
import os


def Sumar(numero):
    Suma = 0
    Con = 0
    while Con < len(numero):
        digit = numero[Con]
        Suma += int(digit)
        Con += 1
    return Suma


def Error(stri):
    print(f'Debe ingresar algo valido, el error fue: {stri}')
    print('Saliendo...')


os.system('cls')
while True:
    x = input('Ingrese un numero\n')
    os.system('cls')
    if len(x) == 0:
        Error('No ingresar nada')
        break
    elif x[0] == '-':
        Error('Un numero negativo')
        break
    if not x.isnumeric():
        Error('No es un numero')
        break
    print(f'n = {x}, entonces la suma de sus dígitos es Suma = {Sumar(x)}')

