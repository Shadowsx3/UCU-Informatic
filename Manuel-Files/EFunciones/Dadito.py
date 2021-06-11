import random

num = int(input('Ingrese el numero de tiradas\n'))
dado = int(input('Ingrese el numero de dados\n'))
Ac = 0
dadocopy = dado
cantidad = num
caras = [0, 0, 0, 0, 0, 0]
caras1 = [1, 2, 3, 4, 5, 6]
while 0 < num:
    while 0 < dadocopy:
        n = random.randint(1, 6)
        Ac += n
        caras[n-1] += 1
        dadocopy -= 1
    dadocopy = dado
    num -= 1
print(f'El promedio de hacer {cantidad} tiradas con {dado} dados es: {Ac / cantidad}\n'
      f'La cantidad de veces que salieron las caras\n{caras1} son\n{caras}')
