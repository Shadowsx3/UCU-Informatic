"""
Realice un programa que pida los siguientes datos:
    - Código del medidor (string),
    - Lectura anterior y lectura actual (enteros)
El programa debe calcular el monto de la factura e imprimir el siguiente mensaje:
    - Código del medidor: <código del medidor>
    - Monto de la Factura: <monto>
Si se consumen 500 Kwh o menos, el costo es de 2$ por cada Kwh
Si se consumen más de 500 Kwh, pero menos de 1001, el costo es 1200$ por los primeros 500 Kwh y
5$ por Kwh, para  el consumo que exceda los 500 Kwh
Si se consumen más de 1000 Kwh, el costo es 4000$ por los primeros 1000 Kwh y 9$ por Kwh, para el consumo que exceda los
1000 Kwh
La compañía eléctrica incluye en la factura un gasto fijo de 200$, independiente del consumo. Además, al monto final
 debe sumarse el IVA del 22%.
"""


def Calcular(LecAnterior, LecActual):
    # La compañía eléctrica incluye en la factura un gasto fijo de 200$
    costo = 200
    while LecActual < LecAnterior:
        LecActual = LeerFloat('Por favor, ingrese una lectuara actual mayor a la anterior')
    consumo = LecActual - LecAnterior
    if consumo <= 500:
        # El costo es de 2$ por cada Kwh
        costo += consumo * 2
    elif consumo <= 1000:
        # El costo es 1200$
        # 5$ por Kwh, para  el consumo que exceda los 500 Kwh
        costo += 1200 + (consumo - 500) * 5
    else:
        # El costo es 4000$ por los primeros 1000 Kwh
        # 9$ por Kwh, para el consumo que exceda los 1000 Kwh
        costo += 4000 + (consumo - 1000) * 9
    return costo * 1.22


def LeerFloat(texto):
    numero = input(f'{texto}\n')
    if numero.isnumeric():
        return float(numero)
    else:
        print('Error: No es un numero valido')
        return LeerFloat(texto)


while True:
    codigo = input('Ingrese el código del medidor\n')
    lecAnt = LeerFloat('Ingrese la lectura anterior')
    lectActual = LeerFloat('Ingrese la lectura actual')
    # El programa debe calcular el monto de la factura e imprimir el siguiente mensaje:
    # Código del medidor: <código del medidor>
    # Monto de la Factura: <monto>
    print(f'Código del medidor: {codigo}\nMonto de la Factura: {Calcular(lecAnt, lectActual)}')
    continuar = input('Si desea salir presione enter\n')
    if continuar == '':
        break
