"""Escribir un programa que reciba del teclado una cifra y un número natural (un dígito), y diga cuántas veces el dígito aparece en la cifra introducida. (No se pueden utilizar funciones asociadas a strings)."""

# Entrada: Una cifra - un número natural (un dígito)
# Salida: Repeticiones del digito en la cifra
# Al restringir el uso de string no se puede saber si la cifra es una repeticion de 0

cifra = int(input('Ingrese una cifra\n'))
digito = int(input('Ingrese un digito\n'))
apariciones = 0
if cifra == digito:
    apariciones = 1
else:
    while cifra > 0:
        apariciones += int(cifra % 10 == digito)
        cifra = cifra // 10
print("El digito ", digito, " aparece", apariciones, " veces")

