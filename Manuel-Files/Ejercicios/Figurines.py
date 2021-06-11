from os import system
x = int(input('Ingrese el ancho de la figura\n'))
y = int(input('Ingrese el largo de la figura\n'))
c = input('Ingrese el caracter de borde\n')
system("cls")
print(c*x)
for i in range(0, y-2):
    print(c+' '*len(c)*(x-2)+c)
if y > 1:
    print(c*x)
