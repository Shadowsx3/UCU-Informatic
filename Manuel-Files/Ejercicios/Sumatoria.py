from more_itertools import locate
x = input("Ingrese los numeros separados por espacio\n").split()
x = list(map(int, x))
x.sort()
N = list(locate(x, lambda y: y <= 0))
i = len(x)-1
acum = 0
while i > len(N)-1:
    acum += x[i]
    i -= 1
print(f'LA sumatoria es: {acum}')
