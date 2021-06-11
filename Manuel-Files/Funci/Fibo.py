def Fibon(N):
    if N < 2:
        return N % 2
    else:
        return Fibon(N - 1) + Fibon(N - 2)


R = Fibon(int(input('Ingrese un numero para realizar la sucesion de fibonacci\n')))
print(f'El resultado es {R}')
