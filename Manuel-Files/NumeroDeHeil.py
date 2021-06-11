from more_itertools import locate
x = input("Ingrese los numeros separados por espacio\n").split()
x = list(map(int, x))
x.sort()
N = list(locate(x, lambda y: y < 0))
C = list(locate(x, lambda y: y == 0))
P = list(locate(x, lambda y: y > 0))
print(f'Las cantidades son \nPositivos: {len(P)}\n{P}\nCeros: {len(C)}\n{C}\nNegativos: {len(N)}\n{N}')
