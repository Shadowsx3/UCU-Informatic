from math import factorial


def Factorial(nume):
    res = 1
    if nume < 0: res = 'No hay factorial de negativos'
    else:
        while nume > 1:
            res *= nume
            nume -= 1
    return res


x = int(input('Ingrese un numero para hacer el factorial\n'))
print(f'El factorial de {x} es {Factorial(x)}')
print(f'El factorial segun math de {x} es {factorial(x)}')
