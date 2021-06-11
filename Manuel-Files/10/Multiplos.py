x = int(input('Ingrese x\n'))
a = int(input('Ingrese a\n'))
b = int(input('Ingrese b\n'))
dif = (x - (a % x))
dif += a if dif != x else a - x
lis = []
for i in range(dif, b+1, x):
    lis.append(i)
print(lis)
