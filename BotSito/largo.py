n = int(input("Ingrese la cantidad denumeros\n"))
x = 1
primos = 0
contador = 0
divisores = 0
inicio = 2
while contador < n:
    num = int(input("Ingrese un numero\n"))
    if num != 2:
        while inicio < num:
            if num % inicio == 0:
                divisores += 1
            inicio += 1
    if divisores == 0:
        primos += 1
    divisores = 0
    contador += 1
    inicio = 2
print(f"La cantidad de primos es {primos}")
