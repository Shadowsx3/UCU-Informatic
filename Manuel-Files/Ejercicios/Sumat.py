N = int(input('Ingrese el valor de N\n'))
suma = 0
for i in range(2, N+1):
    suma += i**2/(i**2-1)
print(f'La sumatoria da {suma}')

