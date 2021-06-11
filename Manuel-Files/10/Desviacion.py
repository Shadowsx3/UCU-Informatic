from math import sqrt
from more_itertools import locate

x = input("Ingrese los numeros separados por espacio\n").split()
x = list(map(int, x))
x.sort()
N = list(locate(x, lambda y: y < 0))
if len(N) > 0:
    for i in range(0, N[len(N)-1]+1):
        del(x[i])
s = 0
a = 0
print(x)
for i in x:
    a += i
    s += i*i
n = len(x)
CuaDes = s/n - (a/n)**2
Desviacion = sqrt(CuaDes)
print(f'La desviacion estandar es {Desviacion}')
