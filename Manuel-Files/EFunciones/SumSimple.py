while True:
    x = input('Ingrese un numero\n')
    if len(x) == 0:
        break
    elif x[0] == '-':
        break
    if not x.isnumeric():
        break
    Suma = 0
    Con = 0
    while Con < len(x):
        digit = x[Con]
        Suma += int(digit)
        Con += 1
    print(f'n = {x}, entonces la suma de sus dígitos es Suma = {Suma}')
